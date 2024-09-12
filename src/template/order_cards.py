from nicegui import ui
from random import randint
from backend import get_order_items, all_orders_from_user

# attribute order: SERIE.Titolo, FILM.Titolo, NumStagione, Supporto
def simple_order_card(info, languages, color):
    with ui.card().classes("w-full items-center border bg-" + color + "-300" ):
        with ui.column().classes("w-full items-center"):
            if info[1] is None:
                with ui.row():
                    ui.label("Titolo: " + info[0]).classes("text-" + color + "-700").style("font-weight: bold; font-size: 120%")
                    ui.label("Stagione: " + str(info[2])).classes("text-" + color + "-700").style("font-weight: bold; font-size: 120%")
            else:
                ui.label("Titolo: " + info[1]).classes("text-" + color + "-900").style("font-weight: bold; font-size: 120%")
            ui.label("Supporto: " + info[3]).classes("text-" + color + "-700").style("font-weight: bold; font-size: 120%")
            with ui.card().classes("border bg-" + color + "-200"):
                with ui.row():
                    ui.label("Lingue: ").classes("text-" + color + "-400").style("font-weight: bold; font-size: 120%")
                    for l in languages:
                        ui.label(l).classes("text-" + color + "-400").style("font-weight: bold; font-size: 120%")
                        
                        
def all_orders_from_list(orders):
    card_colors = ["indigo", "blue", "purple", "green", "pink"]
    with ui.column().classes("w-full, items-center"):
        with ui.grid(columns=3).classes("w-full, items-center"):
            for val in orders:
                info, lang = val
                simple_order_card(info, lang, card_colors[randint(0, 4)])

# attribute order: DataConferma, DataRitiro, RitiroEffettuato
def order_card_with_dates(info, orders):
    with ui.card():
        with ui.column():
            ui.label("Data Conferma: " + str(info[0])).style("font-size: 130%; font-weight: bold;")
            ui.label("Data Ritiro: " + str(info[1])).style("font-size: 130%; font-weight: bold;")
            if info[2] is None:
                ui.label("Data Ritiro ancora non raggiunta").style("font-size: 130%; font-weight: bold;")
            else:
                ui.label("Ritiro effettuato: " + str(info[2])).style("font-size: 130%; font-weight: bold;")
            if info[3] is None:
                ui.label("Reso ancora non effettuato").style("font-size: 130%; font-weight: bold;")
            else:
                ui.label("Reso effettuato: " + str(info[2])).style("font-size: 130%; font-weight: bold;")
        all_orders_from_list(get_order_items(orders))

def all_user_order_history(userId: int):
    history = all_orders_from_user(userId)
    for info, orders in history:
        order_card_with_dates(info, orders)