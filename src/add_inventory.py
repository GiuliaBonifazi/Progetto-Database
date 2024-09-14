from nicegui import ui
from template import directors_as_dict, actors_as_dict, notify_empty_field, series_as_dict, notify_added, \
                    movies_as_dict, users_as_dict
from backend import add_movie, add_series, add_season, add_cast, add_shelf, add_shelving, add_genre, \
                    add_language, add_copy, get_languages, get_genres, add_admin, remove_admin

selected_actors = []
selected_genres = []
selected_languages = []

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
        admin = ui.tab("Admin")
    with ui.tab_panels(tabs, value=film).classes('w-full'):
        #FILM --------------------------
        with ui.tab_panel(film).classes("items-center"):
            with ui.grid(columns=2).classes('w-full items-center'):
                title = ui.input(label="Titolo")
                ogTitle = ui.input(label="Titolo originale")
                runtime = ui.input(label="Durata", validation={"Not a number" : lambda value: value.isnumeric()})
                mark = ui.input(label="Valutazione", validation={"Not a number" : lambda value: value.isnumeric()})
                year = ui.input(label="Anno d'uscita", validation={"Not a number" : lambda value: value.isnumeric()})
                country = ui.input(label="Paese di produzione")
                genre_select()
                with ui.row():
                    ui.label("Seleziona regista: ")
                    director = ui.select(directors_as_dict(), label="Regista")
                    actor_select()
                ui.button(text="Aggiungi", on_click=lambda: add_movie_check(title.value, ogTitle.value, runtime.value, mark.value, 
                                                                        year.value, country.value, director.value))
                ui.button("Refresh", on_click=lambda: ui.navigate.reload())
        #SERIE -------------------------
        with ui.tab_panel(series).classes("items-center"):
            with ui.grid(columns=2).classes('w-full items-center'):
                title_ser = ui.input(label="Titolo")
                ogTitle_ser = ui.input(label="Titolo originale")
                mark_ser = ui.input(label="Valutazione", validation={"Not a number" : lambda value: value.isnumeric()})
                year_ser = ui.input(label="Anno d'uscita", validation={"Not a number" : lambda value: value.isnumeric()})
                country_ser = ui.input(label="Paese di produzione")
                genre_select()
                actor_select()
            ui.button(text="Aggiungi", on_click=lambda: add_series_check(title_ser.value, ogTitle_ser.value, 
                                                                         mark_ser.value, year_ser.value, country_ser.value))
            ui.button("Refresh", on_click=lambda: ui.navigate.reload())
        #STAGIONE ----------------------
        with ui.tab_panel(season):
            with ui.grid(columns=2).classes('w-full items-center'):
                with ui.row():
                    ui.label("Seleziona serie:")
                    codSeason = ui.select(series_as_dict(), label="Serie")
                numSeason = ui.input(label="Numero stagione", validation={"Not a number" : lambda value: value.isnumeric()})
                numEp = ui.input(label="Numero episodi", validation={"Not a number" : lambda value: value.isnumeric()})
                mark_sea = ui.input(label="Valutazione", validation={"Not a number" : lambda value: value.isnumeric()})
                year_sea = ui.input(label="Anno d'uscita", validation={"Not a number" : lambda value: value.isnumeric()})
                country_sea = ui.input(label="Paese di produzione")
                actor_select()
            ui.button(text="Aggiungi", on_click=lambda: add_season_check(codSeason.value, numSeason.value, mark_sea.value,
                                                                 year_sea.value, country_sea.value, numEp.value))
            ui.button("Refresh", on_click=lambda: ui.navigate.reload())
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
                ui.button("Refresh", on_click=lambda: ui.navigate.reload())
        #COPIA -------------------------------
        with ui.tab_panel(copy).classes("w-full items-center"):
            with ui.column().classes("w-full items-center"):
                with ui.card():
                    ui.label("Scegli un film, una stagione o una serie").style("font-weight: bold;")
                    with ui.row():
                        ui.label("Serie e stagione")
                        copySeries = ui.select(series_as_dict(), label="Serie", clearable=True)
                        copySeason = ui.input("Stagione", validation={"Not a number" : lambda value: value.isnumeric()})
                    with ui.row():
                        ui.label("Film")
                        copyFilm = ui.select(movies_as_dict(), label="Film", clearable=True)
                support = ui.select(label="Supporto", options=["DVD", "Blu-Ray", "VHS"], value="DVD")
                with ui.card():
                    copyShelving = ui.input(label="Scaffalatura", validation={"Not a number" : lambda value: value.isnumeric()})
                    copyShelf = ui.input(label="Scaffale", validation={"Not a number" : lambda value: value.isnumeric()})
                with ui.row():
                    ui.label("Seleziona lingue: ")
                    ui.select([x[0] for x in get_languages()], label="Lingue", multiple=True, on_change=update_selected_languages, clearable=True).props("use-chips")
                ui.button("Aggiungi", on_click=lambda: add_copy_check(copyFilm.value, copySeries.value, copySeason.value, support.value, 
                                                                      copyShelf.value, copyShelving.value))
                ui.button("Refresh", on_click=lambda: ui.navigate.reload())
        #ZONA -----------------------------
        with ui.tab_panel(zone).classes("w-full items-center"):
            with ui.card().classes("border"):
                shelving = ui.input(label="Scaffalatura", validation={"Not a number" : lambda value: value.isnumeric()})
                ui.button("Aggiungi", on_click=lambda: add_shelving_check(shelving.value))
            with ui.card().classes("border"):
                shelfShelving = ui.input(label="Scaffalatura", validation={"Not a number" : lambda value: value.isnumeric()})
                shelf = ui.input(label="Scaffale", validation={"Not a number" : lambda value: value.isnumeric()})
                ui.button("Aggiungi", on_click=lambda: add_shelf_check(shelf.value, shelfShelving.value))
            ui.button("Refresh", on_click=lambda: ui.navigate.reload())
        #ALTRO ----------------------------
        with ui.tab_panel(other).classes("w-full items-center"):
            with ui.card().classes("border"):
                genre = ui.input(label="Genere")
                ui.button("Aggiungi", on_click=lambda: add_genre_check(genre.value))
            with ui.card().classes("border"):
                language = ui.input(label="Lingua")
                ui.button("Aggiungi", on_click=lambda: add_language_check(language.value))
            ui.button("Refresh", on_click=lambda: ui.navigate.reload())
        # ADMIN -------------------
        with ui.tab_panel(admin).classes("w-full items-center"):
            with ui.card().classes("border"):
                ui.label("Aggiungi admin")
                pw = ui.input(label="Password")
                adminToAdd = ui.select(users_as_dict(), with_input=True)
                ui.button("Conferma", on_click=lambda: admin_add(pw.value, adminToAdd.value))
            with ui.card().classes("border"):
                ui.label("Rimuovi Admin")
                remAdmin = ui.select(users_as_dict(), with_input=True)
                ui.button("Conferma", on_click=lambda: admin_delete(remAdmin.value))

