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
        
def add_season(seriesId: int, numSeason: int, numEpisodes: int, mark: int, year: int, country: str, actors):
    db = get_database()
    db.execute("INSERT INTO STAGIONE (CodSerie, NumStagione, NumeroEpisodi, Valutazione, AnnoUscita, PaeseProduzione) \
                      VALUES (?, ?, ?, ?, ?, ?)", (seriesId, numSeason, numEpisodes, mark, year, country))
    db.commit()
    for act in actors:
        db.execute("INSERT INTO RECITAZIONE_STAGIONE (CodAttore, CodSerie, NumStagione) VALUES (?, ?, ?)", (act, seriesId, numSeason))
        db.commit()
        
def add_cast(name: str, birth: str, death: str, isActor: bool, isDirector: bool):
    db = get_database()
    db.execute("INSERT INTO MEMBRO_DEL_CAST (NomeArte, DataNascita, DataMorte, Attore, Regista) VALUES (?, ?, ?, ?, ?)",
               (name, birth, death, isActor, isDirector))
    db.commit()

def check_for_shelving(shelving: int):
    db = get_database()
    cur = db.execute("SELECT COUNT(*) FROM SCAFFALATURA WHERE CodScaffalatura=?", (shelving,))
    return cur.fetchone()[0] > 0

def check_for_shelf(shelving: int, shelf: int):
    db = get_database()
    cur = db.execute("SELECT COUNT(*) FROM SCAFFALE WHERE CodScaffalatura=? AND NumScaffale=?", (shelving, shelf))
    return cur.fetchone()[0] > 0

def add_shelf(shelf: int, shelving: int):
    if not check_for_shelf(shelving, shelf):
        if check_for_shelving(shelving):
            db = get_database()
            db.execute("INSERT INTO SCAFFALE (NumScaffale, CodScaffalatura) VALUES (?, ?)", (shelf, shelving))
            db.commit()
            return ("", True)
        else:
            return ("La scaffalatura selezionata non esiste", False)
    else:
        return ("Lo scaffale inserito esiste già", False)
    
def add_shelving(shelving: int):
    if check_for_shelving(shelving):
        return ("La scaffalatura inserita esiste già", False)
    else:
        db = get_database()
        db.execute("INSERT INTO SCAFFALATURA (CodScaffalatura) VALUES (?)", (shelving,))
        db.commit()
        return ("", True)
    
def check_genre(genre: str):
    db = get_database()
    cur = db.execute("SELECT COUNT(*) FROM GENERE WHERE Nome=?", (genre,))
    return cur.fetchone()[0] > 0

def check_language(lang: str):
    db = get_database()
    cur = db.execute("SELECT COUNT(*) FROM LINGUA WHERE Denominazione=?", (lang,))
    return cur.fetchone()[0] > 0

def add_genre(genre: str):
    if check_genre(genre):
        return ("Il genere inserito esiste già", False)
    else:
        db = get_database()
        db.execute("INSERT INTO GENERE (Nome) VALUES (?)", (genre,))
        db.commit()
        return ("", True)
    
def add_language(lang: str):
    if check_language(lang):
        return ("La lingua inserita esiste già", False)
    else:
        db = get_database()
        db.execute("INSERT INTO LINGUA (Denominazione) VALUES (?)", (lang,))
        db.commit()
        return ("", True)