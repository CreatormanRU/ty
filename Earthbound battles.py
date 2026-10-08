import pygame
import random
import math
#from Earthhelper import *
#
W = 1430
H = 805

W = 900
H = 900

#tick_speed = int(input())
sc = pygame.display.set_mode((W,H), pygame.FULLSCREEN | pygame.SCALED)


pygame.mixer.pre_init(44100, -16, 1, 512)
# Инициализация pygame
pygame.init()

f_sys = pygame.font.SysFont('comicsans', 30)

pygame.display.set_caption("Earthbound")
FPS = 60       # число кадров в секунду
clock = pygame.time.Clock()
RED = (255,0,0)
DRED = (100,0,0)
BLUE = (0,0,255)
DBLUE = (0,0,100)
BLUEYAN = (75,75,175)
GREEN = (0,255,0)
BLACK = (0,0,0)
WHITE = (255,255,255)
GRAY = (100,100,100)
DGRAY = (50,50,50)
YELLOW = (242, 198, 0)
PURPLE = (155,0,155)
#extra important!
running = True
Scene = 1
window_X = 10
window_Y = 10
window_W = 225
window_H = 240

W_Select_menu = 0
H_Select_menu = 0
Window_type = "normal"
tick = 0
Window_Selected = 1
Player_which = 1
Player_turn = True
Window_which = 1


#Player 1
p1_HP,p1_SP,p1_effect,p1_state = 100,110,0,0
#Player 2
p2_HP,p2_SP,p2_effect,p2_state = 120,100,0,0
#Player 3
p3_HP,p3_SP,p3_effect,p3_state = 140,80,0,0
#Player 4
p4_HP,p4_SP,p4_effect,p4_state = 90,150,0,0

Window_Select_Menu_part = 1

