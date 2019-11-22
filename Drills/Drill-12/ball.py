from pico2d import *
import random
import game_framework
import game_world


class Ball:

    image = None

    def __init__(self):
        if Ball.image==None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y = random.randint(0, 1600 - 1),random.randint(0, 1024 - 1)

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def handle_event(self, event):
        pass

class BigBall:
    image = None

    def __init__(self):
        if BigBall.image == None:
            BigBall.image = load_image('ball41x41.png')
        self.x, self.y = random.randint(0, 1600 - 1), random.randint(0, 1024 - 1)

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def handle_event(self, event):
        pass