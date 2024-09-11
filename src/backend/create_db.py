from .database import get_database


def create():
    with open('src/backend/db_sqlite.sql', 'r') as file:
        script = file.read()
    get_database().executescript(script)
    
