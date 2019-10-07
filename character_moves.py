from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

a=0

while(a<800):
    clear_canvas_now()
    x = math.sin(a/180*math.pi)
    y = math.cos(a/180*math.pi)
    grass.draw_now(400,30)
    character.draw_now(400+x*200,260+y*200)
    a=a+2
    delay(0.01)
    
close_canvas()
