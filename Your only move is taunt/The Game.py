import pygame
import random

pygame.init()
pygame.mixer.init()  # для звука

W = 1400  # ширина игрового окна
H = 1000 # высота игрового окна
FPS = 60 # частота кадров в секунду

# Цвета (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
#Red
RED = (255, 0, 0)
DRED = (150, 0, 0)
WRED = (255, 150, 150)
#Green
GREEN = (0, 255, 0)
DGREEN = (0, 150, 0)
WGREEN = (150, 255, 150)
#Blue
BLUE = (0, 0, 255)
WBLUE = (150,150, 255)
DBLUE = (0, 0, 150)

#sc = pygame.display.set_mode((W, H))
sc = pygame.display.set_mode((W,H), pygame.FULLSCREEN | pygame.SCALED)
pygame.display.set_caption("Your only move is TAUNT")
clock = pygame.time.Clock()
f_sys = pygame.font.SysFont('comicsans', 60)


running = True
scene = "fight"

time_stop = True
frames_till_round_end = 1000
frames_till_turn_end = 0 #100
turns_till_end = 10
turn_frames_long = 10
nmove_frames_move = 0
Space_key_CD = 10

#Player variables
px,py,pvx,pvy = 150,10,0,0
pxn,pyn,pvxn,pvyn = px,py,pvx,pvy
Pcur_move,Pnext_move = 0,0


#Floor_Y = 750
def player_draw_sc():
    pygame.draw.rect(sc,DRED,(px,py,50,70))

def player_nmove_draw_sc():
    pygame.draw.rect(sc,(150,0,150),(pxn,pyn,50,70))

def update_player_pos():
    global px,py,pvx,pvy
    if py < 680:
        pvy += 1
    else:
        py = 680
        pvy = 0

    if pvx != 0:
        if pvx > 0:
            pvx -= 1
        else:
            pvx += 1

    py += pvy
    px += pvx
def update_nmove_player_pos():
    global pxn,pyn,pvxn,pvyn
    if pyn < 680:
        pvyn += 1
    else:
        pyn = 680
        pvyn = 0

    if pvxn != 0:
        if pvxn > 0:
            pvxn -= 1
        else:
            pvxn += 1
    pyn += pvyn
    pxn += pvxn
def draw_bar_select_UI():
    pygame.draw.rect(sc,BLACK,(0,H-200,W//2,H-200))
    pygame.draw.rect(sc,WHITE,(-3,H-200,W//2+3,H-200),3)

while running:
    while scene == "fight": #Main_menu
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        bt = pygame.key.get_pressed()
        if bt[pygame.K_ESCAPE]:
            exit()
        if bt[pygame.K_SPACE] and Space_key_CD <= 0:
            time_stop = False
            turns_till_end -= 1
            Space_key_CD = 105
            frames_till_turn_end = 0
            pxn,pyn,pvxn,pvyn = px,py,pvx,pvy

        sc.fill(DBLUE)

        pygame.draw.line(sc,WBLUE,(0,H-250+2.5),(W,H-250+2.5),5)
        if time_stop == True:
            nmove_frames_move += 1
            if nmove_frames_move >= turn_frames_long:
                pxn,pyn,pvxn,pvyn = px,py,pvx,pvy
                nmove_frames_move = 0
            player_nmove_draw_sc()
            update_nmove_player_pos()

        if time_stop == False:
            update_player_pos()

        player_draw_sc()

        draw_bar_select_UI()


        f_sys = pygame.font.SysFont('comicsans', 60)
        txt_sc = f_sys.render(f"{frames_till_round_end}", True, WHITE)
        sc.blit(txt_sc, (W//2,25))
        txt_sc = f_sys.render(f"{turns_till_end}", True, WHITE)
        sc.blit(txt_sc, (W//2,95))
        txt_sc = f_sys.render(f"{Space_key_CD}", True, WHITE)
        sc.blit(txt_sc, (W//2,95+70))

        f_sys = pygame.font.SysFont('comicsans', 20)
        txt_sc = f_sys.render(f"{pxn,pyn,pvxn,pvyn}", True, (255,150,150))
        sc.blit(txt_sc, (10,H//2))
        txt_sc = f_sys.render(f"{px,py,pvx,pvy}", True, (255,100,100))
        sc.blit(txt_sc, (10,H//2-35))
        pygame.display.update()
        clock.tick(FPS)

        if time_stop == False and turn_frames_long > frames_till_turn_end:
            frames_till_round_end -= 1
            frames_till_turn_end += 1
        else:
            time_stop = True

        Space_key_CD -= 1