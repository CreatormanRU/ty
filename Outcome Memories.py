import pygame
import random
import math
#from Earthhelper import *
#
W = 900
H = 900

#tick_speed = int(input())
sc = pygame.display.set_mode((W,H), pygame.FULLSCREEN | pygame.SCALED)


pygame.mixer.pre_init(44100, -16, 1, 512)
# Инициализация pygame
pygame.init()

f_sys = pygame.font.SysFont('comicsans', 10)

pygame.display.set_caption("Earthbound")
FPS = 60       # число кадров в секунду
clock = pygame.time.Clock()
RED = (255,0,0)
DRED = (150,0,0)
DDRED = (100,0,0)
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
BROWN = (139, 69, 19)
DBROWN = (109, 39, 0)

#extra important!
running = True
Scene = 0
size_of_map = 5
block_size = 90


map = [
[[0,0],[0,0],[0,0],[0,0],[0,0]],
[[0,0],[0,0],[0,0],[0,0],[0,0]],
[[0,0],[0,0],[0,0],[0,0],[0,0]],
[[0,0],[0,0],[0,0],[0,0],[0,0]],
[[0,0],[0,0],[0,0],[0,0],[0,0]],
]
#Sprites_outcome/Block_dirt_grass.png
#pygame.image.load("Sprites_outcome/Block_dirt.png")
dirt_block_sprite = pygame.transform.scale((pygame.image.load("Sprites_outcome/Block_dirt.png")), (block_size, block_size))
dirt_block_sprite_left = pygame.transform.flip(dirt_block_sprite, True, False)
dirt_grass_block_sprite = pygame.transform.scale((pygame.image.load("Sprites_outcome/Block_dirt_grass.png")), (block_size, block_size))
dirt_grass_block_sprite_left = pygame.transform.flip(dirt_grass_block_sprite, True, False)

def Read_map_and_draw_it():
    for i in range(size_of_map):
        for j in range(size_of_map):
            spr_type = -1
            spr_angle = -1
            slot_list = map[j][i]

            spr_type = slot_list[0]
            spr_angle = slot_list[1]

            slot_place_x = 90 * i
            slot_place_y = 90 * j

            if spr_type == 0:
                pass
            elif spr_type == 1:
                if spr_angle == 0:
                    sc.blit(dirt_block_sprite,(slot_place_x,slot_place_y))
                else:
                    sc.blit(dirt_block_sprite_left,(slot_place_x,slot_place_y))
            elif spr_type == 2:
                if spr_angle == 0:
                    sc.blit(dirt_grass_block_sprite,(slot_place_x,slot_place_y))
                else:
                    sc.blit(dirt_grass_block_sprite_left,(slot_place_x,slot_place_y))
            txt_surf = f_sys.render(f"Angle {spr_angle}", True, RED)
            sc.blit(txt_surf, (slot_place_x,slot_place_y))


#def display_info_player():
    #txt_surf = f_sys.render(f"Stun {Player_stun_time}", True, RED)
    #sc.blit(txt_surf, (Player_X-(Player_W//2),Player_Y))


while running:
    while Scene == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        bt = pygame.key.get_pressed()
        if bt[pygame.K_ESCAPE]:
            exit()

        sc.fill(WHITE)

        Read_map_and_draw_it()




        pygame.display.update()
        clock.tick(FPS)
