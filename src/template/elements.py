from nicegui import ui

def notify_empty_field(field):
    ui.notify("Non puoi lasciare il campo " + field + " vuoto!", type="warning")