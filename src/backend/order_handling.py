from backend import get_database

def get_order_items(copyIds):
    items = []
    db = get_database()
    for id in copyIds:
        cur = db.execute("SELECT SERIE.Titolo, FILM.Titolo, NumStagione, Supporto \
                         FROM SERIE RIGHT JOIN \
                        (COPIA_ARTICOLO LEFT JOIN FILM ON COPIA_ARTICOLO.CodFilm=FILM.CodFilm) \
                        ON SERIE.CodSerie=COPIA_ARTICOLO.CodSerie \
                        WHERE CodCopia=?", (id,))
        data = cur.fetchone()
        cur = db.execute("SELECT Lingua FROM LINGUA_COPIA WHERE CodCopia=?", (id,))
        languages = cur.fetchall()
        items.append((data, languages))
    return items

def get_order_items_with_position(copyIds):
    items = []
    db = get_database()
    for id in copyIds:
        cur = db.execute("SELECT SERIE.Titolo, FILM.Titolo, NumStagione, Supporto, Scaffale, Scaffalatura \
                         FROM SERIE RIGHT JOIN \
                        (COPIA_ARTICOLO LEFT JOIN FILM ON COPIA_ARTICOLO.CodFilm=FILM.CodFilm) \
                        ON SERIE.CodSerie=COPIA_ARTICOLO.CodSerie \
                        WHERE CodCopia=?", (id,))
        data = cur.fetchone()
        cur = db.execute("SELECT Lingua FROM LINGUA_COPIA WHERE CodCopia=?", (id,))
        languages = cur.fetchall()
        items.append((data, languages))
    return items