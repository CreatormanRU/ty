import pygame
import random

pygame.init()
pygame.mixer.init()  # для звука

W = 1400  # ширина игрового окна
H = 900 # высота игрового окна
FPS = 60 # частота кадров в секунду
f_sys = pygame.font.SysFont('Fonts/FredokaOne-Regular.ttf', 50)
# Цвета (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WGRAY = (200, 200, 200)
GRAY = (155, 155, 155)
DGRAY = (100, 100, 100)
#Red
RED = (255, 0, 0)
#Green
GREEN = (0, 255, 0)
#Blue
BLUE = (0, 0, 255)
#YELLOW
YELLOW = (220, 220, 0)
#PINK
PINK = (255, 155, 155)

NDPINK = (200, 150, 150)
DPINK = (155, 100, 100)
DDPINK = (100, 55, 55)
sc = pygame.display.set_mode((W, H))
#sc = pygame.display.set_mode((W,H), pygame.FULLSCREEN | pygame.SCALED)
pygame.display.set_caption("Colorful world")
clock = pygame.time.Clock()

running = True
scene = "Main menu"
test_counter = 10
Toon_selected = 0
#OBJ_PLAYER
Obj_player_anim_walk_timer = 15
Obj_player_anim_abilities_timer = 2
Walking = False
Player_X = 0
Player_layer = random.randint(1,3)
Player_dir_cur_look = 1
Player_dir_was_look = 1
Player_walks1 = 1

#Stats
STAT_Health = random.randint(1,3)
STAT_Stamina = random.randint(1,5)
STAT_Speed = 1  #random.randint(1,5)
STAT_Extr_speed = random.randint(1,5)
STAT_Skillcheck =  random.randint(1,5)


#stats max and shi
Max_health = STAT_Health
Cur_health = Max_health
Max_stamina = 75 + (25 * STAT_Stamina)
Cur_stamina = Max_stamina 

#counters
Stamina_waste_counter = 5
Stamina_gain_counter = 30
Death_counter = 120
Stamina_punishment = 0

#funny numbers
Skill_check_chance = 0
Skill_check_roll = 0
Extracting_ichor = False

#Skill check bar
Skill_check_position = random.randint(0,500)
Skill_check_wide = 25 + (25 * STAT_Skillcheck)
Skill_check_meter_X = 0
Skill_check_goes = False
#MACHINES XPOS
Machine_1_XPOS = 350 #random.randint(-4500,4500)
Machine_1_type = 1
Machine_completition = 0
Machine_1_layer = random.randint(1,3)




#left_image = pygame.transform.flip(original_image, True, False) 
#        sc_text = f_sys.render("Song: Final Destination 0%", 3, BLACK)
#    pos = sc_text.get_rect(center=(0+250, 0+175))
#            SPACE_PRESS_NOW_spr.set_colorkey((0, 155, 0))
#            sc.blit(BF_idle_spr,(W-350-Scene_x_actual,H-350))

#Images
Toon_Test_idle = pygame.image.load("Sprites/Test_toon_idle.png")
Toon_Test_walk = pygame.image.load("Sprites/Test_toon_walk.png")
Death_toon = pygame.image.load("Sprites/Death_toon.png")
    #Hearts
Heart_Normal = pygame.image.load("Sprites/Hearts/Heart_normal.png")
Heart_Hurt = pygame.image.load("Sprites/Hearts/Heart_hurt.png")
Heart_Corrupted = pygame.image.load("Sprites/Hearts/Heart_corrupted.png")
Heart_Smilenbleed = pygame.image.load("Sprites/Hearts/Heart_=D.png")
    #UI
Running_indicator = pygame.image.load("Sprites/UI and Other/Running_indicator.png")
    #Machines
Machine_normal_not_finished = pygame.image.load("Sprites/Machines/Machine_normal_not_done.png")



