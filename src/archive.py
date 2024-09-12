from nicegui import ui
from template import all_movie_cards, all_series_cards

@ui.page("/archive_page")
def archive_page():
    with ui.tabs().classes() as tabs:
        series = ui.tab("Serie")
        film = ui.tab("Film")
    with ui.tab_panels(tabs, value=series).classes("items-center"):
        with ui.tab_panel(series):
            ui.label("Serie").style("font-size: 150%; font-weight: bold;")
            all_series_cards()
        with ui.tab_panel(film):
            ui.label("Film").style("font-size: 150%; font-weight: bold;")
            all_movie_cards()
                    