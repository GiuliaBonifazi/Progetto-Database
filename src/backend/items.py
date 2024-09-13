from backend import get_database

def is_item_in_order(copyId: int):
    db = get_database()
    cur = db.execute("SELECT CodPrenotazione FROM RICHIESTA WHERE CodCopia=?", (copyId,))
    row = cur.fetchone()
    return row is None

def delete_item_from_inv(copyId: int):
    if not is_item_in_order(copyId):
        return ("Spiacente, l'articolo non può essere cancellato causa mantenimento dello storico prenotazioni", False)
    else:
        db = get_database()
        db.execute("DELETE FROM LINGUA_COPIA WHERE CodCopia=?", (copyId,))
        db.commit()
        db.execute("DELETE FROM COPIA_ARTICOLO WHERE CodCopia=?", (copyId,))
        db.commit()
        return ("", True)