from nicegui import ui

@ui.page("/archive_page")
def archive_page():
    with ui.tabs() as tabs:
        series = ui.tab("Serie")
        film = ui.tab("Film")
    with ui.tab_panels(tabs, value=series).classes("w-full"):
        with ui.tab_panel(series):
            