from backend import get_database

def get_all_directors():
    db = get_database()
    cur = db.execute("SELECT NomeArte, CodMembroCast FROM MEMBRO_DEL_CAST WHERE Regista=true")
    return cur.fetchall()

def get_all_actors():
    db = get_database()
    cur = db.execute("SELECT NomeArte, CodMembroCast FROM MEMBRO_DEL_CAST WHERE Attore=true")
    return cur.fetchall()

def add_movie(title: str, ogTitle: str, runtime: int, mark: int, year: int, country: str, director: int, actors):
    db = get_database()
    cur = db.execute("INSERT INTO FILM (Titolo, TitoloOriginale, Durata, Valutazione, AnnoUscita, PaeseProduzione, CodRegista) \
                        VALUES (?, ?, ?, ?, ?, ?, ?)", (title, ogTitle, runtime, mark, year, country, director))
    filmId = cur.lastrowid
    db.commit()
    for act in actors:
        db.execute("INSERT INTO RECITAZIONE_FILM (CodAttore, CodFilm) VALUES (?, ?)", (act, filmId))
        db.commit()

def add_series(title: str, ogTitle: str, mark: int, year: int, country: str, actors):
    db = get_database()
    cur = db.execute("INSERT INTO SERIE (Titolo, TitoloOriginale, Valutazione, AnnoUscita, PaeseProduzione) \
                     VALUES (?, ?, ?, ?, ?)", (title, ogTitle, mark, year, country))
    seriesId = cur.lastrowid
    db.commit()
    for act in actors:
        db.execute("INSERT INTO RECITAZIONE_SERIE (CodAttore, CodSerie) VALUES (?, ?)", (act, seriesId))
        db.commit()