def draw_enemy():
    pygame.draw.rect(sc,RED,(W//2-100,150,200,300))

def draw_select_window():
    global sc, H, W
    global window_X,window_Y,window_W,window_H,Window_Selected
    global Player_which

    #Player info
    global Window_Select_Menu_part #P1 status

    #                          x   y    w   h
    pygame.draw.rect(sc,BLACK,(window_X,(H-window_H)-window_Y,window_W,window_H))

    pygame.draw.rect(sc,WHITE,(window_X,(H-window_H)-window_Y,window_W,window_H),5)
    f_sys = pygame.font.SysFont('comicsans', 30)

    #WINDOW SELECT WHAT TO DO
    if Window_Select_Menu_part == 1:
        f_sys = pygame.font.SysFont('comicsans', 40)
        #ATTACK
        if W_Select_menu == 0 and H_Select_menu == 0:
            txt_surf = f_sys.render("Attack", True, GREEN)
        else:
            txt_surf = f_sys.render("Attack", True, WHITE)
        sc.blit(txt_surf, (window_X+10,(H-window_Y-window_H)+15))
        #SPELL
        if W_Select_menu == 0 and H_Select_menu == 1:
            txt_surf = f_sys.render("Spells", True, GREEN)
        else:
            txt_surf = f_sys.render("Spells", True, WHITE)
        sc.blit(txt_surf, (window_X+10,(H-window_Y-window_H)+155))
        #ITEM
        if W_Select_menu == 1 and H_Select_menu == 0:
            txt_surf = f_sys.render("Items", True, GREEN)
        else:
            txt_surf = f_sys.render("Items", True, WHITE)
        sc.blit(txt_surf, (window_X+W//2,(H-window_Y-window_H)+15))
        #Defend
        if W_Select_menu == 1 and H_Select_menu == 1:
            txt_surf = f_sys.render("Defend", True, GREEN)
        else:
            txt_surf = f_sys.render("Defend", True, WHITE)
        sc.blit(txt_surf, (window_X+W//2,(H-window_Y-window_H)+155))

def draw_window():
    global sc, H, W
    global window_X,window_Y,window_W,window_H

    #Player info
    global Window_HP,Window_SP,Window_effect,Window_state
    global Window_Selected,Player_which,Window_which #P1 status
    #BOX
    #                          x   y    w   h
    pygame.draw.rect(sc,BLACK,(window_X,(H-window_H)-window_Y,window_W,window_H))
    if Window_Selected == Player_which == Window_which:
        pygame.draw.rect(sc,GREEN,(window_X,(H-window_H)-window_Y,window_W,window_H),5)
    else:
        pygame.draw.rect(sc,WHITE,(window_X,(H-window_H)-window_Y,window_W,window_H),5)

    #MAIN INFO
    f_sys = pygame.font.SysFont('comicsans', 30)
    txt_surf = f_sys.render(f"HP:{Window_HP}", True, WHITE)
    sc.blit(txt_surf, (window_X+10,(H-window_Y-window_H)))
    txt_surf = f_sys.render(f"SP:{Window_SP}", True, WHITE)
    sc.blit(txt_surf, (window_X+10,(H-window_Y-window_H)+45))
    if Window_effect == 0:
        txt_surf = f_sys.render("Nothing", True, WHITE)
    elif Window_effect == 1:
        txt_surf = f_sys.render("Bleeding", True, DRED)

    sc.blit(txt_surf, (window_X+10,(H-window_Y-window_H)+90))

    if Window_state == 0:
        txt_surf = f_sys.render("Does: Nothing", True, WHITE)
    elif Window_state == 1:
        txt_surf = f_sys.render("Does: Bash", True, WHITE)
    sc.blit(txt_surf, (window_X+10,(H-window_Y-window_H)+130))
    if 1 == 2:
        txt_surf = f_sys.render(f"window{Window_which}", True, GREEN)
        sc.blit(txt_surf, (window_X+10,(H-window_Y-window_H)+200))
        txt_surf = f_sys.render(f"P_which{Player_which}", True, GREEN)
        sc.blit(txt_surf, (window_X+10,(H-window_Y-window_H)+160))
        txt_surf = f_sys.render(f"W_sel{Window_Selected}", True, GREEN)
        sc.blit(txt_surf, (window_X+10,(H-window_Y-window_H)+120))
def draw_info():
    if tick == 1:
        txt_surf = f_sys.render(f"tick:{tick}", True, RED)
    else:
        txt_surf = f_sys.render(f"tick:{tick}", True, GREEN)
    sc.blit(txt_surf, (10,10))

    txt_surf = f_sys.render(f"W_sel {W_Select_menu}/ H_sel {H_Select_menu}", True, GREEN)
    sc.blit(txt_surf, (10,40))
    txt_surf = f_sys.render(f"Window_type {Window_type}", True, GREEN)
    sc.blit(txt_surf, (10,70))





def draw_window_all():
    global sc, H, W
    global window_X,window_Y,window_W,window_H
    global Window_HP,Window_SP,Window_effect,Window_state
    #player info
    global p1_HP,p1_SP,p1_effect,p1_state
    global p2_HP,p2_SP,p2_effect,p2_state
    global p3_HP,p3_SP,p3_effect,p3_state
    global p4_HP,p4_SP,p4_effect,p4_state
    global Window_which

    window_X,window_Y,window_W,window_H,Window_which = 15,10,210,240,1
    Window_HP,Window_SP,Window_effect,Window_state = p1_HP, p1_SP, p1_effect, p1_state
    draw_window()

    window_X,window_Y,window_W,window_H,Window_which = window_W+window_X+10,10,210,240,2
    Window_HP,Window_SP,Window_effect,Window_state = p2_HP, p2_SP, p2_effect, p2_state
    draw_window()

    window_X,window_Y,window_W,window_H,Window_which = window_W+window_X+10,10,210,240,3
    Window_HP,Window_SP,Window_effect,Window_state = p3_HP, p3_SP, p3_effect, p3_state
    draw_window()

    window_X,window_Y,window_W,window_H,Window_which = window_W+window_X+10,10,210,240,4
    Window_HP,Window_SP,Window_effect,Window_state = p4_HP, p4_SP, p4_effect, p4_state
    draw_window()



def draw_window_select_config():
    global sc, H, W
    global window_X,window_Y,window_W,window_H


    window_X,window_Y,window_W,window_H = 10,10,W-20,240
    draw_select_window()

while running:
    while Scene == 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        bt = pygame.key.get_pressed()
        if bt[pygame.K_ESCAPE]:
            exit()
        if Player_turn == True:
            if bt[pygame.K_w] and tick == 1 and H_Select_menu != 0:
                H_Select_menu -= 1
            if bt[pygame.K_s] and tick == 1 and H_Select_menu != 1:
                H_Select_menu += 1
            if bt[pygame.K_a] and tick == 1 and W_Select_menu != 0:
                W_Select_menu -= 1
            if bt[pygame.K_d] and tick == 1 and W_Select_menu != 1:
                W_Select_menu += 1
            if bt[pygame.K_q] and tick == 1:
                Window_type = "select"
                W_Select_menu = 0
                H_Select_menu = 0
                Window_Select_Menu_part = 1
            if bt[pygame.K_e] and tick == 1:
                if Window_type == "select":
                    if W_Select_menu == 0 and H_Select_menu == 0 and Window_Selected == 1:
                        p1_state = 1
                        Window_type = "normal"
                    if W_Select_menu == 0 and H_Select_menu == 0 and Window_Selected == 2:
                        p2_state = 1
                        Window_type = "normal"
                    if W_Select_menu == 0 and H_Select_menu == 0 and Window_Selected == 3:
                        p3_state = 1
                        Window_type = "normal"
                    if W_Select_menu == 0 and H_Select_menu == 0 and Window_Selected == 4:
                        p4_state = 1
                        Window_type = "normal"


            if bt[pygame.K_SPACE] and tick == 1 and Window_type == "normal":
                Player_which += 1
                Window_Selected += 1
                if Player_which == 5:
                    Player_turn = False


        sc.fill(BLUEYAN)

        draw_enemy()

        if Window_type == "normal":
            draw_window_all()
        if Window_type == "select":
            draw_window_select_config()
        draw_info()



        pygame.display.update()
        clock.tick(FPS)
        tick -= 1
        if tick <= 0:
            tick = 10