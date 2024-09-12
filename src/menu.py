from nicegui import ui
from logged_user import get_user
from backend import login_admin
from archive import archive_page
from add_inventory import add_to_archive_page
from current_order import current_order

@ui.page("/menu_page")
def menu_page():
    with ui.column().classes('w-full items-center'):
        ui.label("Ciao, " + get_user()["name"] + "!").style("font-weight: bold; font-size: 150%")
        with ui.card().classes("bg-indigo"):
            ui.label("Sei un cliente?").style("font-size: 150%")
            with ui.row():
                ui.button(icon="movie", text="Archivio", on_click=lambda: ui.navigate.to(archive_page)).classes("bg-purple")
                ui.button(icon="history", text="Cronologia ordini").classes("bg-purple")
            with ui.row():
                ui.button(icon='verified', text="Ordine corrente", on_click=lambda: ui.navigate.to(current_order)).classes("bg-purple")
                ui.button(icon='sort', text="Classifiche").classes("bg-purple")
        with ui.card().classes("bg-blue"):
            ui.label("Sei l'amministratore?").style("font-size: 150%")
            with ui.row():
                ui.button(icon="add_circle", text="Amplia inventario", on_click=lambda: add_to_inventory()).classes("bg-cyan")
                ui.button(icon="newspaper", text="Ordini per cliente").classes("bg-cyan")
            ui.button(icon='history', text="Ordini attivi").classes("bg-cyan")
    admin_pw = ui.input(label="Password admin")
    ui.button(icon="key", text="Login amministratore", on_click=lambda: check_admin(admin_pw.value)).classes("bg-blue")
    
def check_admin(password: str):
    if not password:
        ui.notify("Inserisci la password admin", color="red")
        return
    user = get_user()
    if user["admin"] == False:
        if login_admin(get_user()["userId"], password):
            user["admin"] = True
            ui.notify("Benvenuto, admin!", type="positive")
        else:
            ui.notify("Password admin sbagliata!", type="info")

def add_to_inventory():
    if get_user()["admin"]:
        ui.navigate.to(add_to_archive_page)
    else:
        ui.notify("Non sei l'amministratore, non puoi accedere a questa funzione!", type="warning")
        