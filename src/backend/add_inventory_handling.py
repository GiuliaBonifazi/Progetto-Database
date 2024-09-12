from backend import get_database

def get_all_directors():
    db = get_database()
    cur = db.execute("SELECT NomeArte, CodMembroCast FROM MEMBRO_DEL_CAST WHERE Regista=true")
    return cur.fetchall()

def get_all_actors():
    db = get_database()
    cur = db.execute("SELECT NomeArte, CodMembroCast FROM MEMBRO_DEL_CAST WHERE Attore=true")
    return cur.fetchall()