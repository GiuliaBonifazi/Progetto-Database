from nicegui import ui
from template import all_user_order_history
from logged_user import get_user


@ui.page("/order_history")
def order_history():
    with ui.column().classes("w-full items-center"):
        all_user_order_history(get_user()["userId"])