import game_framework
from pico2d import *
import main_state


name = "PauseState"
image = None
stock = 0.0


def enter():
    global image
    image = load_image('pause.png')


def exit():
    global image
    del image


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if event.type == SDL_KEYDOWN and event.key == SDLK_p:
                game_framework.pop_state()


def draw():
    global stock
    clear_canvas()
    main_state.pause()
    if stock % 2 < 1:
        image.draw(400, 300, 100, 100)
    stock = stock + 0.01
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass