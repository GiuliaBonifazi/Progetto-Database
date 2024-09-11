from backend import get_database

def login_check(email: str, password: str):
    db = get_database()
    cur = db.execute("SELECT COUNT(*) FROM UTENTE WHERE Email=? AND Password=?", (email, password))
    return cur.fetchone()[0] == 1

def find_user(email: str, password: str):
    db = get_database()
    cur = db.execute("SELECT * FROM UTENTE WHERE Email=? AND Password=?", (email, password))
    return cur.fetchall()