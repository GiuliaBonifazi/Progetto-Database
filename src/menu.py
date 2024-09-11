from nicegui import ui
from logged_user import get_user

@ui.page("/menu_page")
def menu_page():
    with ui.column().classes('w-full items-center'):
        ui.label("Ciao, " + get_user()["name"] + "!").style("font-weight: bold; font-size: 150%")
        with ui.card().style("background-color: red;"):
            ui.label("Sei un cliente?").style("font-size: 150%")
            with ui.row():
                ui.button(icon="movie", text="Archivio").classes("auto")
                ui.button(icon="scoreboard", text="Cronologia ordini")
            ui.button(icon='history', text="Ordine corrente")
        with ui.card().style("background-color: blue;"):
            ui.label("Sei l'amministratore?").style("font-size: 150%")
            with ui.row():
                ui.button(icon="inventory", text="Amplia inventario").classes("auto")
                ui.button(icon="newspaper", text="Ordini per cliente")
            ui.button(icon='history', text="Ordini attivi")
        