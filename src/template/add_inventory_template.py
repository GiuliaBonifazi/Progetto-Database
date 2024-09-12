from nicegui import ui
from backend import get_all_directors, get_all_actors, get_series, get_movies, get_seasons_from_series


def directors_as_dict():
    directors = get_all_directors()
    dict = {}
    for dir in directors:
        dict.update( {dir[1] : dir[0]} )
    return dict

def actors_as_dict():
    actors = get_all_actors()
    dict = {}
    for act in actors:
        dict.update( {act[1] : act[0] } )
    return dict

def series_as_dict():
    series = get_series()
    dict = {}
    for s in series:
        dict.update( {s[5] : s[0] } )
    return dict

def movies_as_dict():
    movies = get_movies()
    dict = {}
    for m in movies:
        dict.update( {m[7] : m[0]} )
    return dict