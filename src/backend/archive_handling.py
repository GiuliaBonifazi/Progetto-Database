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

def get_movie_genres(movieId: int):
    db = get_database()
    cur = db.execute("SELECT Nome FROM GENERE LEFT JOIN GENERE_FILM ON GENERE.Nome=GENERE_FILM.Genere WHERE CodFilm=?", (movieId,))
    return cur.fetchall()

def get_series_genres(seriesId: int):
    db = get_database()
    cur = db.execute("SELECT Nome FROM GENERE LEFT JOIN GENERE_SERIE ON GENERE.Nome=GENERE_SERIE.Genere WHERE CodSerie=?", (seriesId,))
    return cur.fetchall()

def rent_movie_copy(movieId: int, support: str):
    db = get_database()
    cur = db.execute("SELECT CodCopia FROM COPIA_ARTICOLO WHERE CodFilm=? AND Disponibilita=true AND Supporto=?", (movieId, support))
    row = cur.fetchone()
    if row is None:
        return ("Spiacente, quel formato non è al momento disponibile.", False)
    else:
        return (cur.fetchone(), True)
    
def get_series_actors_names(seriesId: int):
    db = get_database()
    cur = db.execute("SELECT NomeArte FROM MEMBRO_DEL_CAST JOIN RECITAZIONE_SERIE ON CodMembroCast=CodAttore WHERE CodSerie=?", (seriesId,))
    return cur.fetchall()

def get_series():
    db = get_database()
    cur = db.execute("SELECT Titolo, TitoloOriginale, Valutazione, AnnoUscita, PaeseProduzione, CodSerie FROM SERIE")
    return cur.fetchall()

def get_languages():
    db = get_database()
    cur = db.execute("SELECT Denominazione FROM LINGUA")
    return cur.fetchall()

def get_genres():
    db = get_database()
    cur = db.execute("SELECT Nome FROM GENERE")
    return cur.fetchall()

def get_seasons_from_series(seriesId: int):
    db = get_database()
    cur = db.execute("SELECT CodSerie, NumStagione, NumeroEpisodi, Valutazione, AnnoUscita, PaeseProduzione FROM STAGIONE WHERE CodSerie=? ORDER BY NumStagione", (seriesId,))
    return cur.fetchall()

def rent_series(seriesId: int, support: str):
    db = get_database()
    cur = db.execute("Select CodCopia FROM COPIA_ARTICOLO WHERE CodSerie=? AND Supporto=? AND Disponibilita=true", (seriesId, support))
    row = cur.fetchone()
    if row is None:
        return ("Spiacente, quel formato non è al momento disponibile.", False)
    else:
        return (cur.fetchone(), True)
    
def rent_season(seriesId: int, seasonNum: int, support: str):
    db = get_database()
    cur = db.execute("Select CodCopia FROM COPIA_ARTICOLO WHERE CodSerie=? AND NumStagione=? AND Supporto=? AND Disponibilita=true",
                    (seriesId, seasonNum, support))
    row = cur.fetchone()
    if row is None:
        return ("Spiacente, quel formato non è al momento disponibile.", False)
    else:
        return (cur.fetchone(), True)