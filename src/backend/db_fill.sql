INSERT INTO GENERE (Nome)
VALUES 
     ("Giallo"), ("Drammatico"), ("Commedia"), ("Horror"), ("Polizesco"), ("Thriller"), 
     ("Noir"), ("Comico"), ("Fantasy"), ("Fantastico"), ("Fantascienza"), ("Animazione"), 
     ("Demenziale"),  ("Grottesco"),  ("Musicale"),   ("Sentimentale"),  ("Storico"), 
     ("Biografico"), ("Documentario"), ("Western"), ("Spionaggio");

INSERT INTO LINGUA (Denominazione)
VALUES
     ("Italiano"), ("Inglese"), ("Tedesco"), ("Francese"), ("Spagnolo"), ("Giapponese"), ("Coreano");

INSERT INTO UTENTE (CodUtente, Nome, Cognome, Email, `Password`, NumTelefono, PasswordAdmin)
VALUES
     (1, "Giulia", "Boni", "giulia@giulia.it", "12345678", 24167435, "admin");

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

INSERT INTO GENERE_FILM (CodFilm, Genere)
VALUES
     (1, "Horror"),
     (1, "Commedia"),
     (1, "Animazione"),
     (2, "Drammatico"),
     (2, "Biografico"),
     (3, "Horror"),
     (3, "Grottesco"),
     (4, "Horror"),
     (4, "Demenziale"),
     (4, "Commedia"),
     (5, "Horror"),
     (5, "Grottesco");

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

INSERT INTO SERIE (CodSerie, Titolo, TitoloOriginale, Valutazione, AnnoUscita, PaeseProduzione)
VALUES
     (1, "Il Trono di Pane", "Throne of Bread", 30, 2003, "USA"),
     (2, "Pink Mirror - Il Riflesso Rosa", "Pink Mirror", 70, 2016, "UK"),
     (3, "La Casa di Panna", "House", 90, 2020, "UK"),
     (4, "Ricordati di me", "Ricordami di te", 99, 2022, "IT"),
     (5, "Gli Anelli del Podere", "Rings of Power", 12, 2023, "UK");

INSERT INTO GENERE_SERIE (CodSerie, Genere)
VALUES
     (1, "Horror"),
     (1, "Commedia"),
     (1, "Animazione"),
     (2, "Drammatico"),
     (2, "Fantasy"),
     (3, "Horror"),
     (3, "Fantastico"),
     (4, "Horror"),
     (4, "Giallo"),
     (4, "Commedia"),
     (5, "Drammatico"),
     (5, "Grottesco");

INSERT INTO RECITAZIONE_SERIE(CodSerie, CodAttore)
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

