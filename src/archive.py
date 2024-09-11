from nicegui import ui
from movie_cards import all_movie_cards

@ui.page("/archive_page")
def archive_page():
    with ui.tabs().classes() as tabs:
        series = ui.tab("Serie")
        film = ui.tab("Film")
    with ui.tab_panels(tabs, value=series).classes("items-center"):
        with ui.tab_panel(series):
            with ui.column():
                ui.label("Serie").style("font-size: 150%; font-weight: bold;")
        with ui.tab_panel(film):
            ui.label("Film").style("font-size: 150%; font-weight: bold;")
            all_movie_cards()
                    