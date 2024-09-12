from nicegui import ui
from backend import get_order_items
from logged_user import get_user
from template import all_orders_from_list

@ui.page("/current_order")
def current_order():
    all_orders_from_list(get_order_items(get_user()["order"]))