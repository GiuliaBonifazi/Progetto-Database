from nicegui import ui
from backend import login_check, find_user, register_user, repeat_email
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
        name = ui.input(label="Nome *", placeholder="Scrivi il tuo nome")
        
        surname = ui.input(label="Cognome *", placeholder="Scrivi il tuo cognome")
        
        email = ui.input(label="Email *", placeholder="Scrivi la tua mail")
        
        pw = ui.input(label="Password *", placeholder="Scrivi la tua password", password=True)
        
        tel = ui.input(label="Numero di telefono *:", placeholder="Numero di telefono senza prefisso")
        
        with ui.row():
            ui.label("* Campi obbligatori")
            ui.button("Conferma", on_click=lambda: signup(email=email.value, password=pw.value, name=name.value, surname=surname.value, cell=tel.value))
            
def login(email: str, password: str):
    if login_check(email, password):
        loggedUser = get_user()
        foundUser = find_user(email, password)
        loggedUser["userId"] = foundUser[0]
        loggedUser["name"] = foundUser[1]
        loggedUser["surname"] = foundUser[2]
        print(get_user())
    else:
        ui.notify("Login fallito")

def signup(email: str, password: str, name: str, surname: str, cell: int):
    if not repeat_email(email):
        register_user(email, password, name, surname, cell)
        ui.navigate.to("/login_page")
    else:
        ui.notify("Email già in uso")
        