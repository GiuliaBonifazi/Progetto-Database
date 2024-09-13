from nicegui import ui
from template import all_movie_cards, all_series_cards, some_movie_cards, some_series_cards
from backend import search_movie_db, search_series_db

movieGrid = None
seriesCol = None

@ui.page("/archive_page")
def archive_page():
    global movieGrid
    global seriesCol
    with ui.tabs().classes() as tabs:
        series = ui.tab("Serie")
        film = ui.tab("Film")
    with ui.tab_panels(tabs, value=series).classes("items-center"):
        with ui.tab_panel(series) as seriesPanel:
            ui.label("Serie").style("font-size: 150%; font-weight: bold;")
            with ui.row():
                ui.label("Cerca per attore:").style("font-size: 130%; font-weight: bold;")
                seriesAct = ui.input(label="Attore")
                ui.button("Cerca", on_click=lambda: series_search("ACT", seriesAct.value, seriesPanel))
            with ui.row():
                ui.label("Cerca per titolo:").style("font-size: 130%; font-weight: bold;")
                seriesTitle = ui.input(label="Titolo")
                ui.button("Cerca", on_click=lambda: series_search("TTL", seriesTitle.value, seriesPanel))
            with ui.row():
                ui.label("Cerca per anno d'uscita:").style("font-size: 130%; font-weight: bold;")
                seriesYear = ui.input(label="Anno d'uscita")
                ui.button("Cerca", on_click=lambda: series_search("YEA", seriesYear.value, seriesPanel))
            seriesCol = all_series_cards()
        with ui.tab_panel(film) as filmPanel:
            ui.label("Film").style("font-size: 150%; font-weight: bold;")
            with ui.row():
                ui.label("Cerca per attore:").style("font-size: 130%; font-weight: bold;")
                movieAct = ui.input(label="Attore")
                ui.button("Cerca", on_click=lambda: movie_search("ACT", movieAct.value, filmPanel))
            with ui.row():
                ui.label("Cerca per titolo:").style("font-size: 130%; font-weight: bold;")
                movieTitle = ui.input(label="Titolo")
                ui.button("Cerca", on_click=lambda: movie_search("TTL", movieTitle.value, filmPanel))
            with ui.row():
                ui.label("Cerca per anno d'uscita:").style("font-size: 130%; font-weight: bold;")
                movieYear = ui.input(label="Anno d'uscita")
                ui.button("Cerca", on_click=lambda: movie_search("YEA", movieYear.value, filmPanel))
            with ui.row():
                ui.label("Cerca per Regista:").style("font-size: 130%; font-weight: bold;")
                movieDir = ui.input(label="Regista")
                ui.button("Cerca", on_click=lambda: movie_search("DIR", movieDir.value, filmPanel))
            movieGrid = all_movie_cards()
            
def movie_search(type, search, filmPanel):
    global movieGrid
    filmPanel.remove(movieGrid)
    with filmPanel:
        movieGrid = some_movie_cards(search_movie_db(type, search))
        
def series_search(type, search, seriesPanel):
    global seriesCol
    seriesPanel.remove(seriesCol)
    with seriesPanel:
        seriesCol = some_series_cards(search_series_db(type, search))