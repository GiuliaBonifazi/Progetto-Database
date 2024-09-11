INSERT INTO MEMBRO_DEL_CAST (CodMembroCast, NomeArte, DataNascita, DataMorte, Attore, Regista)
VALUES 
     (1, "Tim Burton", '1958/08/25', null, true, true),
     (2, "Johnny Depp", '1963/06/9', null, true, false),
     (3, "Helena Bonham Carter", '1966/05/26', null, true, false),
     (4, "Amy Adams", '1974/08/20', null, true, false),
     (5, "Winona Ryder", '1971/10/29', null, true, false);

INSERT INTO FILM (CodFilm, Durata, Titolo, TitoloOriginale, Valutazione, AnnoUscita, PaeseProduzione, CodRegista)
VALUES 
     (1, 77, "La Sposa Cadavere", "Corpse Bride", 90, 2005, "UK", 1),
     (2, 106, "Big Eyes", "Big Eyes", 78, 2014, "USA", 1),
     (3, 105, "Edward Mani di Forbice", "Edward Scissorhands", 87, 1990, "USA", 1),
     (4, 92, "Beetlejuice - Spiritello porcello", "Beetlejuice", 89, 1988, "USA", 1),
     (5, 116, "Sweeney Todd - Il diabolico barbiere di Fleet Street", "Sweeney Todd - The demon barber of Fleet Street", 78, 2007, "UK", 1);

INSERT INTO RECITAZIONE_FILM (CodFilm, CodAttore)
VALUES
     (1, 2),
     (1, 3),
     (2, 4),
     (3, 1),
     (3, 5),
     (4, 5),
     (5, 2),
     (5, 3);

INSERT INTO SERIE (CodSerie, Titolo, TitoloOriginale, Valutazione, AnnoUscita, PaeseProduzione):
VALUES
     (1, "Il Trono di Pane", "Throne of Bread", 30, 2003, "USA"),
     (2, "Pink Mirror - Il Riflesso Rosa", "Pink Mirror", 70, 2016, "UK"),
     (3, "La Casa di Panna", "House", 90, 2020, "UK"),
     (4, "Ricordati di me", "Ricordami di te", 99, 2022, "IT"),
     (5, "Gli Anelli del Podere", "Rings of Power", 12, 2023, "UK");

INSERT INTO RECITAZIONE_SERIE(CodSerie, CodAttore):
VALUES
     (1, 1),
     (1, 2),
     (1, 3),
     (1, 4),
     (2, 2),
     (2, 3),
     (2, 5),
     (3, 1),
     (3, 4),
     (3, 5),
     (4, 1),
     (4, 3),
     (4, 5),
     (5, 3),
     (5, 4),
     (5, 5);