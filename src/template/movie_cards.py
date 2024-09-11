from nicegui import ui
from backend import get_movies, get_director_name, get_movie_actors_names, rent_movie_copy
from random import randint
from logged_user import get_user

def movie_card(color, movie, director, actors):
    with ui.card().classes("bg-" + color + "-300 border"):
        with ui.column():
            ui.label(text=movie[0]).style("font-weight: bold; font-size: 140%")
            ui.label(text="Titolo Originale: " + movie[1]).classes("text-" + color + "-700").style("font-weight: bold; font-size: 120%")
            ui.label(text="Durata: " + str(movie[2]) + " min").classes("text-" + color).style("font-weight: bold; font-size: 120%")
            ui.label(text="Valutazione: " + str(movie[3]) + "/100").classes("text-" + color + "-700").style("font-weight: bold; font-size: 120%")
            ui.label(text="Anno d'Uscita: " + str(movie[4])).classes("text-" + color).style("font-weight: bold; font-size: 120%")
            ui.label(text="Paese di Produzione: " + movie[5]).classes("text-" + color + "-700").style("font-weight: bold; font-size: 120%")
            ui.label(text="Regista: " + director).classes("text-" + color).style("font-weight: bold; font-size: 120%")
            with ui.row():
                ui.label(text="Attori:").classes("text-" + color).style("font-weight: bold; font-size: 120%")
                for actor in actors:
                    ui.label(actor[0]).classes("text-" + color).style("font-weight: bold; font-size: 120%")
            with ui.row():
                ui.button(text="DVD", on_click=lambda: rent_movie(movie[6], "DVD"))
                ui.button(text="VHS", on_click=lambda: rent_movie(movie[6], "VHS"))
                ui.button(text="Blu-Ray", on_click=lambda: rent_movie(movie[6], "Blu Ray"))
                
def all_movie_cards():
    movie_colors = ["indigo", "blue", "purple", "green", "pink"]
    movies = get_movies()
    with ui.grid(columns=4):
        for m in movies:
            movie_card(movie_colors[randint(0, 4)], m, get_director_name(m[6])[0], get_movie_actors_names(m[7]))

def rent_movie(movieId, support):
    res = rent_movie_copy(movieId, support)
    if res is None:
        ui.notify("Ci spiace! Il titolo richiesto non è al momento disponibile in quel formato", type="negative")
    else:
        user = get_user
        user["order"].append(res[0])
        print(user)