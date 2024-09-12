from nicegui import ui
from backend import get_order_items
from logged_user import get_user

@ui.page("/current_order")
def current_order():
    with ui.column().classes("w-full, items-center"):
        ui.button("Conferma").classes("bg-green")
        print(get_order_items(get_user()["order"]))