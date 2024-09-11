from backend import get_database

def login_check(email: str, password: str):
    db = get_database()
    cur = db.execute("SELECT COUNT(*) FROM UTENTE WHERE Email=? AND Password=?", (email, password))
    return cur.fetchone()[0] == 1

def find_user(email: str, password: str):
    db = get_database()
    cur = db.execute("SELECT * FROM UTENTE WHERE Email=? AND Password=?", (email, password))
    return cur.fetchone()

def register_user(email: str, password: str, name: str, surname: str, cell: int):
    db = get_database()
    db.execute("INSERT INTO UTENTE (Password, Nome, Cognome, Email, NumTelefono) values (?, ?, ?, ?, ?)", 
                    (password, name, surname, email, cell))
    db.commit()
    
def repeat_email(email: str):
    db = get_database()
    cur = db.execute("SELECT COUNT(*) FROM UTENTE WHERE Email=?", (email,))
    return cur.fetchone()[0] == 1