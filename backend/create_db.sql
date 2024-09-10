-- *********************************************
-- * Standard SQL generation                   
-- *--------------------------------------------
-- * DB-MAIN version: 11.0.2              
-- * Generator date: Sep 14 2021              
-- * Generation date: Tue Sep 10 21:08:56 2024 
-- * LUN file: C:\Users\giuli\Desktop\Uni\Basi di Dati\Progetto Database.lun 
-- * Schema: Logico GIUSTO/SQL1 
-- ********************************************* 


-- Database Section
-- ________________ 

create database videonoleggio;


-- DBSpace Section
-- _______________


-- Tables Section
-- _____________ 

create table COPIA_ARTICOLO (
     CodCopia integer not null auto_increment,
     Supporto text not null,
     Disponibilita boolean not null,
     CodScaffalatura integer not null,
     NumScaffale integer not null,
     CodFilm integer,
     CodSerie integer,
     CodSerieStagione integer,
     NumStagione integer,
     constraint ID_COPIA_ARTICOLO_ID primary key (CodCopia));

create table EPISODIO (
     CodSerie integer not null,
     NumStagione integer not null,
     Titolo text not null,
     NumEpisodio integer not null,
     AnnoUscita integer not null,
     Durata integer not null,
     constraint ID_EPISODIO_ID primary key (CodSerie, NumStagione, NumEpisodio));

create table FILM (
     Durata integer not null,
     CodFilm integer not null,
     Titolo text not null,
     TitoloOriginale text not null,
     Valutazione integer not null,
     Locandina longblob not null,
     AnnoUscita integer not null,
     PaeseProduzione text not null,
     CodRegista integer not null,
     constraint ID_FILM_ID primary key (CodFilm));

create table MEMBRO_DEL_CAST (
     CodMembroCast integer not null,
     NomeArte text not null,
     DataNascita date not null,
     DataMorte date,
     Attore char not null,
     Regista char not null,
     constraint ID_MEMBRO_DEL_CAST_ID primary key (CodMembroCast));

create table LINGUA (
     Denominazione text not null,
     constraint ID_LINGUA_ID primary key (Denominazione));

create table GENERE (
     Nome text not null,
     constraint ID_GENERE_ID primary key (Nome));

create table PRENOTAZIONE (
     CodPrenotazione integer not null,
     DataConferma date not null,
     DataRitiro date not null,
     RitiroEffettuato boolean,
     CodUtente integer not null,
     constraint ID_PRENOTAZIONE_ID primary key (CodPrenotazione));

create table genere_film (
     Genere text not null,
     CodFilm integer not null,
     constraint ID_genere_film_ID primary key (Genere, CodFilm));

create table lingua_copia (
     Lingua text not null,
     CodCopia integer not null,
     constraint ID_lingua_copia_ID primary key (Lingua, CodCopia));

create table genere_serie (
     CodSerie integer not null,
     Genere text not null,
     constraint ID_genere_serie_ID primary key (Genere, CodSerie));

create table recitazione_film (
     CodFilm integer not null,
     CodAttore integer not null,
     constraint ID_recitazione_film_ID primary key (CodFilm, CodAttore));

create table recitazione_serie (
     CodSerie integer not null,
     CodAttore integer not null,
     constraint ID_recitazione_serie_ID primary key (CodSerie, CodAttore));

create table recitazione_stagione (
     CodAttore integer not null,
     CodSerie integer not null,
     NumStagione integer not null,
     constraint ID_recitazione_stagione_ID primary key (CodSerie, NumStagione, CodAttore));

create table richiesta (
     CodPrenotazione integer not null,
     CodCopia integer not null,
     constraint ID_richiesta_ID primary key (CodPrenotazione, CodCopia));

create table SCAFFALATURA (
     CodScaffalatura integer not null auto_increment,
     constraint ID_SCAFFALATURA_ID primary key (CodScaffalatura));

create table SCAFFALE (
     CodScaffalatura integer not null,
     NumScaffale integer not null,
     constraint ID_SCAFFALE_ID primary key (CodScaffalatura, NumScaffale));

create table SERIE (
     CodSerie integer not null auto_increment,
     Titolo text not null,
     TitoloOriginale text not null,
     Valutazione integer not null,
     Locandina varchar(1) not null,
     AnnoUscita integer not null,
     PaeseProduzione text not null,
     constraint ID_SERIE_ID primary key (CodSerie));

create table STAGIONE (
     CodSerie integer not null,
     NumStagione integer not null,
     NumeroEpisodi integer not null,
     Titolo text not null,
     TitoloOriginale text not null,
     Valutazione integer not null,
     Locandina varchar(1) not null,
     AnnoUscita integer not null,
     PaeseProduzione text not null,
     constraint ID_STAGIONE_ID primary key (CodSerie, NumStagione));

