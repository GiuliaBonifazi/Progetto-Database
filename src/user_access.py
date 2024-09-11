from nicegui import ui
from backend import login_check, find_user
from logged_user import get_user

@ui.page('/login_page')
def login_page():
    ui.page_title = "Login"
    with ui.column().classes('w-full items-center'):
        ui.label("Login").style("font-size: 150%; font-weight: bold;")
        
        email = ui.input(label="Email *", placeholder="Scrivi la tua mail")
        
        pw = ui.input(label="Password *", placeholder="Scrivi la tua password", password=True)
        
        with ui.row():
            ui.label("* Campi obbligatori")
            ui.button("Conferma", on_click=lambda: login(email.value, pw.value))
        ui.link("Non hai un account? Registrati", "/signup_page")

@ui.page('/signup_page')
def signup_page():
    ui.page_title = "Registrati"
    ui.label("Registrati").style("font-size: 150%; font-weight: bold;")
    with ui.column().classes('w-full items-center'):
        ui.input(label="Nome *", placeholder="Scrivi il tuo nome")
        
        ui.input(label="Cognome *", placeholder="Scrivi il tuo cognome")
        
        ui.input(label="Email *", placeholder="Scrivi la tua mail")
        
        ui.input(label="Password *", placeholder="Scrivi la tua password", password=True)
        
        ui.input(label="Numero di telefono *:", placeholder="Numero di telefono senza prefisso").default_style()
        
        with ui.row():
            ui.label("* Campi obbligatori")
            ui.button("Conferma")
            
def login(email: str, password: str):
    if login_check(email, password):
        loggedUser = get_user()
        foundUser = find_user(email, password)
        loggedUser["userId"] = foundUser["CodUtente"]
        loggedUser["name"] = foundUser["Nome"]
        loggedUser["surname"] = foundUser["Cognome"]
    else:
        ui.notify("Login fallito")

def signup(email: str, password: str, name: str, surname: str):
    