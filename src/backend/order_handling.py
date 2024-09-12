from backend import get_database
from datetime import date

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

def confirm_order(copyIds, pickUpDate, userId: int):
    db = get_database()
    orderDate = date.today()
    cur = db.execute("INSERT INTO PRENOTAZIONE (DataConferma, DataRitiro, CodUtente) VALUES (?, ?, ?)", (orderDate, pickUpDate, userId))
    orderId = cur.lastrowid
    db.commit()
    for id in copyIds:
        db.execute("UPDATE COPIA_ARTICOLO SET Disponibilita=false WHERE CodCopia=?", (id,))
        db.execute("INSERT INTO RICHIESTA (CodPrenotazione, CodCopia) VALUES (?, ?)", (orderId, id))
        db.commit()
        
def all_orders_from_user(userId: int):
    db = get_database()
    cur = db.execute("SELECT CodPrenotazione FROM PRENOTAZIONE WHERE CodUtente=?", (userId,))
    orders = []
    for orderId in cur.fetchall():
        cur = db.execute("SELECT DataConferma, DataRitiro, RitiroEffettuato, ConsegnaEffettuata FROM PRENOTAZIONE WHERE CodPrenotazione=?", (orderId[0],))
        data = cur.fetchone()
        cur = db.execute("SELECT CodCopia FROM RICHIESTA WHERE CodPrenotazione=?", (orderId[0],))
        orders.append((data, [x[0] for x in cur.fetchall()]))
    return orders