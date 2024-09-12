from backend import get_database

def users_from_name_surname(name: str, surname: str):
    db = get_database()
    cur = db.execute("SELECT CodUtente FROM UTENTE WHERE Nome LIKE ? AND Cognome LIKE ?", (name, surname))
    return cur.fetchall()

def all_user_names():
    db = get_database()
    cur = db.execute("SELECT Nome FROM UTENTE")
    return cur.fetchall()

def all_user_surnames():
    db = get_database()
    cur = db.execute("SELECT Cognome FROM UTENTE")
    return cur.fetchall()