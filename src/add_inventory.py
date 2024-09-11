from nicegui import ui

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
        with ui.tab_panel(film):
            with ui.column().classes('w-full items-center'):
                title = ui.input(label="Titolo")
                ogTitle = ui.input(label="Titolo originale")
                runtime = ui.input(label="Durata")
                mark = ui.input(label="Valutazione")
                year = ui.input(label="Anno d'uscita")
                country = ui.input(label="Paese di produzione")
                with ui.menu() as director:
                    ui.menu_item()
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
            