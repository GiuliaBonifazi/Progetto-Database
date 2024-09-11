from backend import get_database

def get_movies():
    db = get_database()
    cur = db.execute("SELECT Titolo, Titolo Originale, Durata, Valutazione, AnnoUscita, PaeseProduzione, CodRegista, CodFilm FROM FILM")
    return cur.fetchall()

def get_series():
    db = get_database()
    cur = db.execute("SELECT * FROM SERIE")
    return cur.fetchall()

def get_seasons_for_series(id: int):
    db = get_database()
    cur = db.execute("SELECT * FROM STAGIONE WHERE CodSerie=? ORDER BY NumStagione")
    return cur.fetchall()

def get_director_name(id):
    db = get_database()
    cur = db.execute("SELECT NomeArte FROM MEMBRO_DEL_CAST WHERE CodMembroCast=?", (id,))
    return cur.fetchone()

def get_movie_actors_names(movieId):
    db = get_database()
    cur = db.execute("SELECT NomeArte FROM MEMBRO_DEL_CAST JOIN RECITAZIONE_FILM ON CodMembroCast=CodAttore WHERE CodFilm=?", (movieId,))
    return cur.fetchall()