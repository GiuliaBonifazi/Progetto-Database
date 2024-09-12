from nicegui import ui
from random import randint
from logged_user import get_user
from backend import get_series, get_series_actors_names, get_seasons_from_series, rent_season, rent_series, get_series_genres

def series_card(series, seasons, actors, color, genres):
    with ui.card().classes("bg-" + color + "-300 border").classes("w-full"):
        with ui.column():
            ui.label(text=series[0]).style("font-weight: bold; font-size: 140%")
            with ui.row():
                ui.label(text="Titolo Originale: " + series[1]).classes("text-" + color + "-700").style("font-weight: bold; font-size: 120%")
                ui.label(text="Valutazione: " + str(series[2]) + "/100").classes("text-" + color).style("font-weight: bold; font-size: 120%")
                ui.label(text="Anno d'Uscita: " + str(series[3])).classes("text-" + color + "-700").style("font-weight: bold; font-size: 120%")
                ui.label(text="Paese di Produzione: " + series[4]).classes("text-" + color).style("font-weight: bold; font-size: 120%")
            with ui.row():
                ui.label(text="Genere/i: ").classes("text-" + color + "-700").style("font-weight: bold; font-size: 120%")
                for g in genres:
                    ui.label(g[0]).classes("text-" + color + "-700").style("font-weight: bold; font-size: 120%")
            with ui.card().classes("bg-" + color + "-200"):
                with ui.row():
                    ui.label(text="Attori:").classes("text-" + color).style("font-weight: bold; font-size: 120%")
                    for actor in actors:
                        ui.label(actor[0]).classes("text-" + color).style("font-weight: bold; font-size: 120%")
            with ui.grid(columns=3 ):
                for season in seasons:
                    season_card(season, color)
            with ui.row():
                ui.button(text="DVD", on_click=lambda: check_rent_series(series[5], "DVD"))
                ui.button(text="VHS", on_click=lambda: check_rent_series(series[5], "VHS"))
                ui.button(text="Blu-Ray", on_click=lambda: check_rent_series(series[5], "Blu-Ray"))

def check_rent_series(seriesId: int, support: str):
    res, success = rent_series(seriesId, support)
    if not success:
        ui.notify(res, type="negative")
    else:
        user = get_user()
        for id in res:
            if res not in user["order"]:
                user["order"].append(id)
            else:
                ui.notify("C'è già una copia di questo articolo nella tua prenotazione!")
        ui.notify("Aggiunto alla prenotazione (ricorda di confermare prima di uscire!)", type="positive")

def season_card(season, color):
    with ui.card().classes("bg-" + color + "-100 border"):
        with ui.column():
            ui.label(text="Stagione " + str(season[1])).classes("text-" + color + "-700").style("font-weight: bold; font-size: 100%")
            ui.label(text="Numero episodi: " + str(season[2])).classes("text-" + color + "-700")
            ui.label(text="Valutazione: " + str(season[3]) + "/100").classes("text-" + color + "-700")
            ui.label(text="Anno d'Uscita: " + str(season[4])).classes("text-" + color + "-700")
            ui.label(text="Paese di Produzione: " + season[5]).classes("text-" + color + "-700")
            with ui.row():
                ui.button(text="DVD", on_click=lambda: check_rent_season(season[0], season[1] , "DVD"))
                ui.button(text="VHS", on_click=lambda: check_rent_season(season[0], season[1] , "VHS"))
                ui.button(text="Blu-Ray", on_click=lambda: check_rent_season(season[0], season[1] , "Blu-Ray"))
                
def check_rent_season(seriesId: int, seasonNum:  int, support: str):
    res, success = rent_season(seriesId, seasonNum, support)
    if not success or res is None:
        ui.notify(res, type="negative")
    else:
        user = get_user()
        if res[0] not in user["order"]:
            user["order"].append(res[0])
            ui.notify("Aggiunto alla prenotazione (ricorda di confermare prima di uscire!)", type="positive")
        else:
            ui.notify("C'è già una copia di questo articolo nella tua prenotazione!")

def all_series_cards():
    series_colors = ["indigo", "blue", "purple", "green", "pink"]
    series = get_series()
    with ui.column():
        for s in series:
            series_card(s, get_seasons_from_series(s[5]), get_series_actors_names(s[5]), series_colors[randint(0, 4)], get_series_genres(s[5]))