INSERT INTO SCAFFALATURA VALUES(1);
INSERT INTO SCAFFALATURA VALUES(2);
INSERT INTO SCAFFALE VALUES(1,1);
INSERT INTO SCAFFALE VALUES(1,2);
INSERT INTO SCAFFALE VALUES(1,3);
INSERT INTO SCAFFALE VALUES(2,1);
INSERT INTO STAGIONE VALUES(1,1,10,40,2002,'Italia');
INSERT INTO STAGIONE VALUES(1,2,10,60,2002,'Italia');
INSERT INTO STAGIONE VALUES(1,3,10,89,2002,'Italia');
INSERT INTO STAGIONE VALUES(2,1,10,89,2002,'Italia');
INSERT INTO STAGIONE VALUES(3,1,10,89,1990,'Italia');
INSERT INTO STAGIONE VALUES(3,2,10,70,1990,'Italia');
INSERT INTO STAGIONE VALUES(4,1,15,99,1990,'Regno Unito');
INSERT INTO STAGIONE VALUES(5,1,9,5,2023,'Regno Unito');
INSERT INTO STAGIONE VALUES(5,2,9,4,2024,'Regno Unito');
INSERT INTO STAGIONE VALUES(5,3,9,3,2024,'Regno Unito');
INSERT INTO UTENTE VALUES(2,'Paolo','Rossi','123','paolo@paolo.it',12345678,NULL);
INSERT INTO UTENTE VALUES(3,'Rosa','Rossa','1234','rosa@rossa.it',12345678,NULL);
INSERT INTO RECITAZIONE_STAGIONE VALUES(1,1,1);
INSERT INTO RECITAZIONE_STAGIONE VALUES(3,1,1);
INSERT INTO RECITAZIONE_STAGIONE VALUES(2,1,1);
INSERT INTO RECITAZIONE_STAGIONE VALUES(1,1,2);
INSERT INTO RECITAZIONE_STAGIONE VALUES(3,1,2);
INSERT INTO RECITAZIONE_STAGIONE VALUES(4,1,2);
INSERT INTO RECITAZIONE_STAGIONE VALUES(3,1,3);
INSERT INTO RECITAZIONE_STAGIONE VALUES(4,1,3);
INSERT INTO RECITAZIONE_STAGIONE VALUES(1,1,3);
INSERT INTO RECITAZIONE_STAGIONE VALUES(3,2,1);
INSERT INTO RECITAZIONE_STAGIONE VALUES(4,2,1);
INSERT INTO RECITAZIONE_STAGIONE VALUES(5,2,1);
INSERT INTO RECITAZIONE_STAGIONE VALUES(4,3,1);
INSERT INTO RECITAZIONE_STAGIONE VALUES(5,3,1);
INSERT INTO RECITAZIONE_STAGIONE VALUES(3,3,1);
INSERT INTO RECITAZIONE_STAGIONE VALUES(4,3,2);
INSERT INTO RECITAZIONE_STAGIONE VALUES(5,3,2);
INSERT INTO RECITAZIONE_STAGIONE VALUES(3,3,2);
INSERT INTO RECITAZIONE_STAGIONE VALUES(4,4,1);
INSERT INTO RECITAZIONE_STAGIONE VALUES(5,4,1);
INSERT INTO RECITAZIONE_STAGIONE VALUES(3,4,1);
INSERT INTO RECITAZIONE_STAGIONE VALUES(4,5,1);
INSERT INTO RECITAZIONE_STAGIONE VALUES(5,5,1);
INSERT INTO RECITAZIONE_STAGIONE VALUES(3,5,1);
INSERT INTO RECITAZIONE_STAGIONE VALUES(4,5,2);
INSERT INTO RECITAZIONE_STAGIONE VALUES(5,5,2);
INSERT INTO RECITAZIONE_STAGIONE VALUES(3,5,2);
INSERT INTO RECITAZIONE_STAGIONE VALUES(4,5,3);
INSERT INTO RECITAZIONE_STAGIONE VALUES(5,5,3);
INSERT INTO RECITAZIONE_STAGIONE VALUES(3,5,3);
INSERT INTO COPIA_ARTICOLO VALUES(1,'DVD',0,1,1,1,NULL,NULL);
INSERT INTO COPIA_ARTICOLO VALUES(2,'DVD',0,2,1,NULL,1,1);
INSERT INTO COPIA_ARTICOLO VALUES(3,'DVD',0,2,1,NULL,1,2);
INSERT INTO COPIA_ARTICOLO VALUES(4,'DVD',0,2,1,NULL,1,3);
INSERT INTO COPIA_ARTICOLO VALUES(5,'VHS',1,2,1,NULL,1,1);
INSERT INTO COPIA_ARTICOLO VALUES(6,'VHS',1,2,1,NULL,1,2);
INSERT INTO COPIA_ARTICOLO VALUES(7,'VHS',1,2,1,NULL,1,3);
INSERT INTO LINGUA_COPIA VALUES('Italiano',1);
INSERT INTO LINGUA_COPIA VALUES('Inglese',1);
INSERT INTO LINGUA_COPIA VALUES('Tedesco',1);
INSERT INTO LINGUA_COPIA VALUES('Italiano',2);
INSERT INTO LINGUA_COPIA VALUES('Inglese',2);
INSERT INTO LINGUA_COPIA VALUES('Tedesco',2);
INSERT INTO LINGUA_COPIA VALUES('Italiano',3);
INSERT INTO LINGUA_COPIA VALUES('Inglese',3);
INSERT INTO LINGUA_COPIA VALUES('Tedesco',3);
INSERT INTO LINGUA_COPIA VALUES('Italiano',4);
INSERT INTO LINGUA_COPIA VALUES('Inglese',4);
INSERT INTO LINGUA_COPIA VALUES('Tedesco',4);
INSERT INTO LINGUA_COPIA VALUES('Italiano',5);
INSERT INTO LINGUA_COPIA VALUES('Inglese',5);
INSERT INTO LINGUA_COPIA VALUES('Tedesco',5);
INSERT INTO LINGUA_COPIA VALUES('Italiano',6);
INSERT INTO LINGUA_COPIA VALUES('Inglese',6);
INSERT INTO LINGUA_COPIA VALUES('Tedesco',6);
INSERT INTO LINGUA_COPIA VALUES('Italiano',7);
INSERT INTO LINGUA_COPIA VALUES('Inglese',7);
INSERT INTO LINGUA_COPIA VALUES('Tedesco',7);
INSERT INTO PRENOTAZIONE VALUES(1,'2024-09-13','2024-09-20',NULL,NULL,2);
INSERT INTO PRENOTAZIONE VALUES(2,'2024-09-13','2024-09-19',NULL,NULL,3);
INSERT INTO RICHIESTA VALUES(1,2);
INSERT INTO RICHIESTA VALUES(1,3);
INSERT INTO RICHIESTA VALUES(1,4);
INSERT INTO RICHIESTA VALUES(2,1);