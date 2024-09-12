from backend import get_database

def get_movies():
    db = get_database()
    cur = db.execute("SELECT Titolo, TitoloOriginale, Durata, Valutazione, AnnoUscita, PaeseProduzione, CodRegista, CodFilm FROM FILM")
    return cur.fetchall()

def get_director_name(id: int):
    db = get_database()
    cur = db.execute("SELECT NomeArte FROM MEMBRO_DEL_CAST WHERE CodMembroCast=?", (id,))
    return cur.fetchone()

def get_movie_actors_names(movieId: int):
    db = get_database()
    cur = db.execute("SELECT NomeArte FROM MEMBRO_DEL_CAST JOIN RECITAZIONE_FILM ON CodMembroCast=CodAttore WHERE CodFilm=?", (movieId,))
    return cur.fetchall()

def rent_movie_copy(movieId: int, support: str):
    db = get_database()
    cur = db.execute("SELECT CodCopia FROM COPIA_ARTICOLO WHERE CodFilm=? AND Disponibilita=true AND Supporto=?", (movieId, support))
    if (cur.rowcount == 0):
        return None
    else:
        return cur.fetchone()
    
def get_series_actors_names(seriesId: int):
    db = get_database()
    cur = db.execute("SELECT NomeArte FROM MEMBRO_DEL_CAST JOIN RECITAZIONE_SERIE ON CodMembroCast=CodAttore WHERE CodSerie=?", (seriesId,))
    return cur.fetchall()

def get_series():
    db = get_database()
    # cur = db.execute("SELECT * FROM STAGIONE")
    # print(cur.fetchall())
    cur = db.execute("SELECT Titolo, TitoloOriginale, Valutazione, AnnoUscita, PaeseProduzione, CodSerie FROM SERIE")
    return cur.fetchall()

def get_seasons_from_series(seriesId: int):
    db = get_database()
    cur = db.execute("SELECT CodSerie, NumStagione, NumeroEpisodi, Valutazione, AnnoUscita, PaeseProduzione FROM STAGIONE WHERE CodSerie=? ORDER BY NumStagione", (seriesId,))
    return cur.fetchall()

def rent_series(seriesId: int, support: str):
    db = get_database()
    cur = db.execute("Select CodCopia FROM COPIA_ARTICOLO WHERE CodSerie=? AND Supporto=? AND Disponibilita=true", (seriesId, support))
    if (cur.rowcount == 0):
        return None
    else:
        return cur.fetchone()
    
def rent_season(seriesId: int, seasonNum: int, support: str):
    db = get_database()
    cur = db.execute("Select CodCopia FROM COPIA_ARTICOLO WHERE CodSerieStagione=? AND NumStagione=? AND Supporto=? AND Disponibilita=true",
                    (seriesId, seasonNum, support))
    if (cur.rowcount == 0):
        return None
    else:
        return cur.fetchone()