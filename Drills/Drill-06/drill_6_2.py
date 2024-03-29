from pico2d import *

import random

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def move(p1, p2, p3, p4):
    global frame
    global direction
    for i in range(0, 100, 2):
        t = i / 100
        cx = ((-(t + 0.01) ** 3 + 2 * (t + 0.01) ** 2 - (t + 0.01)) * p1[0] +
              (3 * (t + 0.01) ** 3 - 5 * (t + 0.01) ** 2 + 2) * p2[0] + (-3 * (t + 0.01) ** 3 +
               4 * (t + 0.01) ** 2 + (t + 0.01)) * p3[0] + ((t + 0.01) ** 3 - (t + 0.01) ** 2) * p4[0]) / 2
        x = ((-t ** 3 + 2 * t ** 2 - t) * p1[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p2[0] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p3[0] + (t ** 3 - t ** 2) * p4[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p1[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p2[1] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p3[1] + (t ** 3 - t ** 2) * p4[1]) / 2
        clear_canvas()
        handle_events()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        if cx > x:
            direction = 1
        elif cx < x:
            direction = 0

        character.clip_draw(frame * 100, 100 * direction, 100, 100, x, y)
        frame = (frame + 1) % 8
        delay(0.01)
        update_canvas()


def drill_6_8_1(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10):

    # draw p1-p2
    move(p10, p1, p2, p3)
    # draw p2-p3
    move(p1, p2, p3, p4)
    # draw p3-p4
    move(p2, p3, p4, p5)
    # draw p4-p5
    move(p3, p4, p5, p6)
    # draw p5-p6
    move(p4, p5, p6, p7)
    # draw p6-p7
    move(p5, p6, p7, p8)
    # draw p7-p8
    move(p6, p7, p8, p9)
    # draw p8-p9
    move(p7, p8, p9, p10)
    # draw p9-p10
    move(p8, p9, p10, p1)
    # draw p10-p1
    move(p9, p10, p1, p2)


open_canvas(KPU_WIDTH, KPU_HEIGHT)
running = True
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
direction = 1
frame = 0
p = [(random.randint(300, 800), random.randint(300, 800)) for i in range(10)]

while running:

    drill_6_8_1(p[0], p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9])


close_canvas()
