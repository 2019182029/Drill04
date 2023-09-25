# 1. 상하좌우 방향키를 이용하여 이동
# 2. 캐릭터가 작을 경우 확대

# 배경 : TUK_GROUND.png
# 캐릭터 : character.png

from pico2d import *

ground_width, ground_height = 1280, 1024
frame = 0

open_canvas(ground_width, ground_height)
ground = load_image('TUK_GROUND.png')
character = load_image('character.png')

def handle_events() :
    pass

while(1) :
    clear_canvas()
    ground.draw(ground_width // 2, ground_height // 2)
    character.clip_draw(frame * 64, 64, 64, 64, ground_width // 2, ground_height // 2)
    update_canvas()
    frame = (frame + 1) % 4
    delay(1)

close_canvas()