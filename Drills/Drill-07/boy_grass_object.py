from pico2d import *
import random

ground = 60
left_end = 0
right_end = 800


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

    pass


class S_Ball:
    def __init__(self):
        self.x, self.y = random.randint(0, 700), 599
        self.image = load_image('ball21x21.png')

    def update(self):
        if self.y <= ground:
            self.y = ground

        elif self.y > ground:
            self.y -= random.randint(1, 15)
        pass

    def draw(self):
        self.image.draw(self.x, self.y)


class B_Ball:
    def __init__(self):
        self.x, self.y = random.randint(0, 700), 599
        self.image = load_image('ball41x41.png')

    def update(self):
        if self.y <= ground:
            self.y = ground

        elif self.y > ground:
            self.y -= random.randint(1, 15)
        pass

    def draw(self):
        self.image.draw(self.x, self.y)


class Boy:
    def __init__(self):
        self.x, self.y = random.randint(0, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        if self.x >= right_end:
            self.x = right_end
        elif self.x <= left_end:
            self.x = left_end
        else:
            self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


running = True
open_canvas()
bb_count = random.randint(1, 25)
sb_count = random.randint(1, 25)
b_team = [B_Ball() for i in range(bb_count)]
s_team = [S_Ball() for i in range(sb_count)]
team = [Boy() for i in range(11)]
grass = Grass()
while running:
    clear_canvas()
    handle_events()
    for boy in team:
        boy.draw()
        boy.update()
    for ball in b_team:
        ball.draw()
        ball.update()
    for ball in s_team:
        ball.draw()
        ball.update()
    grass.draw()
    update_canvas()
    delay(0.02)


close_canvas()