create table UTENTE (
     CodUtente integer not null auto_increment,
     Nome text not null,
     Cognome text not null,
     Password text not null,
     Email text not null,
     NumTelefono integer not null,
     PasswordAdmin text,
     constraint ID_UTENTE_ID primary key (CodUtente));


-- Constraints Section
-- ___________________ 

alter table COPIA_ARTICOLO add constraint ID_COPIA_ARTICOLO_CHK
     check(exists(select * from lingua_copia
                  where lingua_copia.CodCopia = CodCopia)); 

alter table COPIA_ARTICOLO add constraint REF_COPIA_SCAFF_FK
     foreign key (CodScaffalatura, NumScaffale)
     references SCAFFALE;

alter table COPIA_ARTICOLO add constraint EQU_COPIA_FILM_FK
     foreign key (CodFilm)
     references FILM;

alter table COPIA_ARTICOLO add constraint EQU_COPIA_SERIE_FK
     foreign key (CodSerie)
     references SERIE;

alter table COPIA_ARTICOLO add constraint EQU_COPIA_STAGI_FK
     foreign key (CodSerieStagione, NumStagione)
     references STAGIONE;

alter table COPIA_ARTICOLO add constraint EQU_COPIA_STAGI_CHK
     check((CodSerieStagione is not null and NumStagione is not null)
           or (CodSerieStagione is null and NumStagione is null)); 

alter table EPISODIO add constraint EQU_EPISO_STAGI
     foreign key (CodSerie, NumStagione)
     references STAGIONE;

alter table FILM add constraint ID_FILM_CHK
     check(exists(select * from genere_film
                  where genere_film.CodFilm = CodFilm)); 

alter table FILM add constraint ID_FILM_CHK
     check(exists(select * from recitazione_film
                  where recitazione_film.CodFilm = CodFilm)); 

alter table FILM add constraint ID_FILM_CHK
     check(exists(select * from COPIA_ARTICOLO
                  where COPIA_ARTICOLO.CodFilm = CodFilm)); 

alter table FILM add constraint REF_FILM_MEMBR_FK
     foreign key (CodRegista)
     references MEMBRO_DEL_CAST;

alter table PRENOTAZIONE add constraint ID_PRENOTAZIONE_CHK
     check(exists(select * from richiesta
                  where richiesta.CodPrenotazione = CodPrenotazione)); 

alter table PRENOTAZIONE add constraint REF_PRENO_UTENT_FK
     foreign key (CodUtente)
     references UTENTE;

alter table genere_film add constraint EQU_gener_FILM_FK
     foreign key (CodFilm)
     references FILM;

alter table genere_film add constraint REF_gener_GENER_1
     foreign key (Genere)
     references GENERE;

alter table lingua_copia add constraint EQU_lingu_COPIA_FK
     foreign key (CodCopia)
     references COPIA_ARTICOLO;

alter table lingua_copia add constraint REF_lingu_LINGU
     foreign key (Lingua)
     references LINGUA;

alter table genere_serie add constraint REF_gener_GENER
     foreign key (Genere)
     references GENERE;

alter table genere_serie add constraint EQU_gener_SERIE_FK
     foreign key (CodSerie)
     references SERIE;

alter table recitazione_film add constraint REF_recit_MEMBR_2_FK
     foreign key (CodAttore)
     references MEMBRO_DEL_CAST;

alter table recitazione_film add constraint EQU_recit_FILM
     foreign key (CodFilm)
     references FILM;

alter table recitazione_serie add constraint REF_recit_MEMBR_1_FK
     foreign key (CodAttore)
     references MEMBRO_DEL_CAST;

alter table recitazione_serie add constraint EQU_recit_SERIE
     foreign key (CodSerie)
     references SERIE;

alter table recitazione_stagione add constraint EQU_recit_STAGI
     foreign key (CodSerie, NumStagione)
     references STAGIONE;

alter table recitazione_stagione add constraint REF_recit_MEMBR_FK
     foreign key (CodAttore)
     references MEMBRO_DEL_CAST;

alter table richiesta add constraint REF_richi_COPIA_FK
     foreign key (CodCopia)
     references COPIA_ARTICOLO;

alter table richiesta add constraint EQU_richi_PRENO
     foreign key (CodPrenotazione)
     references PRENOTAZIONE;

alter table SCAFFALATURA add constraint ID_SCAFFALATURA_CHK
     check(exists(select * from SCAFFALE
                  where SCAFFALE.CodScaffalatura = CodScaffalatura)); 

