import pygame
import random

pygame.init()
pygame.mixer.init()  # для звука

W = 1400  # ширина игрового окна
H = 900 # высота игрового окна
FPS = 120 # частота кадров в секунду

# Цвета (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
#Red
RED = (255, 0, 0)
#Green
GREEN = (0, 255, 0)
#Blue
BLUE = (0, 0, 255)
WBLUE = (150,150, 255)
DBLUE = (0, 0, 150)

#sc = pygame.display.set_mode((W, H))
sc = pygame.display.set_mode((W,H), pygame.FULLSCREEN | pygame.SCALED)
pygame.display.set_caption("Colorful world")
clock = pygame.time.Clock()

running = True
scene = "Main menu"

Toon_selected = 0
#OBJ_PLAYER
Obj_player_anim_walk_timer = 15
Obj_player_anim_abilities_timer = 2


#        sc_text = f_sys.render("Song: Final Destination 0%", 3, BLACK)
#    pos = sc_text.get_rect(center=(0+250, 0+175))
#            SPACE_PRESS_NOW_spr.set_colorkey((0, 155, 0))
#            sc.blit(BF_idle_spr,(W-350-Scene_x_actual,H-350))

#Images
Toon_Test_idle = pygame.image.load("Sprites/Test_toon_idle.png")

Player_obj = pygame.image.load("Sprites/just test sprite.png")
def main_menu_render_floor():
    pygame.draw.rect(sc,WBLUE,(0,H//2+250,W,H//2-250))

def draw_obj_player():
    sc.blit(Player_obj,(W//2-150,H//2))
    


def Player_obj_config():
    global Toon_selected,Player_obj
    if Toon_selected == 0:
        Player_obj = Toon_Test_idle
    
    Player_obj.set_colorkey((0, 155, 0))
while running:
    while scene == "Main menu": #Lobby
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        bt = pygame.key.get_pressed()
        if bt[pygame.K_ESCAPE]:
            exit()
            
        sc.fill(RED) 
        
        main_menu_render_floor()
        
        #Player and all his things?
        Player_obj_config()
        draw_obj_player()
        
        pygame.display.update()
        clock.tick(FPS)
        Obj_player_anim_abilities_timer -= 1
        Obj_player_anim_walk_timer -= 1
    
        if Obj_player_anim_walk_timer <= 0:
            Obj_player_anim_walk_timer = 15
        if Obj_player_anim_abilities_timer <= 0:
            Obj_player_anim_abilities_timer = 2