from nicegui import ui
from backend import get_top_ten_genres
from random import randint

def genre_card(genre, amount, placement, color):
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
            genre_card(genres[i][0], genres[i][1], i+1, card_colors[randint(0, 4)])