from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def handle_events():
    global running
    global x, y
    global cx, cy
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, KPU_HEIGHT - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            cx, cy = event.x, KPU_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
cursor = load_image('hand_arrow.png')


running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
cx, cy = KPU_WIDTH // 2, KPU_HEIGHT // 2
ci_x, ci_y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
i, t = 0, 0
direction = 1
hide_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    cursor.draw(x, y)

    if ci_x >= cx:
        direction = 0
    else:
        direction = 1

    i = (i + 1) % 100
    t = i / 100
    ci_x = (1 - t) * ci_x + t * cx
    ci_y = (1 - t) * ci_y + t * cy
    character.clip_draw(frame * 100, 100 * direction, 100, 100, ci_x, ci_y)

    update_canvas()

    handle_events()
    frame = (frame + 1) % 8
    delay(0.05)


close_canvas()




