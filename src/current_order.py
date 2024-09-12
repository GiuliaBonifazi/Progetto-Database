from nicegui import ui
from backend import get_order_items
from logged_user import get_user
from template import simple_order_card
from random import randint

@ui.page("/current_order")
def current_order():
    card_colors = ["indigo", "blue", "purple", "green", "pink"]
    with ui.column().classes("w-full, items-center"):
        with ui.grid(columns=3).classes("w-full, items-center"):
            for val in get_order_items(get_user()["order"]):
                info, lang = val
                simple_order_card(info, lang, card_colors[randint(0, 4)])
        ui.button("Conferma").classes("bg-green")