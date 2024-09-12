from nicegui import ui
from template import directors_as_dict, actors_as_dict, notify_empty_field, series_as_dict, notify_added
from backend import add_movie, add_series, add_season, add_cast, add_shelf, add_shelving, add_genre, add_language

selected_actors = []

@ui.page("/add_to_archive_page")
def add_to_archive_page():
    with ui.tabs().classes('w-full') as tabs:
        film = ui.tab('Film')
        series = ui.tab('Serie')
        season = ui.tab('Stagione')
        member = ui.tab('Cast')
        copy = ui.tab('Copia')
        zone = ui.tab('Zona')
        other = ui.tab("Altro")
    with ui.tab_panels(tabs, value=film).classes('w-full'):
        #FILM --------------------------
        with ui.tab_panel(film).classes("items-center"):
            with ui.grid(columns=2).classes('w-full items-center'):
                title = ui.input(label="Titolo")
                ogTitle = ui.input(label="Titolo originale")
                runtime = ui.input(label="Durata")
                mark = ui.input(label="Valutazione")
                year = ui.input(label="Anno d'uscita")
                country = ui.input(label="Paese di produzione")
                with ui.row():
                    ui.label("Seleziona regista: ")
                    director = ui.select(directors_as_dict(), label="Regista")
                with ui.row():
                    actor_select()
                ui.button(text="Aggiungi", on_click=lambda: add_movie_check(title.value, ogTitle.value, runtime.value, mark.value, 
                                                                            year.value, country.value, director.value))
        #SERIE -------------------------
        with ui.tab_panel(series).classes("items-center"):
            with ui.grid(columns=2).classes('w-full items-center'):
                title_ser = ui.input(label="Titolo")
                ogTitle_ser = ui.input(label="Titolo originale")
                mark_ser = ui.input(label="Valutazione")
                year_ser = ui.input(label="Anno d'uscita")
                country_ser = ui.input(label="Paese di produzione")
                actor_select()
            ui.button(text="Aggiungi", on_click=lambda: add_series_check(title_ser.value, ogTitle_ser.value, 
                                                                         mark_ser.value, year_ser.value, country_ser.value))
        #STAGIONE ----------------------
        with ui.tab_panel(season):
            with ui.grid(columns=2).classes('w-full items-center'):
                with ui.row():
                    ui.label("Seleziona serie:")
                    codSeason = ui.select(series_as_dict(), label="Serie")
                numSeason = ui.input(label="Numero stagione")
                mark_sea = ui.input(label="Valutazione")
                year_sea = ui.input(label="Anno d'uscita")
                country_sea = ui.input(label="Paese di produzione")
                actor_select()
            ui.button(text="Aggiungi", on_click=lambda: add_season_check(codSeason.value, numSeason.value, mark_sea.value,
                                                                 year_sea.value, country_sea.value))
        #MEMBRO DEL CAST ----------------------
        with ui.tab_panel(member):
            with ui.column().classes("w-full items-center"):
                name = ui.input(label="Nome d'arte *")
                with ui.row():
                    ui.label("Data di nascita *")
                    birth = ui.date()
                with ui.row():
                    ui.label("Data di morte")
                    death = ui.date()
                isActor = ui.checkbox(text="Attore *")
                isDirector = ui.checkbox(text="Regista *")
                ui.button("Aggiungi", on_click=lambda: add_member_check(name.value, birth.value, death.value, isActor.value, isDirector.value))
        #COPIA -------------------------------
        with ui.tab_panel(copy):
            ui.label('Second tab')
        #ZONA -----------------------------
        with ui.tab_panel(zone).classes("w-full items-center"):
            with ui.card().classes("border"):
                shelving = ui.input(label="Scaffalatura")
                ui.button("Aggiungi", on_click=lambda: add_shelving_check(shelving.value))
            with ui.card().classes("border"):
                shelfShelving = ui.input(label="Scaffalatura")
                shelf = ui.input(label="Scaffale")
                ui.button("Aggiungi", on_click=lambda: add_shelf_check(shelf.value, shelfShelving.value))
        #ALTRO
        with ui.tab_panel(other).classes("w-full items-center"):
            with ui.card().classes("border"):
                genre = ui.input(label="Genere")
                ui.button("Aggiungi", on_click=lambda: add_genre_check(genre.value))
            with ui.card().classes("border"):
                language = ui.input(label="Lingua")
                ui.button("Aggiungi", on_click=lambda: add_language_check(language.value))

