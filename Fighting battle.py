import pygame
import random
import math
#from Earthhelper import *
#
W = 1200
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
can_jump = False

#Player
Player_X = 150
Player_Y = 400
VelPlayer_Y = 0
VelPlayer_X = 0
Player_W = 75
Player_H = 130
Player_speed = 4.5
Player_stun_time = 0
VelDashPlayer_X = 0
Dash_player_CD = 150
Look_dir_player = 1
Hitbox_type = 0
Player_state = "Normal"

PUNCH_TEST_hitbox = pygame.Rect(W-250, 400, 100, 100)

#0 none
#1 punch_normal
#2 punch_s_var
#3 punch_air_var

#Enemy
Enemy_X = 250
Enemy_Y = 100
VelEnemy_Y = 0
VelEnemy_X = 0

def num_change_vel_etc():
    global Player_X,Player_Y,VelPlayer_Y,VelPlayer_X,can_jump, VelDashPlayer_X
    if VelDashPlayer_X == 0:
        if VelPlayer_X > 0:
            VelPlayer_X -= 0.25
        if VelPlayer_X < 0:
            VelPlayer_X += 0.25
    else:
        Player_X += VelDashPlayer_X
        if VelDashPlayer_X > 0:
            VelDashPlayer_X -= 0.5
        if VelDashPlayer_X < 0:
            VelDashPlayer_X += 0.5
        VelPlayer_Y = 1
    if Player_Y <= (H-250) - Player_H - 8:
        VelPlayer_Y += 0.1
    else:
        VelPlayer_Y = 0
        can_jump = True
        Player_Y = (H-250) - Player_H - 8
    Player_X += VelPlayer_X
    Player_Y += VelPlayer_Y



def draw_player_on_screen_collision():
    global Player_X,Player_Y,VelPlayer_Y,VelPlayer_X,Player_crouch

    pygame.draw.rect(sc,RED,(Player_collision))

    if Player_crouch == False:
        pygame.draw.rect(sc, BLUE, (Player_X,Player_Y,Player_W,Player_H))
    else:
        pygame.draw.rect(sc, BLUE, (Player_X,Player_Y+(Player_H//2),Player_W,Player_H//2))


def draw_map():
    pygame.draw.line(sc,WHITE,(0,H-250),(W,H-250),15)



def display_info_player():
    #global Player_X,Player_Y,Player_stun_time,VelPlayer_Y,VelPlayer_X,Dash_player_CD

    txt_surf = f_sys.render(f"Stun {Player_stun_time}", True, RED)
    sc.blit(txt_surf, (Player_X-(Player_W//2),Player_Y))
    txt_surf = f_sys.render(f"VY {VelPlayer_Y}", True, RED)
    sc.blit(txt_surf, (Player_X-(Player_W//2),Player_Y-35))
    txt_surf = f_sys.render(f"VX {VelPlayer_X}", True, RED)
    sc.blit(txt_surf, (Player_X-(Player_W//2),Player_Y-70))
    txt_surf = f_sys.render(f"DashCD {Dash_player_CD}", True, RED)
    sc.blit(txt_surf, (Player_X-(Player_W//2),Player_Y-105))
    txt_surf = f_sys.render(f"DashCD {Player_state}", True, RED)
    sc.blit(txt_surf, (Player_X-(Player_W//2),Player_Y-140))


while running:
    while Scene == 1:
        Player_collision = pygame.Rect(Player_X, Player_Y, Player_W, Player_H)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        bt = pygame.key.get_pressed()
        if bt[pygame.K_ESCAPE]:
            exit()

        if bt[pygame.K_a] and VelDashPlayer_X == 0 and Player_crouch == False:
            VelPlayer_X = -Player_speed
            Look_dir_player = 0
        if bt[pygame.K_d] and VelDashPlayer_X == 0 and Player_crouch == False:
            VelPlayer_X = Player_speed
            Look_dir_player = 1
        if bt[pygame.K_q] and Dash_player_CD <= 0:
            Dash_player_CD = 150
            if Look_dir_player == 0:
                VelDashPlayer_X = -19
            else:
                VelDashPlayer_X = 19
        if bt[pygame.K_w] and can_jump == True:
            VelPlayer_Y = -5.5
            Player_Y -= 1
            can_jump = False
        if bt[pygame.K_s] and (Player_state == "Normal" or Player_state == "Crouch"):
            Player_crouch = True
        else:
            Player_crouch = False

        sc.fill(DBLUE)



        pygame.draw.rect(sc,RED,(PUNCH_TEST_hitbox))
        draw_map()
        draw_player_on_screen_collision()
        num_change_vel_etc()
        display_info_player()

        if VelDashPlayer_X == 0:
            if VelPlayer_Y < 0:
                Player_state = "Air (up)"
            elif VelPlayer_Y > 0.1:
                Player_state = "Air (falling)"
            elif VelPlayer_Y == 0 and Player_crouch == False:
                Player_state = "Normal"
            elif Player_crouch == True:
                Player_state = "Crouch"
        else:
            Player_state = "Dashing"
        pygame.display.update()
        clock.tick(FPS)
        if VelDashPlayer_X == 0:
            Dash_player_CD -= 1