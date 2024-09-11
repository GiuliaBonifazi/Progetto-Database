import sqlite3

class CustomConnection(sqlite3.Connection):
    """
    In sqlite3 foreign_keys are disabled by default.
    This custom connection enables them for every database connection
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.execute("PRAGMA foreign_keys = ON")


database = None


def get_database():
    global database
    if not database:
        database = sqlite3.connect("videonoleggio.db", factory=CustomConnection)
    return database

def execute(query: str):
    database = get_database()
    database.execute(query)
    database.commit()
    