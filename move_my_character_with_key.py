# 1. 상하좌우 방향키를 이용하여 이동
# 2. 캐릭터가 작을 경우 확대

# 배경 : TUK_GROUND.png
# 캐릭터 : character.png

from pico2d import *

ground_width, ground_height = 1280, 1024
running = True
frame = 0
x, y = ground_width // 2, ground_height // 2
xdir, ydir = 0, 0

open_canvas(ground_width, ground_height)
ground = load_image('TUK_GROUND.png')
character = load_image('character.png')

def handle_events() :
    global running
    global xdir, ydir
    events = get_events()
    for event in events :
        if (event.type == SDL_QUIT) :
            running = False
        elif (event.type == SDL_KEYDOWN) :
            if (event.key == SDLK_LEFT) :
                xdir -= 1
            if (event.key == SDLK_ESCAPE) :
                running = False 
        elif (event.type == SDL_KEYUP) :
            if (event.key == SDLK_LEFT) :
                xdir += 1

while(running) :
    clear_canvas()
    ground.draw(ground_width // 2, ground_height // 2)
    character.clip_draw(frame * 64, 0, 64, 64, x, y)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 4
    x += xdir * 5
    delay(0.1)

close_canvas()