# Progetto-Database
Progetto per corso Basi di Dati di Ingegneria e Scienze Informatiche a Cesena

Per utilizzare:

# 1 - Creare virtual environment di python

aprire il terminale e dalla cartella del progetto digitare:

python -m venv .venv

aspettare che venga ultimata la creazione e digitare:

source .venv/Scripts/Activate

# 2 - Scaricare i requirements

pip install -r requirements.txt

# 3 - Inizializzare il database

python src/initialize.py

# 4 - avviare l'applicazione

python src/main.py