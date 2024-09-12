from nicegui import ui

def notify_empty_field(field):
    ui.notify("Non puoi lasciare il campo " + field + " vuoto!", type="warning")
    
def notify_added(item):
    ui.notify("Aggiunta di " + item + " avvenuta con successo!", type="positive")