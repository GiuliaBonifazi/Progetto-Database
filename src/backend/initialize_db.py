from backend import get_database


def create():
    db = get_database()
    with open('src/backend/db_sqlite.sql', 'r') as file:
        script = file.read()
    db.executescript(script)
    db.commit()
    

def fill():
    db = get_database()
    with open('src/backend/db_fill.sql', 'r') as file:
        script = file.read()
    db.executescript(script)
    db.commit()