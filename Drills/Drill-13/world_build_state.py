import random
import json
import pickle
import os

from pico2d import *
import game_framework
import game_world

import main_state

from boy import Boy
from zombie import Zombie


boy = None


name = "WorldBuildState"

menu = None

def enter():
    global menu
    menu = load_image('menu.png')
    hide_cursor()
    hide_lattice()

def exit():
    global menu
    del menu

def pause():
    pass

def resume():
    pass

def get_boy():
    return boy



def create_new_world():
    global boy
    global zombie
    boy = Boy()
    game_world.add_object(boy, 1)

    with open('zombie_data.json', 'r') as f:
        zomebie_data_list = json.load(f)

    for data in zomebie_data_list:
        zombie = Zombie(data['name'], data['x'], data['y'], data['size'])
        game_world.add_object(zombie, 1)




def load_saved_world():
    global boy

    game_world.load()
    for o in game_world.all_objects():
        if isinstance(o, Boy):
            boy = o
            break;



def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_n:
            create_new_world()
            game_framework.change_state(main_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_l:
            load_saved_world()
            game_framework.change_state(main_state)

def update():
    pass

def draw():
    clear_canvas()
    font = load_font('ENCR10B.TTF', 40)
    for i in range(10):
        font.draw(get_canvas_width()//2 - 200, 900 - i*30, '(Rank %d : %3.2f )' % (i+1, game_world.ranking[i]), (0, 0, 0))
    menu.draw(get_canvas_width()//2, get_canvas_height()//2 - 200)
    update_canvas()






