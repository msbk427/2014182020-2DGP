from pico2d import *

import random

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def drill_6_8_1(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10):
    global frame
    global direction
    # draw p1-p2
    for i in range(0, 50, 2):
        t = i / 100
        cx = (2 * (t + 1) ** 2 - 3 * (t + 1) + 1) * p1[0] + \
             (-4 * (t + 1) ** 2 + 4 * (t + 1)) * p2[0] + (2 * (t + 1) ** 2 - (t + 1)) * p3[0]
        x = (2 * t ** 2 - 3 * t + 1) * p1[0] + (-4 * t ** 2 + 4 * t) * p2[0] + (2 * t ** 2 - t) * p3[0]
        y = (2 * t ** 2 - 3 * t + 1) * p1[1] + (-4 * t ** 2 + 4 * t) * p2[1] + (2 * t ** 2 - t) * p3[1]
        clear_canvas()
        if cx > x:
            direction = 1
        elif cx < x:
            direction = 0
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        character.clip_draw(frame * 100, 100 * direction, 100, 100, x, y)
        frame = (frame + 1) % 8
        delay(0.05)
        update_canvas()
    # draw p2-p3
    for i in range(0, 100, 2):
        t = i / 100
        cx = ((-(t+1) ** 3 + 2 * (t+1) ** 2 - (t+1)) * p1[0] + (3 * (t+1) ** 3 - 5 * (t+1) ** 2 + 2) * p2[0] + (
                -3 * (t+1) ** 3 + 4 * (t+1) ** 2 + (t+1)) * p3[0] + ((t+1) ** 3 - (t+1) ** 2) * p4[0]) / 2
        x = ((-t ** 3 + 2 * t ** 2 - t) * p1[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p2[0] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p3[0] + (t ** 3 - t ** 2) * p4[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p1[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p2[1] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p3[1] + (t ** 3 - t ** 2) * p4[1]) / 2
        clear_canvas()
        if cx > x:
            direction = 1
        elif cx < x:
            direction = 0
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        character.clip_draw(frame * 100, 100 * direction, 100, 100, x, y)
        frame = (frame + 1) % 8
        delay(0.05)
        update_canvas()
    # draw p3-p4
    for i in range(0, 100, 2):
        t = i / 100
        cx = ((-(t + 1) ** 3 + 2 * (t + 1) ** 2 - (t + 1)) * p2[0] + (3 * (t + 1) ** 3 - 5 * (t + 1) ** 2 + 2) * p3[
            0] + (-3 * (t + 1) ** 3 + 4 * (t + 1) ** 2 + (t + 1)) * p4[0] + ((t + 1) ** 3 - (t + 1) ** 2) * p5[0]) / 2
        x = ((-t ** 3 + 2 * t ** 2 - t) * p2[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p3[0] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p4[0] + (t ** 3 - t ** 2) * p5[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p2[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p3[1] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p4[1] + (t ** 3 - t ** 2) * p5[1]) / 2
        clear_canvas()
        if cx > x:
            direction = 1
        elif cx < x:
            direction = 0
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        character.clip_draw(frame * 100, 100 * direction, 100, 100, x, y)
        frame = (frame + 1) % 8
        delay(0.05)
        update_canvas()
    # draw p4-p5
    for i in range(0, 100, 2):
        t = i / 100
        cx = ((-(t + 1) ** 3 + 2 * (t + 1) ** 2 - (t + 1)) * p3[0] + (3 * (t + 1) ** 3 - 5 * (t + 1) ** 2 + 2) * p4[
            0] + (-3 * (t + 1) ** 3 + 4 * (t + 1) ** 2 + (t + 1)) * p5[0] + ((t + 1) ** 3 - (t + 1) ** 2) * p6[0]) / 2
        x = ((-t ** 3 + 2 * t ** 2 - t) * p3[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p4[0] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p5[0] + (t ** 3 - t ** 2) * p6[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p3[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p4[1] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p5[1] + (t ** 3 - t ** 2) * p6[1]) / 2
        clear_canvas()
        if cx > x:
            direction = 1
        elif cx < x:
            direction = 0
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        character.clip_draw(frame * 100, 100 * direction, 100, 100, x, y)
        frame = (frame + 1) % 8
        delay(0.05)
        update_canvas()
    # draw p5-p6
    for i in range(0, 100, 2):
        t = i / 100
        cx = ((-(t + 1) ** 3 + 2 * (t + 1) ** 2 - (t + 1)) * p4[0] + (3 * (t + 1) ** 3 - 5 * (t + 1) ** 2 + 2) * p5[
            0] + (-3 * (t + 1) ** 3 + 4 * (t + 1) ** 2 + (t + 1)) * p6[0] + ((t + 1) ** 3 - (t + 1) ** 2) * p7[0]) / 2
        x = ((-t ** 3 + 2 * t ** 2 - t) * p4[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p5[0] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p6[0] + (t ** 3 - t ** 2) * p7[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p6[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p5[1] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p6[1] + (t ** 3 - t ** 2) * p7[1]) / 2
        clear_canvas()
        if cx > x:
            direction = 1
        elif cx < x:
            direction = 0
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        character.clip_draw(frame * 100, 100 * direction, 100, 100, x, y)
        frame = (frame + 1) % 8
        delay(0.05)
        update_canvas()
    # draw p6-p7
    for i in range(0, 100, 2):
        t = i / 100
        cx = ((-(t + 1) ** 3 + 2 * (t + 1) ** 2 - (t + 1)) * p5[0] + (3 * (t + 1) ** 3 - 5 * (t + 1) ** 2 + 2) * p6[
            0] + (-3 * (t + 1) ** 3 + 4 * (t + 1) ** 2 + (t + 1)) * p7[0] + ((t + 1) ** 3 - (t + 1) ** 2) * p8[0]) / 2
        x = ((-t ** 3 + 2 * t ** 2 - t) * p5[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p6[0] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p7[0] + (t ** 3 - t ** 2) * p8[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p5[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p6[1] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p7[1] + (t ** 3 - t ** 2) * p8[1]) / 2
        clear_canvas()
        if cx > x:
            direction = 1
        elif cx < x:
            direction = 0
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        character.clip_draw(frame * 100, 100 * direction, 100, 100, x, y)
        frame = (frame + 1) % 8
        delay(0.05)
        update_canvas()
    # draw p7-p8
    for i in range(0, 100, 2):
        t = i / 100
        cx = ((-(t + 1) ** 3 + 2 * (t + 1) ** 2 - (t + 1)) * p6[0] + (3 * (t + 1) ** 3 - 5 * (t + 1) ** 2 + 2) * p7[
            0] + (-3 * (t + 1) ** 3 + 4 * (t + 1) ** 2 + (t + 1)) * p8[0] + ((t + 1) ** 3 - (t + 1) ** 2) * p9[0]) / 2
        x = ((-t ** 3 + 2 * t ** 2 - t) * p6[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p7[0] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p8[0] + (t ** 3 - t ** 2) * p9[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p6[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p7[1] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p8[1] + (t ** 3 - t ** 2) * p9[1]) / 2
        clear_canvas()
        if cx > x:
            direction = 1
        elif cx < x:
            direction = 0
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        character.clip_draw(frame * 100, 100 * direction, 100, 100, x, y)
        frame = (frame + 1) % 8
        delay(0.05)
        update_canvas()
    # draw p8-p9
    for i in range(0, 100, 2):
        t = i / 100
        cx = ((-(t + 1) ** 3 + 2 * (t + 1) ** 2 - (t + 1)) * p7[0] + (3 * (t + 1) ** 3 - 5 * (t + 1) ** 2 + 2) * p8[
            0] + (-3 * (t + 1) ** 3 + 4 * (t + 1) ** 2 + (t + 1)) * p9[0] + ((t + 1) ** 3 - (t + 1) ** 2) * p10[0]) / 2
        x = ((-t ** 3 + 2 * t ** 2 - t) * p7[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p8[0] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p9[0] + (t ** 3 - t ** 2) * p10[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p7[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p8[1] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p9[1] + (t ** 3 - t ** 2) * p10[1]) / 2
        clear_canvas()
        if cx > x:
            direction = 1
        elif cx < x:
            direction = 0
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        character.clip_draw(frame * 100, 100 * direction, 100, 100, x, y)
        frame = (frame + 1) % 8
        delay(0.05)
        update_canvas()
    # draw p9-p10
    for i in range(0, 100, 2):
        t = i / 100
        cx = ((-(t + 1) ** 3 + 2 * (t + 1) ** 2 - (t + 1)) * p8[0] + (3 * (t + 1) ** 3 - 5 * (t + 1) ** 2 + 2) * p9[
            0] + (-3 * (t + 1) ** 3 + 4 * (t + 1) ** 2 + (t + 1)) * p10[0] + ((t + 1) ** 3 - (t + 1) ** 2) * p1[0]) / 2
        x = ((-t ** 3 + 2 * t ** 2 - t) * p8[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p9[0] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p10[0] + (t ** 3 - t ** 2) * p1[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p8[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p9[1] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p10[1] + (t ** 3 - t ** 2) * p1[1]) / 2
        clear_canvas()
        if cx > x:
            direction = 1
        elif cx < x:
            direction = 0
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        character.clip_draw(frame * 100, 100 * direction, 100, 100, x, y)
        frame = (frame + 1) % 8
        delay(0.05)
        update_canvas()
    # draw p10-p1
    for i in range(0, 100, 2):
        t = i / 100
        cx = ((-(t + 1) ** 3 + 2 * (t + 1) ** 2 - (t + 1)) * p9[0] + (3 * (t + 1) ** 3 - 5 * (t + 1) ** 2 + 2) * p10[
            0] + (-3 * (t + 1) ** 3 + 4 * (t + 1) ** 2 + (t + 1)) * p1[0] + ((t + 1) ** 3 - (t + 1) ** 2) * p2[0]) / 2
        x = ((-t ** 3 + 2 * t ** 2 - t) * p9[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p10[0] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p1[0] + (t ** 3 - t ** 2) * p2[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p9[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p10[1] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p1[1] + (t ** 3 - t ** 2) * p2[1]) / 2
        clear_canvas()
        if cx > x:
            direction = 1
        elif cx < x:
            direction = 0
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        character.clip_draw(frame * 100, 100 * direction, 100, 100, x, y)
        frame = (frame + 1) % 8
        delay(0.05)
        update_canvas()
    pass


open_canvas(KPU_WIDTH, KPU_HEIGHT)
running = True
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
direction = 1
frame = 0
points1 = [random.randint(300, 800), random.randint(300, 800)]
points2 = [random.randint(300, 800), random.randint(300, 800)]
points3 = [random.randint(300, 800), random.randint(300, 800)]
points4 = [random.randint(300, 800), random.randint(300, 800)]
points5 = [random.randint(300, 800), random.randint(300, 800)]
points6 = [random.randint(300, 800), random.randint(300, 800)]
points7 = [random.randint(300, 800), random.randint(300, 800)]
points8 = [random.randint(300, 800), random.randint(300, 800)]
points9 = [random.randint(300, 800), random.randint(300, 800)]
points10 = [random.randint(300, 800), random.randint(300, 800)]

while 1:
    drill_6_8_1(points1, points2, points3, points4, points5, points6, points7, points8, points9, points10)