def admin_add(pw, id):
    if not pw:
        notify_empty_field("Password Admin")
        return
    if not id:
        notify_empty_field("Utente")
        return
    add_admin(id, pw)
    notify_added("Admin")
    
def admin_delete(id):
    if not id:
        notify_empty_field("Utente")
        return
    remove_admin(id)
    ui.notify("Admin rimosso con successo!")

def actor_select():
    with ui.row(): 
        ui.label("Seleziona attori: ")
        ui.select(actors_as_dict(), label="Attori", multiple=True, on_change=update_selected_actors, clearable=True).props("use-chips")

def genre_select():
    with ui.row():
        ui.label("Seleziona genere/i ")
        ui.select(get_genres(), label="Generi", multiple=True, on_change=update_selected_genres, clearable=True).props("use-chips")

def update_selected_actors(event):
    global selected_actors
    selected_actors = event.value
    return

def update_selected_genres(event):
    global selected_genres
    selected_genres = event.value
    return

def update_selected_languages(event):
    global selected_languages
    selected_languages = event.value
    return

def add_copy_check(movie: int, series: int, season: int, support: str, shelf: int, shelving: int):
    global selected_languages
    if not shelf:
        notify_empty_field("Scaffale")
        return
    elif not shelving:
        notify_empty_field("Scaffalatura")
        return
    elif len(selected_languages) <= 0:
        notify_empty_field("Lingue")
        return
    elif not movie:
        if not series:
            if not season:
                ui.notify("Devi scegliere uno e un solo articolo", type="info")
                return
            else:
                ui.notify("Seleziona la serie da cui proviene la stagione", type="info")
                return
        else:
            if not season:
                mess, success = add_copy(movie, series, season, support, shelf, shelving, "SERIES", selected_languages)
                if success:
                    notify_added("copia di serie")
                else:
                    ui.notify(mess, type="negative")
            else:
                mess, success = add_copy(movie, series, season, support, shelf, shelving, "SEASON", selected_languages)
                if success:
                    notify_added("copia di stagione")
                else:
                    ui.notify(mess, type="negative")
    elif not series:
        if not season:
            mess, success = add_copy(movie, series, season, support, shelf, shelving, "MOVIE", selected_languages)
            if success:
                notify_added("copia di film")
            else:
                ui.notify(mess, type="negative")
        else:
            ui.notify("Non puoi scegliere sia un film che una stagione!", type="negative")
            return
    else:
        ui.notify("Devi scegliere o un film, o una serie, o una stagione di una serie specifica!", type="info")
        
            

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
    global selected_genres
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
    if len(selected_genres) <= 0:
        notify_empty_field("Genere")
        return
    mess, success = add_movie(title, ogTitle, runtime, mark, year, country, director, selected_actors, selected_genres)
    if success:          
        selected_genres = []
        selected_actors = []
        notify_added("film")
    else:
        ui.notify(mess, type="negative")

def add_series_check(title: str, ogTitle: str, mark: int, year: int, country: str):
    global selected_genres
    global selected_actors
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
    if len(selected_genres) <= 0:
        notify_empty_field("Genere")
        return
    mess, success = add_series(title, ogTitle, mark, year, country, selected_actors, selected_genres)
    if success:          
        selected_genres = []
        selected_actors = []
        notify_added("serie")
    else:
        ui.notify(mess, type="negative")

def add_season_check(seriesId: int, numSeason: int, mark: int, year: int, country: str, numEp: int):
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
    mess, success = add_season(seriesId, numSeason, numEp, mark, year, country, selected_actors)
    if success:
        notify_added("stagione")
    else:
        ui.notify(mess, type="negative")  
    
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