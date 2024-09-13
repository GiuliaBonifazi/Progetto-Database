from backend import get_database

def get_top_ten_couples():
    db = get_database()
    db.execute("SELECT Genere, SUM(NumFilm + NumSerie) AS Num FROM \
                        (SELECT G.Genere, COUNT(CodFilm) AS NumFilm, COUNT(CodSerie) AS NumSerie \
                        FROM (GENERE_FILM AS GF LEFT JOIN GENERE_SERIE GS ON GF.Genere=GS.Genere) AS G \
                        GROUP BY G.Genere) \
                    GROUP BY Genere \
                    ORDER BY Num DESC \
                    LIMIT 10")
    
def get_top_ten_genres():
    db = get_database()
    cur = db.execute("WITH SeriePerGenere(Genere, Serie) AS \
                            (SELECT Genere, COUNT(*) FROM GENERE_SERIE GROUP BY Genere), \
                        FilmPerGenere(Genere, Film) AS \
                            (SELECT Genere, COUNT(*) FROM GENERE_FILM GROUP BY Genere) \
                        SELECT F.Genere, SUM(COALESCE(Film, 0) + COALESCE(Serie,0)) as tot FROM \
                            (FilmPerGenere AS F LEFT JOIN SeriePerGenere ON F.Genere=SeriePerGenere.Genere) \
                        GROUP BY F.Genere \
                        ORDER BY tot DESC \
                        LIMIT 10")
    return cur.fetchall()
    
def get_top_ten_rated_actors():
    db = get_database()
    cur = db.execute("SELECT NomeArte AS na, AVG(Valutazione) FROM \
                        (SELECT Valutazione FROM \
                            (RECITAZIONE_FILM AS rf JOIN FILM ON rf.CodFilm=FILM.CodFilm")