from .database import execute


def create():
    execute(
        """
        CREATE TABLE if not exists MEMBRO_DEL_CAST (
            CodMembroCast INTEGER PRIMARY KEY,
            NomeArte TEXT NOT NULL,
            DataNascita DATE NOT NULL,
            DataMorte DATE,
            Attore BOOLEAN NOT NULL,
            Regista BOOLEAN NOT NULL
        );
        """
    )
    execute(
        """
        CREATE TABLE if not exists FILM (
        CodFilm INTEGER PRIMARY KEY,
        Durata INTEGER NOT NULL,
        Titolo TEXT NOT NULL,
        TitoloOriginale TEXT NOT NULL,
        Valutazione INTEGER NOT NULL,
        AnnoUscita INTEGER NOT NULL,
        PaeseProduzione TEXT NOT NULL,
        CodRegista INTEGER NOT NULL,
        FOREIGN KEY (CodRegista) REFERENCES MEMBRO_DEL_CAST (CodMembroCast)
        );
        """
    )
