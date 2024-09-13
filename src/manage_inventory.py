from nicegui import ui
from template import movies_as_dict, series_as_dict, items_with_pos_and_delete
from backend import get_copies_info_from_series, get_copies_info_from_movie

@ui.page("/manage_inventory_page")
def manage_inventory_page():
    with ui.column().classes("w-full items-center"):
        with ui.row():
            ui.label("Film: ")
            movie = ui.select(movies_as_dict(), with_input=True, clearable=True)
        with ui.row():
            ui.label("Serie: ")
            series = ui.select(series_as_dict(), with_input=True, clearable=True)
        ui.button("Cerca", on_click=lambda: search(movie.value, series.value))
        
def search(movieId: int, seriesId: int):
    if seriesId:
        with ui.card().classes("border"):
            items_with_pos_and_delete(get_copies_info_from_series(seriesId))
    elif movieId:
        with ui.card().classes("border"):
            items_with_pos_and_delete(get_copies_info_from_movie(movieId))
    else:
        ui.notify("Scegli almeno un film o una serie!", type="warning")