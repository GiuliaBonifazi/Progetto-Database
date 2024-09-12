from nicegui import ui
from backend import all_user_names, all_user_surnames, users_from_name_surname

@ui.page("/orders_by_user_page")
def orders_by_user_page():
    with ui.column().classes("w-full items-center"):
        with ui.row():
            ui.label("Nome: ")
            name = ui.select([x[0] for x in all_user_names()], with_input=True)
        with ui.row():
            ui.label("Cognome: ")
            surname = ui.select([x[0] for x in all_user_surnames()], with_input=True)
        ui.button("Cerca")