from pico2d import *

open_canvas()
grass = load_image('grass.png')
character = load_image('run_animation.png')

x = 0
frame = 0
while x < 800:
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 0, 100, 100, x, 85)
    # clip_draw(left,bottom,width,height,x,y), png 파일에서의 이미지 위치
    update_canvas()
    frame = (frame + 1) % 8
    x += 9
    delay(0.04)
    get_events()

close_canvas()
