import pygame
import random

pygame.init()
pygame.mixer.init()  # для звука

W = 1400  # ширина игрового окна
H = 900 # высота игрового окна
FPS = 60 # частота кадров в секунду

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
pygame.display.set_caption("Your only move is TAUNT")
clock = pygame.time.Clock()

running = True
scene = "menu"



while running:
    while scene == "menu": #Main_menu
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        bt = pygame.key.get_pressed()
        if bt[pygame.K_ESCAPE]:
            exit()
            
        sc.fill(RED) 
        
        
        
        
        
        pygame.display.update()
        clock.tick(FPS)
    
