from backend import get_database

def search_movie_db(type: str, search: str):
    db = get_database()
    query = "SELECT Titolo, TitoloOriginale, Durata, Valutazione, AnnoUscita, PaeseProduzione, CodRegista, CodFilm FROM FILM WHERE "
    match type:
        case "DIR":
            query += "CodRegista IN (SELECT CodRegista FROM MEMBRO_DEL_CAST WHERE NomeArte LIKE '%' || ? || '%')"
            cur = db.execute(query, (search,))
        case "YEA":
            query += "AnnoUscita=?"
            cur = db.execute(query, (search,))
        case "TTL":
            query += "Titolo LIKE '%' || ? || '%' OR TitoloOriginale LIKE '%' || ? || '%'"
            cur = db.execute(query, (search, search))
        case "ACT":
            query += "CodFilm IN (SELECT CodFilm FROM RECITAZIONE_FILM JOIN MEMBRO_DEL_CAST \
                    ON CodAttore=CodMembroCast WHERE NomeArte LIKE '%' || ? || '%')"
            cur = db.execute(query, (search,))
    return cur.fetchall()
            