def actor_select():
    with ui.row():
        ui.label("Seleziona attori: ")
        ui.select(actors_as_dict(), label="Attori", multiple=True, on_change=update_selected_actors).props("use-chips")

def update_selected_actors(event):
    global selected_actors
    selected_actors = event.value
    return

def add_genre_check(genre: str):
    if not genre:
        notify_empty_field("Genere")
        return
    mess, success = add_genre(genre)
    if success:
        notify_added("genere")
    else:
        ui.notify(mess, type="negative")
    
def add_language_check(lang: str):
    if not lang:
        notify_empty_field("Lingua")
        return
    mess, success = add_language(lang)
    if success:
        notify_added("lingua")
    else:
        ui.notify(mess, type="negative")

def add_movie_check(title: str, ogTitle: str, runtime: int, mark: int, year: int, country: str, director: int):
    global selected_actors
    if not title:
        notify_empty_field("Titolo")
        return
    if not ogTitle:
        notify_empty_field("Titolo originale")
        return
    if not runtime:
        notify_empty_field("Durata")
        return
    if not mark:
        notify_empty_field("Valutazione")
        return
    if not year:
        notify_empty_field("Anno d'uscita")
        return
    if not country:
        notify_empty_field("Paese di produzione")
        return
    if not director:
        notify_empty_field("Regista")
        return
    if len(selected_actors) < 3:
        ui.notify("Inserisci almeno 3 attori", type="warning")
        return
    add_movie(title, ogTitle, runtime, mark, year, country, director, selected_actors)
    notify_added("film")

def add_series_check(title: str, ogTitle: str, mark: int, year: int, country: str):
    if not title:
        notify_empty_field("Titolo")
        return
    if not ogTitle:
        notify_empty_field("Titolo originale")
        return
    if not mark:
        notify_empty_field("Valutazione")
        return
    if not year:
        notify_empty_field("Anno d'uscita")
        return
    if not country:
        notify_empty_field("Paese di produzione")
        return
    if len(selected_actors) < 3:
        ui.notify("Inserisci almeno 3 attori", type="warning")
        return
    add_series(title, ogTitle, mark, year, country, selected_actors)
    notify_added("serie")

def add_season_check(seriesId: int, numSeason: int, mark: int, year: int, country: str):
    if not seriesId:
        notify_empty_field("Serie")
        return
    if not numSeason:
        notify_empty_field("Numero Stagione")
        return
    if not mark:
        notify_empty_field("Valutazione")
        return
    if not year:
        notify_empty_field("Anno d'uscita")
        return
    if not country:
        notify_empty_field("Paese di produzione")
        return
    if len(selected_actors) < 3:
        ui.notify("Inserisci almeno 3 attori", type="warning")
        return
    add_season(seriesId, numSeason, 0, mark, year, country, selected_actors)
    notify_added("stagione")
    
def add_member_check(name: str, birth: str, death: str, actor: bool, director: bool):
    if not name:
        notify_empty_field("Nome d'arte")
        return
    if not birth:
        notify_empty_field("Data di nascita")
        return
    add_cast(name, birth, death, actor, director)
    notify_added("membro del cast")

def add_shelf_check(shelf: int, shelving: int):
    if not shelving:
        notify_empty_field("Scaffalatura")
        return
    if not shelf:
        notify_empty_field("Scaffalte")
        return
    mess, success = add_shelf(shelf, shelving)
    if success:
        notify_added("scaffale")
    else:
        ui.notify(mess, type="negative")
    
def add_shelving_check(shelving: int):
    if not shelving:
        notify_empty_field("Scaffalatura")
        return
    mess, success = add_shelving(shelving)
    if success:
        notify_added("scaffalatura")
    else:
        ui.notify(mess, type="negative")