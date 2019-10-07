from pico2d import *

open_canvas()

import os
os.chdir('D:\\2014182020MinsukBaek\\2DGP\Labs\\Lecture04')

grass=load_image('grass.png')
character=load_image('character.png')

grass.draw_now(400,30)
character.draw_now(400,90)

delay(5)

close_canvas()
