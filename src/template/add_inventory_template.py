from nicegui import ui
from backend import get_all_directors, get_all_actors


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