from pico2d import *
import game_framework
import main_state


name = "PauseState"


def enter():
    global image
    image = load_image('pause.png')
    pass


def exit():
    global image
    del image
    pass


def pause():
    pass


def resume():
    pass


def draw():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT():
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.pop_state()
    pass


def update():
    pass
