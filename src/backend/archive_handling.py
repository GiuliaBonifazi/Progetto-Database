from backend import get_database

def get_movies():
    db = get_database()
    cur = db.execute("SELECT Titolo, TitoloOriginale, Durata, Valutazione, AnnoUscita, PaeseProduzione, CodRegista, CodFilm FROM FILM")
    return cur.fetchall()

def get_cast_member_name(id: int):
    db = get_database()
    cur = db.execute("SELECT NomeArte FROM MEMBRO_DEL_CAST WHERE CodMembroCast=?", (id,))
    return cur.fetchone()

def get_movie_actors_names(movieId: int):
    db = get_database()
    cur = db.execute("SELECT NomeArte FROM MEMBRO_DEL_CAST JOIN RECITAZIONE_FILM ON CodMembroCast=CodAttore WHERE CodFilm=?", (movieId,))
    return cur.fetchall()

def get_movie_genres(movieId: int):
    db = get_database()
    cur = db.execute("SELECT Genere FROM GENERE_FILM WHERE CodFilm=?", (movieId,))
    return cur.fetchall()

def get_series_genres(seriesId: int):
    db = get_database()
    cur = db.execute("SELECT Genere FROM GENERE_SERIE WHERE CodSerie=?", (seriesId,))
    rows = cur.fetchall()
    return rows

def rent_movie_copy(movieId: int, support: str):
    db = get_database()
    cur = db.execute("SELECT CodCopia FROM COPIA_ARTICOLO WHERE CodFilm=? AND Disponibilita=true AND Supporto=?", (movieId, support))
    row = cur.fetchone()
    if row is None:
        return ("Spiacente, quel formato non è al momento disponibile.", False)
    else:
        return (row, True)
    
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
    series = get_seasons_from_series(seriesId)
    if series == []:
        return ("Spiacente, la serie non ha alcuna stagione", False)
    seasons = []
    for s in series:
        res, success = rent_season(seriesId, s[1], support)
        if not success:
            return ("Spiacente, quel formato non è al momento disponibile per la stagione " + str(s[1]), False)
        else:
            seasons.append(res[0])
    return (seasons, True)
    
def rent_season(seriesId: int, seasonNum: int, support: str):
    db = get_database()
    cur = db.execute("Select CodCopia FROM COPIA_ARTICOLO WHERE CodSerie=? AND NumStagione=? AND Supporto=? AND Disponibilita=true",
                    (seriesId, seasonNum, support))
    row = cur.fetchone()
    if row is None:
        return ("Spiacente, quel formato non è al momento disponibile.", False)
    else:
        return (row, True)