alter table SCAFFALE add constraint EQU_SCAFF_SCAFF
     foreign key (CodScaffalatura)
     references SCAFFALATURA;

alter table SERIE add constraint ID_SERIE_CHK
     check(exists(select * from genere_serie
                  where genere_serie.CodSerie = CodSerie)); 

alter table SERIE add constraint ID_SERIE_CHK
     check(exists(select * from recitazione_serie
                  where recitazione_serie.CodSerie = CodSerie)); 

alter table SERIE add constraint ID_SERIE_CHK
     check(exists(select * from COPIA_ARTICOLO
                  where COPIA_ARTICOLO.CodSerie = CodSerie)); 

alter table SERIE add constraint ID_SERIE_CHK
     check(exists(select * from STAGIONE
                  where STAGIONE.CodSerie = CodSerie)); 

alter table STAGIONE add constraint ID_STAGIONE_CHK
     check(exists(select * from recitazione_stagione
                  where recitazione_stagione.CodSerie = CodSerie and recitazione_stagione.NumStagione = NumStagione)); 

alter table STAGIONE add constraint ID_STAGIONE_CHK
     check(exists(select * from COPIA_ARTICOLO
                  where COPIA_ARTICOLO.CodSerieStagione = CodSerie and COPIA_ARTICOLO.NumStagione = NumStagione)); 

alter table STAGIONE add constraint ID_STAGIONE_CHK
     check(exists(select * from EPISODIO
                  where EPISODIO.CodSerie = CodSerie and EPISODIO.NumStagione = NumStagione)); 

alter table STAGIONE add constraint EQU_STAGI_SERIE
     foreign key (CodSerie)
     references SERIE;


-- Index Section
-- _____________ 

create unique index ID_COPIA_ARTICOLO_IND
     on COPIA_ARTICOLO (CodCopia);

create index REF_COPIA_SCAFF_IND
     on COPIA_ARTICOLO (CodScaffalatura, NumScaffale);

create index EQU_COPIA_FILM_IND
     on COPIA_ARTICOLO (CodFilm);

create index EQU_COPIA_SERIE_IND
     on COPIA_ARTICOLO (CodSerie);

create index EQU_COPIA_STAGI_IND
     on COPIA_ARTICOLO (CodSerieStagione, NumStagione);

create unique index ID_EPISODIO_IND
     on EPISODIO (CodSerie, NumStagione, NumEpisodio);

create unique index ID_FILM_IND
     on FILM (CodFilm);

create index REF_FILM_MEMBR_IND
     on FILM (CodRegista);

create unique index ID_MEMBRO_DEL_CAST_IND
     on MEMBRO_DEL_CAST (CodMembroCast);

create unique index ID_LINGUA_IND
     on LINGUA (Denominazione);

create unique index ID_GENERE_IND
     on GENERE (Nome);

create unique index ID_PRENOTAZIONE_IND
     on PRENOTAZIONE (CodPrenotazione);

create index REF_PRENO_UTENT_IND
     on PRENOTAZIONE (CodUtente);

create unique index ID_genere_film_IND
     on genere_film (Genere, CodFilm);

create index EQU_gener_FILM_IND
     on genere_film (CodFilm);

create unique index ID_lingua_copia_IND
     on lingua_copia (Lingua, CodCopia);

create index EQU_lingu_COPIA_IND
     on lingua_copia (CodCopia);

create unique index ID_genere_serie_IND
     on genere_serie (Genere, CodSerie);

create index EQU_gener_SERIE_IND
     on genere_serie (CodSerie);

create unique index ID_recitazione_film_IND
     on recitazione_film (CodFilm, CodAttore);

create index REF_recit_MEMBR_2_IND
     on recitazione_film (CodAttore);

create unique index ID_recitazione_serie_IND
     on recitazione_serie (CodSerie, CodAttore);

create index REF_recit_MEMBR_1_IND
     on recitazione_serie (CodAttore);

create unique index ID_recitazione_stagione_IND
     on recitazione_stagione (CodSerie, NumStagione, CodAttore);

create index REF_recit_MEMBR_IND
     on recitazione_stagione (CodAttore);

create unique index ID_richiesta_IND
     on richiesta (CodPrenotazione, CodCopia);

create index REF_richi_COPIA_IND
     on richiesta (CodCopia);

create unique index ID_SCAFFALATURA_IND
     on SCAFFALATURA (CodScaffalatura);

create unique index ID_SCAFFALE_IND
     on SCAFFALE (CodScaffalatura, NumScaffale);

create unique index ID_SERIE_IND
     on SERIE (CodSerie);

create unique index ID_STAGIONE_IND
     on STAGIONE (CodSerie, NumStagione);

create unique index ID_UTENTE_IND
     on UTENTE (CodUtente);

