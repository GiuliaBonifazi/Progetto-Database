from nicegui import ui

@ui.page('/login_page')
def login_page():
    ui.page_title = "Login"
    with ui.column().classes('w-full items-center'):
        ui.label("Login").style("font-size: 150%; font-weight: bold;")
        
        ui.input(label="Email *", placeholder="Scrivi la tua mail")
        
        ui.input(label="Password *", placeholder="Scrivi la tua password", password=True)
        
        ui.input(label="Password admin:", placeholder="Password amministratore", password=True)
        
        with ui.row():
            ui.label("* Campi obbligatori")
            ui.button("Conferma")
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