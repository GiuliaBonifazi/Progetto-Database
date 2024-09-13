from backend import get_database

def get_top_ten_couples():
    db = get_database()
    cur = db.execute(
        """
        SELECT CodRegista, CodAttore, COUNT(RF.CodFilm) as tot FROM 
        RECITAZIONE_FILM AS RF LEFT JOIN FILM 
        ON RF.CodFilm=FILM.CodFilm
        GROUP BY CodRegista, CodAttore
        ORDER BY tot DESC
        LIMIT 10
        """)
    return cur.fetchall()
    
def get_top_ten_genres():
    db = get_database()
    cur = db.execute("""
                     WITH SeriePerGenere(Genere, Serie) AS 
                            (SELECT Genere, COUNT(*) FROM GENERE_SERIE GROUP BY Genere), 
                    FilmPerGenere(Genere, Film) AS 
                            (SELECT Genere, COUNT(*) FROM GENERE_FILM GROUP BY Genere) 
                    SELECT COALESCE(F.Genere, S.Genere) as gen, SUM(COALESCE(Film, 0) + COALESCE(Serie,0)) as tot FROM 
                            (FilmPerGenere AS F FULL OUTER JOIN SeriePerGenere AS S ON F.Genere=S.Genere) 
                    GROUP BY gen 
                    ORDER BY tot DESC 
                    LIMIT 10
                    """)
    return cur.fetchall()
    
def get_top_ten_rated_actors():
    db = get_database()
    cur = db.execute(
        """
                     
        """)