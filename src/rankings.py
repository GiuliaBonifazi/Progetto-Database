from nicegui import ui

@ui.page("/rankings_page")
def rankings_page():
    with ui.tabs().classes('w-full') as tabs:
        first = ui.tab('Top 10 coppie attore/regista')
        second = ui.tab('Top 10 attori')
        third = ui.tab('Top 10 registi')
        fourth = ui.tab('Top 10 generi in negozio')
    with ui.tab_panels(tabs, value=first).classes('w-full'):
        with ui.tab_panel(first):
            ui.button()
        with ui.tab_panel(second):
            ui.button()
        with ui.tab_panel(third):
            ui.button()
        with ui.tab_panel(fourth):
            ui.button()