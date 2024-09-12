from nicegui import ui
from backend import get_order_items, confirm_order
from logged_user import get_user
from template import all_orders_from_list, notify_empty_field

with ui.dialog() as dateDialog, ui.card():
    ui.label('Scegli una data')
    with ui.row():
        ui.date(on_change=lambda event: dateDialog.submit(event.value))
        ui.button('Chiudi', on_click=lambda: dateDialog.submit("Closed"))


@ui.page("/current_order")
def current_order():
    all_orders_from_list(get_order_items(get_user()["order"]))
    date = ui.date()
    ui.button("Conferma", on_click=lambda: confirm(date.value)).classes("bg-green")
    
def confirm(date):
    user = get_user()
    if not date:
        notify_empty_field("Data di ritiro")
        return
    if user["order"] == []:
        ui.notify("Prenotazione vuota", type="negative")
        return
    order = user["order"]
    user["order"] = []
    confirm_order(order, date, user["userId"])
    ui.notify("Prenotazione confermata!", type="positive")
    ui.navigate.reload()
    