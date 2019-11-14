from pico2d import *
import game_framework


class Brick:
    def __init__(self):
        self.image = load_image('brick180x40.png')
        self.x = 350
        self.y = 250
        self.speed = 150

    def update(self):
        self.x += self.speed * game_framework.frame_time
        if self.x > 1600:
            self.speed *= -1
        elif self.x < 0:
            self.speed *= -1

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 90, self.y - 20, self.x + 90, self.y + 20
