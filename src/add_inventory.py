from nicegui import ui
from template import directors_as_dict, actors_as_dict, notify_empty_field

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
    with ui.tab_panels(tabs, value=film).classes('w-full'):
        #FILM -----
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
                    ui.label("Seleziona attori: ")
                    actors = ui.select(actors_as_dict(), label="Attori", multiple=True, on_change=update_selected_actors).props("use-chips")
                ui.button(text="Conferma", on_click=lambda: add_movie(title.value, ogTitle.value, runtime.value, mark.value, 
                                                              year.value, country.value, director.value))
        with ui.tab_panel(series):
            ui.label('Second tab')
        with ui.tab_panel(season):
            ui.label('Second tab')
        with ui.tab_panel(member):
            ui.label('Second tab')
        with ui.tab_panel(copy):
            ui.label('Second tab')
        with ui.tab_panel(zone):
            ui.label('Second tab')

def update_selected_actors(event):
    global selected_actors
    selected_actors = event.value
    return

def add_movie(title: str, ogTitle: str, runtime: int, mark: int, year: int, country: str, director: int):
    global selected_actors
    print(selected_actors)
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
    