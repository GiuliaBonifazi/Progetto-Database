from nicegui import ui
from backend import get_movies, get_director_name, get_movie_actors_names, rent_movie_copy, get_movie_genres
from random import randint
from logged_user import get_user

def movie_card(color, movie, director, actors, genres):
    with ui.card().classes("bg-" + color + "-300 border"):
        with ui.column():
            ui.label(text=movie[0]).style("font-weight: bold; font-size: 140%")
            ui.label(text="Titolo Originale: " + movie[1]).classes("text-" + color + "-700").style("font-weight: bold; font-size: 120%")
            ui.label(text="Durata: " + str(movie[2]) + " min").classes("text-" + color).style("font-weight: bold; font-size: 120%")
            ui.label(text="Valutazione: " + str(movie[3]) + "/100").classes("text-" + color + "-700").style("font-weight: bold; font-size: 120%")
            ui.label(text="Anno d'Uscita: " + str(movie[4])).classes("text-" + color).style("font-weight: bold; font-size: 120%")
            ui.label(text="Paese di Produzione: " + movie[5]).classes("text-" + color + "-700").style("font-weight: bold; font-size: 120%")
            with ui.row():
                ui.label(text="Genere/i: ").classes("text-" + color).style("font-weight: bold; font-size: 120%")
                for g in genres:
                    ui.label(g[0]).classes("text-" + color).style("font-weight: bold; font-size: 120%")
            with ui.card().classes("bg-" + color + "-100"):
                ui.label(text="Regista: " + director).classes("text-" + color + "-700").style("font-weight: bold; font-size: 120%")
                with ui.row():
                    ui.label(text="Attori: ").classes("text-" + color + "-700").style("font-weight: bold; font-size: 120%")
                    for actor in actors:
                        ui.label(actor[0]).classes("text-" + color + "-700").style("font-weight: bold; font-size: 120%")
            with ui.row():
                ui.button(text="DVD", on_click=lambda: rent_movie(movie[6], "DVD"))
                ui.button(text="VHS", on_click=lambda: rent_movie(movie[6], "VHS"))
                ui.button(text="Blu-Ray", on_click=lambda: rent_movie(movie[6], "Blu-Ray"))
                
def all_movie_cards():
    movie_colors = ["indigo", "blue", "purple", "green", "pink"]
    movies = get_movies()
    with ui.grid(columns=4):
        for m in movies:
            movie_card(movie_colors[randint(0, 4)], m, get_director_name(m[6])[0], get_movie_actors_names(m[7]), get_movie_genres(m[7]))

def rent_movie(movieId, support):
    res, success= rent_movie_copy(movieId, support)
    if not success:
        ui.notify(res, type="negative")
    else:
        user = get_user()
        if res[0] not in user["order"]:
            user["order"].append(res[0])
            ui.notify("Aggiunto alla prenotazione (ricorda di confermare prima di uscire!)", type="positive")
        else:
            ui.notify("C'è già una copia di questo articolo nella tua prenotazione!")