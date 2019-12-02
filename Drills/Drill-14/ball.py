from pico2d import *
import random
import game_framework
import game_world

WIDTH, HEIGHT = 1837, 1109

class Ball:

    image = None

    def __init__(self):
        if Ball.image==None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y = random.randint(100, WIDTH - 100), random.randint(100, HEIGHT - 1)

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def update(self):
        pass

    def draw(self):
        cx, cy = self.x - self.bg.window_left, self.y - self.bg.window_bottom
        self.image.draw(cx, cy)
        #draw_rectangle(*self.get_bb())

    def handle_event(self, event):
        pass

    def set_background(self, bg):
        self.bg = bg