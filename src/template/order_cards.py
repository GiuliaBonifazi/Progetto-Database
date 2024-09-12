from nicegui import ui
from random import randint
from backend import get_order_items, all_orders_from_user, mark_collection, mark_returned, active_orders
from logged_user import get_user

# attribute order: SERIE.Titolo, FILM.Titolo, NumStagione, Supporto, CodCopia
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
            ui.button(icon="delete", on_click=lambda: delete_item(info[4]))

def delete_item(id: int):
    get_user()["order"].remove(id)
    ui.navigate.reload()
                        
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
        
# CodPrenotazione, CodUtente, DataConferma, DataRitiro, RitiroEffettuato, ConsegnaEffettuata
def order_card_with_buttons(info, items):
    with ui.card():
        ui.label("Ordine " + str(info[0])).style("font-size: 150%; font-weight: bold;")
        with ui.column():
            ui.label("Data Conferma: " + str(info[2])).style("font-size: 130%; font-weight: bold;")
            ui.label("Data Ritiro: " + str(info[3])).style("font-size: 130%; font-weight: bold;")
            with ui.row():
                if info[4] is None:
                        ui.label("Data Ritiro ancora non raggiunta").style("font-size: 130%; font-weight: bold;")
                        ui.button("Effettuato", on_click=lambda: collected(True, info[0])).classes("bg-green")
                        ui.button("Non effettuato", on_click=lambda: collected(False, info[0])).classes("bg-red")
                else:
                    ui.label("Ritiro effettuato: " + (str(bool(info[4])))).style("font-size: 130%; font-weight: bold;")
            with ui.row():
                if info[5] is None:
                    ui.label("Reso ancora non effettuato").style("font-size: 130%; font-weight: bold;")
                    ui.button("Effettuato", on_click=lambda: returned(True, info[0])).classes("bg-green")
                    ui.button("Non effettuato", on_click=lambda: returned(False, info[0])).classes("bg-red")
                else:
                    ui.label("Reso effettuato: " + str((bool(info[5])))).style("font-size: 130%; font-weight: bold;")
        items_with_pos(items)

def returned(value, orderId):
    mark_returned(value, orderId)
    ui.navigate.reload()

def collected(value, orderId):
    mark_collection(value, orderId)
    ui.navigate.reload()

def item_card_with_pos(info, languages, color):
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
            with ui.row():
                ui.label("Scaffalatura: " + str(info[4]))
                ui.label("Scaffale: " + str(info[5]))

def items_with_pos(items):
    card_colors = ["indigo", "blue", "purple", "green", "pink"]
    with ui.column().classes("w-full, items-center"):
        with ui.grid(columns=3).classes("w-full, items-center"):
            for val in items:
                info, lang = val
                item_card_with_pos(info, lang, card_colors[randint(0, 4)])
                
def pending_orders():
    orders = active_orders()
    for info, ord in orders:
       order_card_with_buttons(info, ord)