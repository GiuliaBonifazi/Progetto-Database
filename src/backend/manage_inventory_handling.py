from backend import get_database, get_order_items_with_position

def get_copies_info_from_series(seriesId: int):
    db = get_database()
    cur = db.execute("SELECT CodCopia FROM COPIA_ARTICOLO WHERE CodSerie=?", (seriesId,))
    items = get_order_items_with_position([x[0] for x in cur.fetchall()])
    return items
    
def get_copies_info_from_movie(movieId: int):
    db = get_database()
    cur = db.execute("SELECT CodCopia FROM COPIA_ARTICOLO WHERE CodFilm=?", (movieId,))
    items = get_order_items_with_position([x[0] for x in cur.fetchall()])
    return items

