CREATE TABLE if not exists COPIA_ARTICOLO (
    CodCopia INTEGER PRIMARY KEY,
    Supporto TEXT NOT NULL,
    Disponibilita BOOLEAN NOT NULL,
    CodScaffalatura INTEGER NOT NULL,
    NumScaffale INTEGER NOT NULL,
    CodFilm INTEGER,
    CodSerie INTEGER,
    NumStagione INTEGER,
    FOREIGN KEY (CodScaffalatura, NumScaffale) REFERENCES SCAFFALE (CodScaffalatura, NumScaffale),
    FOREIGN KEY (CodFilm) REFERENCES FILM (CodFilm),
    FOREIGN KEY (CodSerie, NumStagione) REFERENCES STAGIONE (CodSerie, NumStagione),
    CHECK ((CodSerie IS NOT NULL AND NumStagione IS NOT NULL) OR (CodSerie IS NULL AND NumStagione IS NULL))
);

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

CREATE TABLE if not exists MEMBRO_DEL_CAST (
    CodMembroCast INTEGER PRIMARY KEY,
    NomeArte TEXT NOT NULL,
    DataNascita DATE NOT NULL,
    DataMorte DATE,
    Attore BOOLEAN NOT NULL,
    Regista BOOLEAN NOT NULL
);

CREATE TABLE if not exists LINGUA (
    Denominazione TEXT PRIMARY KEY
);

CREATE TABLE if not exists GENERE (
    Nome TEXT PRIMARY KEY
);

CREATE TABLE if not exists PRENOTAZIONE (
    CodPrenotazione INTEGER PRIMARY KEY,
    DataConferma DATE NOT NULL,
    DataRitiro DATE NOT NULL,
    RitiroEffettuato BOOLEAN,
    ConsegnaEffettuata BOOLEAN,
    CodUtente INTEGER NOT NULL,
    FOREIGN KEY (CodUtente) REFERENCES UTENTE (CodUtente)
);

CREATE TABLE if not exists GENERE_FILM (
    Genere TEXT NOT NULL,
    CodFilm INTEGER NOT NULL,
    PRIMARY KEY (Genere, CodFilm),
    FOREIGN KEY (Genere) REFERENCES GENERE (Nome),
    FOREIGN KEY (CodFilm) REFERENCES FILM (CodFilm)
);

CREATE TABLE if not exists LINGUA_COPIA (
    Lingua TEXT NOT NULL,
    CodCopia INTEGER NOT NULL,
    PRIMARY KEY (Lingua, CodCopia),
    FOREIGN KEY (Lingua) REFERENCES LINGUA (Denominazione),
    FOREIGN KEY (CodCopia) REFERENCES COPIA_ARTICOLO (CodCopia)
);

CREATE TABLE if not exists GENERE_SERIE (
    CodSerie INTEGER NOT NULL,
    Genere TEXT NOT NULL,
    PRIMARY KEY (Genere, CodSerie),
    FOREIGN KEY (Genere) REFERENCES GENERE (Nome),
    FOREIGN KEY (CodSerie) REFERENCES SERIE (CodSerie)
);

CREATE TABLE if not exists RECITAZIONE_FILM (
    CodFilm INTEGER NOT NULL,
    CodAttore INTEGER NOT NULL,
    PRIMARY KEY (CodFilm, CodAttore),
    FOREIGN KEY (CodFilm) REFERENCES FILM (CodFilm),
    FOREIGN KEY (CodAttore) REFERENCES MEMBRO_DEL_CAST (CodMembroCast)
);

CREATE TABLE if not exists RECITAZIONE_SERIE (
    CodSerie INTEGER NOT NULL,
    CodAttore INTEGER NOT NULL,
    PRIMARY KEY (CodSerie, CodAttore),
    FOREIGN KEY (CodSerie) REFERENCES SERIE (CodSerie),
    FOREIGN KEY (CodAttore) REFERENCES MEMBRO_DEL_CAST (CodMembroCast)
);

CREATE TABLE if not exists RECITAZIONE_STAGIONE (
    CodAttore INTEGER NOT NULL,
    CodSerie INTEGER NOT NULL,
    NumStagione INTEGER NOT NULL,
    PRIMARY KEY (CodSerie, NumStagione, CodAttore),
    FOREIGN KEY (CodSerie, NumStagione) REFERENCES STAGIONE (CodSerie, NumStagione),
    FOREIGN KEY (CodAttore) REFERENCES MEMBRO_DEL_CAST (CodMembroCast)
);

CREATE TABLE if not exists RICHIESTA (
    CodPrenotazione INTEGER NOT NULL,
    CodCopia INTEGER NOT NULL,
    PRIMARY KEY (CodPrenotazione, CodCopia),
    FOREIGN KEY (CodPrenotazione) REFERENCES PRENOTAZIONE (CodPrenotazione),
    FOREIGN KEY (CodCopia) REFERENCES COPIA_ARTICOLO (CodCopia)
);

CREATE TABLE if not exists SCAFFALATURA (
    CodScaffalatura INTEGER PRIMARY KEY
);

CREATE TABLE if not exists SCAFFALE (
    CodScaffalatura INTEGER NOT NULL,
    NumScaffale INTEGER NOT NULL,
    PRIMARY KEY (CodScaffalatura, NumScaffale),
    FOREIGN KEY (CodScaffalatura) REFERENCES SCAFFALATURA (CodScaffalatura)
);

CREATE TABLE if not exists SERIE (
    CodSerie INTEGER PRIMARY KEY,
    Titolo TEXT NOT NULL,
    TitoloOriginale TEXT NOT NULL,
    Valutazione INTEGER NOT NULL,
    AnnoUscita INTEGER NOT NULL,
    PaeseProduzione TEXT NOT NULL
);

CREATE TABLE if not exists STAGIONE (
    CodSerie INTEGER NOT NULL,
    NumStagione INTEGER NOT NULL,
    NumeroEpisodi INTEGER NOT NULL,
    Valutazione INTEGER NOT NULL,
    AnnoUscita INTEGER NOT NULL,
    PaeseProduzione TEXT NOT NULL,
    PRIMARY KEY (CodSerie, NumStagione),
    FOREIGN KEY (CodSerie) REFERENCES SERIE (CodSerie)
);

CREATE TABLE if not exists UTENTE (
    CodUtente INTEGER PRIMARY KEY,
    Nome TEXT NOT NULL,
    Cognome TEXT NOT NULL,
    Password TEXT NOT NULL,
    Email TEXT NOT NULL,
    NumTelefono INTEGER NOT NULL,
    PasswordAdmin TEXT
);