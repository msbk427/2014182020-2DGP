from pico2d import *


class Grass:

    image = None

    def __init__(self):
        if Grass.image is None:
            Grass.image = load_image('tiles_caves.png')

    def update(self):
        pass

    def draw(self):
        size = 10*10
        fx, fy = 100, 100
        for i in range(0, 10):
            fx = fx + 16
            self.image.clip_draw(0, 240, 16, 16, fx, 100)
            fy = fy + 16
            self.image.clip_draw(0, 240, 16, 16, 100, fy)
