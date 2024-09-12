from nicegui import ui
from backend import all_user_names, all_user_surnames, users_from_name_surname
from template import all_user_order_history

@ui.page("/orders_by_user_page")
def orders_by_user_page():
    with ui.column().classes("w-full items-center"):
        with ui.row():
            ui.label("Nome: ")
            name = ui.select([x[0] for x in all_user_names()], with_input=True)
        with ui.row():
            ui.label("Cognome: ")
            surname = ui.select([x[0] for x in all_user_surnames()], with_input=True)
        ui.button("Cerca", on_click=lambda: user_selected(name.value, surname.value))
        ui.button("Refresh", on_click=lambda: ui.navigate.reload())
        
        
def user_selected(name: str, surname: str):
    userIds = users_from_name_surname(name, surname)
    for id in userIds:
        ui.label(str(id[1]) + " " + str(id[2])).style("font-size:150%; font-weight: bold;")
        all_user_order_history(id[0])