Player_obj = pygame.image.load("Sprites/just test sprite.png")
def draw_skill_check_bar():
    pygame.draw.rect(sc,GRAY,(W//2-(300),H-230,600,65))
    #normal
    pygame.draw.rect(sc,WGRAY,(W//2-(300)+Skill_check_position,H-230,Skill_check_wide,65))
    #Super
    pygame.draw.rect(sc,YELLOW,(W//2-(300)+Skill_check_position+(Skill_check_wide//2)-(Skill_check_wide//3//2),H-230,Skill_check_wide//3,65))
    
    pygame.draw.rect(sc,RED,(W//2-(300)+Skill_check_meter_X,H-230,10,65))
    
    
def interact_with_E():
    pygame.draw.rect(sc,GRAY,(W//2-(150//2),H//2-75,150,75))
    f_sys = pygame.font.SysFont('Fonts/FredokaOne-Regular.ttf', 35)
    sc_text = f_sys.render(f"e to interact", 3, BLACK)
    pos = sc_text.get_rect(center=(W//2,H//2-(75//2)))
    sc.blit(sc_text, pos)
    f_sys = pygame.font.SysFont('Fonts/FredokaOne-Regular.ttf', 50)
def Machine_1_draw(): #107
    Machine_normal_not_finished.set_colorkey((0, 155, 0))
    sc.blit(Machine_normal_not_finished,(Machine_1_XPOS-Player_X,-26))
    if Player_X > -Machine_1_XPOS and Player_X < -Machine_1_XPOS+107 and Extracting_ichor == False:
        interact_with_E()



def draw_needed_stats():
    if Stamina_punishment >= 0:
        sc_text = f_sys.render(f"Stamina: {Cur_stamina}", 3, RED)
    else:
        sc_text = f_sys.render(f"Stamina: {Cur_stamina}", 3, BLACK)
    pos = sc_text.get_rect(center=(125, H//2+300))
    sc.blit(sc_text, pos)
def stats_draw_on_screen():
    sc_text = f_sys.render(f"Player_pos: {Player_X}", 3, BLACK)
    pos = sc_text.get_rect(center=(W//2, 150))
    sc.blit(sc_text, pos)
    sc_text = f_sys.render(f"Health: {STAT_Health}", 3, BLACK)
    pos = sc_text.get_rect(center=(W//2, 150+30))
    sc.blit(sc_text, pos)
    sc_text = f_sys.render(f"Stamina: {STAT_Stamina}", 3, BLACK)
    pos = sc_text.get_rect(center=(W//2, 150+30+30))
    sc.blit(sc_text, pos)
    sc_text = f_sys.render(f"Speed: {STAT_Speed}", 3, BLACK)
    pos = sc_text.get_rect(center=(W//2, 150+30+30+30))
    sc.blit(sc_text, pos)
    sc_text = f_sys.render(f"Extr_speed: {STAT_Extr_speed}", 3, BLACK)
    pos = sc_text.get_rect(center=(W//2, 150+30+30+30+30))
    sc.blit(sc_text, pos)
    sc_text = f_sys.render(f"Skillcheck: {STAT_Skillcheck}", 3, BLACK)
    pos = sc_text.get_rect(center=(W//2, 150+30+30+30+30+30))
    sc.blit(sc_text, pos)
def main_menu_render_floor():
    pygame.draw.rect(sc,DPINK,(0,H//2+250,W,H//2-250))
def draw_UI():
    Running_indicator.set_colorkey((0, 155, 0))
    #Heart UI
    pygame.draw.rect(sc, DGRAY, (0,H//2+340,175+90,H//2-340))
    pygame.draw.rect(sc, BLACK, (0,H//2+340,175+90,H//2-340),5)
    #Stamina UI
    if Player_walks1 == 2:
        sc.blit(Running_indicator,(280,H//2+340))

def draw_obj_player():
    sc.blit(Player_obj,(W//2-150,H//2))
def draw_health():
    Heart_Normal.set_colorkey((0, 155, 0))
    Heart_Hurt.set_colorkey((0, 155, 0))
    Heart_Corrupted.set_colorkey((0, 155, 0))
    Heart_Smilenbleed.set_colorkey((0, 155, 0))
    #HEATH 1
    if Cur_health >= 1:
        sc.blit(Heart_Normal,(15,H//2+350))
    #HEATH 2
    if Max_health >= 2 and Cur_health >= 2:
        sc.blit(Heart_Normal,(95,H//2+350))
    elif Cur_health < 2 and Max_health >= 2:
        sc.blit(Heart_Hurt,(95,H//2+350))
    else:
        sc.blit(Heart_Corrupted,(95,H//2+350))
    #HEATH 3
    if Max_health >= 3 and Cur_health >= 3:
        sc.blit(Heart_Normal,(175,H//2+350))
    elif Cur_health < 3 and Max_health >= 3:
        sc.blit(Heart_Hurt,(175,H//2+350))
    else:
        sc.blit(Heart_Corrupted,(175,H//2+350))
    
def Player_obj_config():
    global Toon_selected,Player_obj,Player_dir_was_look,Player_dir_cur_look
    if Toon_selected == 0:
        if Walking == True and Obj_player_anim_walk_timer >= 7:
            Player_obj = Toon_Test_walk
        else:
            Player_obj = Toon_Test_idle
        if Player_dir_cur_look != Player_dir_was_look:
            Player_obj = pygame.transform.flip(Player_obj, True, False) 
            Player_dir_cur_look = Player_dir_was_look
        
        if Cur_health <= 0:
            Player_obj = Death_toon
        
    Player_obj.set_colorkey((0, 155, 0))
while running:
    while scene == "Main menu": #Lobby
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        bt = pygame.key.get_pressed()
        if bt[pygame.K_ESCAPE]:
            exit()
        if bt[pygame.K_LSHIFT] and Cur_stamina >= 1:
            if Stamina_punishment <= 0:
                Player_walks1 = 2
            else:
                Player_walks1 = 1
        else:
            Player_walks1 = 1
        if bt[pygame.K_SPACE] and test_counter <= 0:
            Cur_health -= 1
            test_counter = 25
        if bt[pygame.K_c] and test_counter <= 0:
            Max_health -= 1
            test_counter = 25
        if bt[pygame.K_a]:
            Walking = True
            Player_X -= 1 + STAT_Speed * Player_walks1
            Player_dir_cur_look = 0
        elif bt[pygame.K_d]:
            Walking = True
            Player_X += 1 + STAT_Speed * Player_walks1
            Player_dir_cur_look = 1
        else:
            Walking = False
        sc.fill(PINK) 
        Player_obj_config()
        main_menu_render_floor()

        #Layers
        #1
        if Machine_1_layer == 1:
            Machine_1_draw()
            
        if Player_layer == 1:
            draw_obj_player()
        #2
        if Machine_1_layer == 2:
            Machine_1_draw()
        
        if Player_layer == 2:
            draw_obj_player()
        #3
        if Machine_1_layer == 3:
            Machine_1_draw()
        
        if Player_layer == 3:
            draw_obj_player()


        
        #UI
        draw_UI()
        stats_draw_on_screen()
        draw_needed_stats()
        draw_health()
        draw_skill_check_bar()
        
        
        pygame.display.update()
        clock.tick(FPS)
        Obj_player_anim_abilities_timer -= 1
        Obj_player_anim_walk_timer -= 1
    
        if Obj_player_anim_walk_timer <= 0:
            Obj_player_anim_walk_timer = 15
        if Obj_player_anim_abilities_timer <= 0:
            Obj_player_anim_abilities_timer = 2
        test_counter -= 1
        Stamina_punishment -= 1
        if Player_walks1 == 1:
            Stamina_gain_counter -= 1
        else:
            Stamina_waste_counter -= 1
        
        if Stamina_gain_counter <= 0:
            Cur_stamina += 1
            Stamina_gain_counter = 20
        if Stamina_waste_counter <= 0:
            Cur_stamina -= 1
            Stamina_waste_counter = 5
            
        if Cur_stamina > Max_stamina:
            Cur_stamina = Max_stamina
        if Cur_stamina <= 1:
            Stamina_punishment = 180
        if Cur_stamina < 0:
            Cur_stamina = 0
        if Cur_health > Max_health:
            Cur_health = Max_health
        if Cur_health <= 0:
            Death_counter -= 1
        if Death_counter <= -1:
            exit()
        if Skill_check_goes == True:
            Skill_check_meter_X += 2
        if Skill_check_meter_X >= 600-10:
            Skill_check_meter_X = 0
            Skill_check_position = random.randint(0,500)
