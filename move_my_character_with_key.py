# 상하좌우 방향키를 이용하여 이동

from pico2d import *

ground_width, ground_height = 1280, 1024
running, keydown = True, False                  # keydown이 True라면 애니메이션이, False라면 정지된 캐릭터가 출력된다.
frame, yframe = 0, 192                          # yframe은 이동하는 방향에 따라 캐릭터가 향하는 방향 또한 바뀌도록 한다. 
x, y = ground_width // 2, ground_height // 2
xdir, ydir = 0, 0

open_canvas(ground_width, ground_height)
ground = load_image('TUK_GROUND.png')
character = load_image('character.png')

def handle_events() :
    global running, keydown
    global xdir, ydir
    global yframe
    events = get_events()
    for event in events :
        if (event.type == SDL_QUIT) :
            running = False
        elif (event.type == SDL_KEYDOWN) :
            keydown = True
            if (event.key == SDLK_LEFT) :
                xdir -= 1
                yframe = 128
            if (event.key == SDLK_RIGHT) :
                xdir += 1
                yframe = 64
            if (event.key == SDLK_DOWN) :
                ydir -= 1
                yframe = 192
            if (event.key == SDLK_UP) :
                ydir += 1
                yframe = 0
            if (event.key == SDLK_ESCAPE) :
                running = False 
        elif (event.type == SDL_KEYUP) :
            keydown = False
            if (event.key == SDLK_LEFT) :
                xdir += 1
                yframe = 128
            if (event.key == SDLK_RIGHT) :
                xdir -= 1
                yframe = 64
            if (event.key == SDLK_DOWN) :
                ydir += 1
                yframe = 192
            if (event.key == SDLK_UP) :
                ydir -= 1
                yframe = 0

while(running) :
    clear_canvas()
    ground.draw(ground_width // 2, ground_height // 2)
    character.clip_draw(frame * 64, yframe, 64, 64, x, y, 196, 196)
    update_canvas()
    handle_events()
    if (keydown == True) :
        frame = (frame + 1) % 4
    else :
        frame = 0
    x += xdir * 5
    y += ydir * 5
    delay(0.1)

close_canvas()