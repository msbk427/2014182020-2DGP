from pico2d import *


class Map:
    count = 0
    image = None

    def __init__(self):
        if Map.image is None:
            Map.image = load_image('tiles_caves.png')

    def update(self):
        pass

    def draw(self):
        size = 16
        count = 0
        count2 = 0
        fx = 0
        fy = 0
        while count <= size:
            while count2 <= size:
                self.image.clip_draw(0, 240, 16, 16, fx, fy, 50, 50)
                fy = fy + 50
                count2 = count2 + 1
            count2 = 0
            fy = 0
            fx = fx + 50
            count = count + 1


