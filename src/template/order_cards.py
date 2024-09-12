from nicegui import ui

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