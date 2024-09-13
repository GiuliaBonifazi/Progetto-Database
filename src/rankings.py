from nicegui import ui
from template import genre_rankings, couple_rankings, actor_rankings,director_rankings

@ui.page("/rankings_page")
def rankings_page():
    with ui.tabs().classes('w-full') as tabs:
        first = ui.tab('Top 10 coppie attore/regista')
        second = ui.tab('Top 10 attori')
        third = ui.tab('Top 10 registi')
        fourth = ui.tab('Top 10 generi in negozio')
    with ui.tab_panels(tabs, value=first).classes('w-full'):
        with ui.tab_panel(first).classes("w-full items-center"):
            couple_rankings()
        with ui.tab_panel(second).classes("w-full items-center"):
            actor_rankings()
        with ui.tab_panel(third).classes("w-full items-center"):
            director_rankings()
        with ui.tab_panel(fourth).classes("w-full items-center"):
            genre_rankings()