from nicegui import ui
from backend import get_top_ten_genres, get_top_ten_couples, get_cast_member_name, get_top_ten_rated_actors, top_ten_rated_directors
from random import randint

def placement_card(genre, amount, placement, color):
    with ui.card().classes("border bg-" + color + "-200"):
        with ui.row():
            ui.label(str(placement)).style("font-size: 170%; font-weight: bold;")
            ui.label(genre).style("font-size: 140%; font-weight: bold;").classes("text-" + color)
            ui.label(str(amount)).style("font-size: 140%; font-weight: bold;").classes("text-" + color)

def genre_rankings():
    card_colors = ["indigo", "blue", "purple", "green", "pink"]
    genres = get_top_ten_genres()
    with ui.column().classes("w-full, items-left"):
        for i in range(len(genres)):
            placement_card(genres[i][0], genres[i][1], i+1, card_colors[randint(0, 4)])

def couple_rankings():
    card_colors = ["indigo", "blue", "purple", "green", "pink"]
    couples = get_top_ten_couples()
    with ui.column().classes("w-full, items-left"):
        for i in range(len(couples)):
            placement_card(get_cast_member_name(couples[i][0])[0] + " - " + get_cast_member_name(couples[i][1])[0], 
                           couples[i][2],
                           i+1, 
                           card_colors[randint(0, 4)])

def member_rankings(members):
    card_colors = ["indigo", "blue", "purple", "green", "pink"]
    with ui.column().classes("w-full, items-left"):
        for i in range(len(members)):
            placement_card(get_cast_member_name(members[i][0]), members[i][1], i + 1, card_colors[randint(0, 4)])
            
def actor_rankings():
    member_rankings(get_top_ten_rated_actors())

def director_rankings():
    member_rankings(top_ten_rated_directors())