# 상하좌우 방향키를 이용하여 이동

from pico2d import *

ground_width, ground_height = 1280, 1024
running= True
keydown = 0                                     # keydown이 0이라면 애니메이션이, !0이라면 정지된 캐릭터가 출력된다.
frame, yframe = 0, 192                          # yframe은 이동하는 방향에 따라 캐릭터가 향하는 방향 또한 바뀌도록 한다. 
x, y = ground_width // 2, ground_height // 2
xdir, ydir = 0, 0

open_canvas(ground_width, ground_height)
ground = load_image('TUK_GROUND.png')
character = load_image('character.png')

def handle_events() :
    global running
    global keydown
    global xdir, ydir

    events = get_events()
    for event in events :
        if (event.type == SDL_QUIT) :
            running = False
        elif (event.type == SDL_KEYDOWN) :
            if (event.key == SDLK_UP) :
                keydown += 1
                ydir += 1
            if (event.key == SDLK_RIGHT) :
                keydown += 1
                xdir += 1
            if (event.key == SDLK_LEFT) :
                keydown += 1
                xdir -= 1
            if (event.key == SDLK_DOWN) :
                keydown += 1
                ydir -= 1
            if (event.key == SDLK_ESCAPE) :
                running = False 
        elif (event.type == SDL_KEYUP) :
            if (event.key == SDLK_UP) :
                keydown -= 1
                ydir -= 1
            if (event.key == SDLK_RIGHT) :
                keydown -= 1
                xdir -= 1
            if (event.key == SDLK_LEFT) :
                keydown -= 1
                xdir += 1
            if (event.key == SDLK_DOWN) :
                keydown -= 1
                ydir += 1

while(running) :
    clear_canvas()
    ground.draw(ground_width // 2, ground_height // 2)
    character.clip_draw(frame * 64, yframe, 64, 64, x, y, 196, 196)
    update_canvas()
    handle_events()

    x += xdir * 10
    y += ydir * 10

    if (keydown != 0 and (xdir != 0 or ydir != 0)) :        # keydown != 0이고 반대 방향키를 동시에 누르는 것이 아니라면 캐릭터가 움직인다.
        frame = (frame + 1) % 4
        if(xdir > 0) :                # 캐릭터의 이동 방향에 따라
            yframe = 64               # 캐릭터가 보는 방향이 달라진다.
        elif(xdir < 0) :
            yframe = 128
        if(ydir > 0) :
            yframe = 0
        elif(ydir < 0) :
            yframe = 192

        if (x <= 0) :                 # 화면 경계선에다다르면
            x = 0                     # 더 이상 진행하지 않는다.
        elif (x >= ground_width) :
            x = ground_width
        if (y <= 0) :
            y = 0
        elif (y >= ground_height) :
            y = ground_height
    else :                            # keydown == 0이거나 반대 방향키를 동시에 누르면 정지된 캐릭터가 출력된다.
        frame = 0
    delay(0.1)

close_canvas()