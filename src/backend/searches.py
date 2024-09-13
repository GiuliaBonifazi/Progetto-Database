from backend import get_database

def search_movie_db(type: str, search):
    db = get_database()
    query = "SELECT Titolo, TitoloOriginale, Durata, Valutazione, AnnoUscita, PaeseProduzione, CodRegista, CodFilm FROM FILM WHERE "
    match type:
        case "DIR":
            query += "CodRegista IN (SELECT CodRegista FROM MEMBRO_DEL_CAST WHERE NomeArte LIKE '%' || ? || '%')"
            cur = db.execute(query, (search,))
        case "YEA":
            query += "AnnoUscita=?"
            cur = db.execute(query, (int(search),))
        case "TTL":
            query += "Titolo LIKE '%' || ? || '%' OR TitoloOriginale LIKE '%' || ? || '%'"
            cur = db.execute(query, (search, search))
        case "ACT":
            query += "CodFilm IN (SELECT CodFilm FROM RECITAZIONE_FILM JOIN MEMBRO_DEL_CAST \
                    ON CodAttore=CodMembroCast WHERE NomeArte LIKE '%' || ? || '%')"
            cur = db.execute(query, (search,))
    return cur.fetchall()

def search_series_db(type: str, search):
    db = get_database()
    query = "SELECT Titolo, TitoloOriginale, Valutazione, AnnoUscita, PaeseProduzione, CodSerie FROM SERIE WHERE "
    match type:
        case "YEA":
            query += "AnnoUscita=?"
            cur = db.execute(query, (int(search),))
        case "TTL":
            query += "Titolo LIKE '%' || ? || '%' OR TitoloOriginale LIKE '%' || ? || '%'"
            cur = db.execute(query, (search, search))
        case "ACT":
            query += "CodSerie IN (SELECT CodSerie FROM RECITAZIONE_SERIE JOIN MEMBRO_DEL_CAST \
                    ON CodAttore=CodMembroCast WHERE NomeArte LIKE '%' || ? || '%')"
            cur = db.execute(query, (search,))
    return cur.fetchall() 