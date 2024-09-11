from nicegui import ui
from logged_user import get_user
from backend import login_admin

@ui.page("/menu_page")
def menu_page():
    print(get_user())
    with ui.column().classes('w-full items-center'):
        ui.label("Ciao, " + get_user()["name"] + "!").style("font-weight: bold; font-size: 150%")
        with ui.card().classes("bg-indigo"):
            ui.label("Sei un cliente?").style("font-size: 150%")
            with ui.row():
                ui.button(icon="movie", text="Archivio").classes("bg-purple")
                ui.button(icon="scoreboard", text="Cronologia ordini").classes("bg-purple")
            ui.button(icon='history', text="Ordine corrente").classes("bg-purple")
        with ui.card().classes("bg-blue"):
            ui.label("Sei l'amministratore?").style("font-size: 150%")
            with ui.row():
                ui.button(icon="inventory", text="Amplia inventario").classes("bg-cyan")
                ui.button(icon="newspaper", text="Ordini per cliente").classes("bg-cyan")
            ui.button(icon='history', text="Ordini attivi").classes("bg-cyan")
    admin_pw = ui.input(label="Password admin")
    ui.button("Login amministratore", on_click=lambda: check_admin(admin_pw.value)).classes("bg-blue")
    
def check_admin(password: str):
    user = get_user()
    if user["admin"] == False:
        if login_admin(get_user()["userId"], password):
            user["admin"] = True
        else:
            ui.notify("Password admin sbagliata!")
        