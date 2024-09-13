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
        WITH ValutazioniAttoriFilm(CodAttore, ValFilm) AS
            (SELECT CodAttore, AVG(Valutazione) FROM RECITAZIONE_FILM AS RF JOIN FILM ON RF.CodFilm=FILM.CodFilm GROUP BY CodAttore),
        ValutazioniAttoriSerie(CodAttore, ValSerie) AS
            (SELECT CodAttore, AVG(Valutazione) FROM RECITAZIONE_SERIE AS RS JOIN SERIE ON RS.CodSerie=SERIE.CodSerie GROUP BY CodAttore)
        SELECT COALESCE(VF.CodAttore, VS.CodAttore) as attore, (COALESCE(ValSerie, ValFilm) + COALESCE(ValFilm, ValSerie))/2 AS mf
        FROM ValutazioniAttoriFilm AS VF FULL OUTER JOIN ValutazioniAttoriSerie AS VS ON VF.CodAttore=VS.CodAttore
        GROUP BY attore
        ORDER BY mf DESC
        """)
    return cur.fetchall()

def top_ten_rated_directors():
    db = get_database()
    cur = db.execute(
    """
    SELECT CodRegista, AVG(Valutazione) as val
    FROM FILM
    GROUP BY CodRegista
    ORDER BY val DESC
    """
    )
    return cur.fetchall()