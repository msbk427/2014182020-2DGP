from pico2d import *
import main_state
import random


class Monster:

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.frame = 0
        self.frame_count = 0
        self.move_count = 0
        self.hp = 10
        self.move_logic = 0
        self.image = load_image('monster.png')

    def update(self):
        self.frame_count += 1
        if self.frame_count > 70:
            self.frame = (self.frame + 1) % 5
            self.frame_count = 0
        self.move_count += 1
        if self.move_count > 300:
            self.move_logic = random.randint(0, 1)
            if self.move_logic == 1:
                if main_state.boy.x > self.x:
                    self.x = self.x + 50
                elif main_state.boy.x < self.x:
                    self.x = self.x - 50
                elif main_state.boy.y > self.y:
                    self.y = self.y + 50
                elif main_state.boy.y < self.y:
                    self.y = self.y - 50
            elif self.move_logic == 0:
                if main_state.boy.y > self.y:
                    self.y = self.y + 50
                elif main_state.boy.y < self.y:
                    self.y = self.y - 50
                elif main_state.boy.x > self.x:
                    self.x = self.x + 50
                elif main_state.boy.x < self.x:
                    self.x = self.x - 50
            self.move_count = 0

    def draw(self):
        self.image.clip_draw(self.frame * 12, 0, 13, 16, self.x, self.y, 50, 50)
