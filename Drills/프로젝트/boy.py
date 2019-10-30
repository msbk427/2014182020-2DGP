from pico2d import *

import game_world

# Boy Event
UP, DOWN, LEFT, RIGHT = range(4)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT,
    (SDL_KEYDOWN, SDLK_UP): UP,
    (SDL_KEYDOWN, SDLK_DOWN): DOWN
}


# Boy States

class IdleState:

    @staticmethod
    def enter(boy, event):
        if event == UP:
            boy.y += 50
        elif event == DOWN:
            boy.y -= 50
        elif event == RIGHT:
            boy.x += 50
        elif event == LEFT:
            boy.x -= 50
        boy.x = clamp(50, boy.x, 750)
        boy.y = clamp(50, boy.y, 750)

    @staticmethod
    def exit(boy, event):

        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % 8
        # fill here

    @staticmethod
    def draw(boy):
        boy.image.clip_draw(boy.frame * 12, 18, 12, 18, boy.x, boy.y, 50, 50)


next_state_table = {
    IdleState: {UP: IdleState, DOWN: IdleState,
                LEFT: IdleState, RIGHT: IdleState}
}


class Boy:

    def __init__(self):
        self.x, self.y = 100, 100
        self.image = load_image('warrior.png')
        self.dir = 1
        self.frame = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

    def attack(self):

        pass

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
