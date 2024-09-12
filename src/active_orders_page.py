from nicegui import ui
from template import pending_orders

@ui.page("/active_orders_page")
def active_orders_page():
    pending_orders()