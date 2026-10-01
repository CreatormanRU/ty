from FNAB_AI_GUY import *
import pygame
import random
import math
# Start pygame mixer
pygame.mixer.init()

#if player_rect.colliderect(enemy_rect):
#    print("Collision detected!")


# Load music file
#pygame.mixer.music.load("FNAB_ost/Music_Box.mp3")
#pygame.mixer.music.load("FNAB_ost/Music_Box_5_am_variant.mp3")
# Play music (loops = -1 to loop forever)
#pygame.mixer.music.play(-1)

# Pause the music
#pygame.mixer.music.pause()

# Unpause/resume the music
#pygame.mixer.music.unpause()
#
# Stop the music completely
#pygame.mixer.music.stop()


for i in range(10):
    print("")

W = 1000
H = 800
sc = pygame.display.set_mode((W,H), pygame.FULLSCREEN | pygame.SCALED) #pygame.display.set_mode((W,H), pygame.FULLSCREEN) #pygame.display.set_mode((W, H))
#sc = pygame.display.set_mode((W,H))
pygame.mixer.pre_init(44100, -16, 1, 512)
# Инициализация pygame
pygame.init()

f_sys = pygame.font.SysFont('comicsans', 30)

pygame.display.set_caption("FNAB Beta 2")
FPS = 60       # число кадров в секунду
clock = pygame.time.Clock()
RED = (255,0,0)
DRED = (100,0,0)
BLUE = (0,0,255)
DBLUE = (0,0,100)
GREEN = (0,255,0)
BLACK = (0,0,0)
WHITE = (255,255,255)
GRAY = (100,100,100)
DGRAY = (50,50,50)
YELLOW = (242, 198, 0)
PURPLE = (155,0,155)
running = True
cliking = False
Night = 0
am = 0
Time = 0
E_Time = 0
Energy_use = 0
Energy = 100
Cameras = 0
Cameras_use_cd = 10
Mask = 0
Mask_use_cd = 10
Mask_Y = -800
CAM = 1
Springlocks = 1000
Win = 0
Prime = 1
DarkerMode = 1
Primecdchange = 10
Flashlight = 0
Flashlightcd = 0

Achivment_1 = False
Achivment_2 = False
Achivment_3 = False
Achivment_4 = False
Achivment_5 = False
View_achivments = False

BlackCamera = 0
BlackAI = 0
BlackChance = 30

GreenCamera = 0
GreenAI = 0
GreenChance = 30

BlueCamera = 0
BlueAI = 0
BlueChance = 30

RedCamera = 0
RedAI = 0
RedChance = 30

YellowCamera = 0
YellowAI = 0
YellowChance = 30
Yellow_atk_time = 49586

PurpleAI = 0
PurpleCamera = 0
PurpleMAXFLIPSAM = 1
PurpleFlipsAmount = 30

GrayAI = 0
GrayMaxPatience = 3500 - (95 * GrayAI)
GrayPatience = GrayMaxPatience
GrayPosCam = random.randint(1,10)
GrayCD = 5

WalkTimeCD = FPS

L_Door_light = 0
R_Door_light = 0
L_Door_closed = 0
R_Door_closed = 0

L_door_use_cd = 10
R_door_use_cd = 10

BlackPowerCd = 0
PowerOut = False
Music = -1
Music_box_played = 0
BlackMusicLast = 0
CustomNight = False
Score = 0
Death_reason = 0

Main_Menu_spr = pygame.image.load("FNAB_sprites/Main Menu.png")
Black_MM_spr = pygame.image.load("FNAB_sprites/Black_MM_screen.png")
Name_MM_spr = pygame.image.load("FNAB_sprites/Name_MM.png")
NS_Button_spr = pygame.image.load("FNAB_sprites/NS_button.png")
CustomNightNoPrime = pygame.image.load("FNAB_sprites/CNBG_NP.png")
CustomNightPrime = pygame.image.load("FNAB_sprites/CNBG_P.png")


Night_Office_spr = pygame.image.load("FNAB_sprites/Office.png")
LDoor_NL = pygame.image.load("FNAB_sprites/Door NL.png")
LDoor_WL = pygame.image.load("FNAB_sprites/LDoor WL.png")
RDoor_NL = pygame.image.load("FNAB_sprites/Door NL.png")
RDoor_WL = pygame.image.load("FNAB_sprites/RDoor WL.png")
RDoor_WL_Bl = pygame.image.load("FNAB_sprites/RDoor WL Bl.png")
LDoor_WL_Gr = pygame.image.load("FNAB_sprites/LDoor WL Gr.png")

OfficeDoor = pygame.image.load("FNAB_sprites/DOOR.png")

MaskButton = pygame.image.load("FNAB_sprites/Mask Button.png")
MaskButtonBroke = pygame.image.load("FNAB_sprites/Mask Button Broke.png")
CameraButton = pygame.image.load("FNAB_sprites/Camera Button.png")
CameraMap = pygame.image.load("FNAB_sprites/CameraMap.png")
WButton = pygame.image.load("FNAB_sprites/Press_W.png")

Cam_1 = pygame.image.load("FNAB_sprites/CAM_1.png")
Cam_2 = pygame.image.load("FNAB_sprites/CAM_2.png")
Cam_3 = pygame.image.load("FNAB_sprites/CAM_3.png")
Cam_4 = pygame.image.load("FNAB_sprites/CAM_4.png")
Cam_5 = pygame.image.load("FNAB_sprites/CAM_5.png")
Cam_6 = pygame.image.load("FNAB_sprites/CAM_6.png")
Cam_7 = pygame.image.load("FNAB_sprites/CAM_7.png")

Cam_80 = pygame.image.load("FNAB_sprites/CAM_8 R0.png")
Cam_81 = pygame.image.load("FNAB_sprites/CAM_8 R1.png")
Cam_82 = pygame.image.load("FNAB_sprites/CAM_8 R2.png")
Cam_83 = pygame.image.load("FNAB_sprites/CAM_8 R3.png")
Cam_84 = pygame.image.load("FNAB_sprites/CAM_8 R4.png")
Cam_85 = pygame.image.load("FNAB_sprites/CAM_8 R5.png")

Cam_9 = pygame.image.load("FNAB_sprites/CAM_9.png")
Cam_10 = pygame.image.load("FNAB_sprites/CAM_10.png")

Black_PlaceHolder = pygame.image.load("FNAB_sprites/BLACKholder.png")
Black_PlaceHolderDARK = pygame.image.load("FNAB_sprites/BLACKholderDARK.png")
Green_PlaceHolder = pygame.image.load("FNAB_sprites/GREENholder.png")
Blue_PlaceHolder = pygame.image.load("FNAB_sprites/BLUEholder.png")
Blue_holdOffice = pygame.image.load("FNAB_sprites/BLUEholdOffice.png")
Yellow_PlaceHolder = pygame.image.load("FNAB_sprites/YELLOWholder.png")
Gray_PlaceHolder = pygame.image.load("FNAB_sprites/GRAYholder.png")

CNPlaceBlack = pygame.image.load("FNAB_sprites/BlackCN.png")
CNPlaceGreen = pygame.image.load("FNAB_sprites/GreenCN.png")
CNPlaceBlue = pygame.image.load("FNAB_sprites/BlueCN.png")
CNPlaceRed = pygame.image.load("FNAB_sprites/RedCN.png")
CNPlaceYellow = pygame.image.load("FNAB_sprites/YellowCN.png")
CNPlacePurple = pygame.image.load("FNAB_sprites/PurpleCN.png")
CNPlaceGray = pygame.image.load("FNAB_sprites/GrayCN.png")
MaskOffice = pygame.image.load("FNAB_sprites/MASK.png")
FlashlightOffice = pygame.image.load("FNAB_sprites/Flashlight.png")
Achiv_1 = pygame.image.load("FNAB_sprites/Achivment_1.png")
Achiv_2 = pygame.image.load("FNAB_sprites/Achivment_2.png")
Achiv_3 = pygame.image.load("FNAB_sprites/Achivment_3.png")
Achiv_4 = pygame.image.load("FNAB_sprites/Achivment_4.png")
Achiv_5 = pygame.image.load("FNAB_sprites/Achivment_5.png")

Black_MM_spr.set_colorkey((0, 155, 0))
Name_MM_spr.set_colorkey((0, 155, 0))
OfficeDoor.set_colorkey((0, 155, 0))
CameraButton.set_colorkey((0, 155, 0))
MaskButton.set_colorkey((0, 155, 0))
MaskButtonBroke.set_colorkey((0, 155, 0))
CameraMap.set_colorkey((0, 155, 0))
MaskOffice.set_colorkey((0, 155, 0))
Black_PlaceHolder.set_colorkey((0, 155, 0))
Green_PlaceHolder.set_colorkey((0, 155, 0))
Blue_PlaceHolder.set_colorkey((0, 155, 0))
Gray_PlaceHolder.set_colorkey((0, 155, 0))
RDoor_WL_Bl.set_colorkey((0, 155, 0))
LDoor_WL_Gr.set_colorkey((0, 155, 0))
Blue_holdOffice.set_colorkey((0, 155, 0))
Black_PlaceHolderDARK.set_colorkey((0, 155, 0))
Yellow_PlaceHolder.set_colorkey((0, 155, 0))
FlashlightOffice.set_colorkey((0, 155, 0))

CursorPosX,CursorPosY = pygame.mouse.get_pos()

BOTinputs = "none"
BOTstate = 0 #office - 0/cameras - 1
BOTknowsaboutRED = False
botGRAYCAM = 0
#inputs
# Q - LEFT DOOR
# A - LEFT LIGHT
# E - RIGHT DOOR
# D - LEFT LIGHT
# W - WIND UP
# SPACE - CAMERAS
# LSHIFT - MASK
# num - cam number





while running:
    while Night == 0 and CustomNight == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                cliking = True
                print("NO")
            else:
                cliking = False






        bt = pygame.key.get_pressed()
        if bt[pygame.K_ESCAPE]:
            exit()
        if bt[pygame.K_1]:
            Night = 1
            BlackAI = 2
            GreenAI = 1
            BlueAI = -1
            RedAI = -1
            PurpleAI = 0
            GrayAI = -1
        if bt[pygame.K_2]:
            Night = 2
            BlackAI = 5
            GreenAI = 6
            BlueAI = 8
            RedAI = 4
            PurpleAI = 0
            GrayAI = 5
        if bt[pygame.K_3]:
            Night = 3
            BlackAI = 9
            GreenAI = 10
            BlueAI = 10
            RedAI = 8
            PurpleAI = 1
            PurpleMAXFLIPSAM = 60
            GrayAI = 10
        if bt[pygame.K_4]:
            Night = 4
            BlackAI = 14
            GreenAI = 12
            BlueAI = 10
            RedAI = 11
            YellowAI = 19
            PurpleAI = 1
            PurpleMAXFLIPSAM = 55
            GrayAI = 13
        if bt[pygame.K_5]:
            Night = 5
            BlackAI = 15
            GreenAI = 13
            BlueAI = 13
            RedAI = 13
            YellowAI = 19
            PurpleAI = 1
            PurpleMAXFLIPSAM = 50
            GrayAI = 15
        if bt[pygame.K_6]:
            Night = 6
            BlackAI = 17
            GreenAI = 15
            BlueAI = 16
            RedAI = 14
            YellowAI = 22
            PurpleAI = 1
            PurpleMAXFLIPSAM = 40
            GrayAI = 18
        if bt[pygame.K_7]:
            Night = 7
            BlackAI = 20
            GreenAI = 18
            BlueAI = 17
            RedAI = 16
            YellowAI = 24
            PurpleAI = 1
            PurpleMAXFLIPSAM = 30
            GrayAI = 20
        if bt[pygame.K_9]:
            CustomNight = True
        if bt[pygame.K_q]:
            Prime = 2
        if bt[pygame.K_w]:
            Prime = 1
        if bt[pygame.K_a]:
            DarkerMode = 2
        if bt[pygame.K_s]:
            DarkerMode = 1
        if bt[pygame.K_SPACE]:
            View_achivments = True
        else:
            View_achivments = False

        sc.fill(BLACK)
        sc.blit(Main_Menu_spr, (0,0))
        sc.blit(Black_MM_spr, (0,0))
        sc.blit(Name_MM_spr, (0,0))
        #sc.blit(NS_Button_spr, (50,H-100))

        txt = f_sys.render('Press number from 1-7 to select night, 9 to Custom Night', True, WHITE)
        sc.blit(txt, (W//2-450, H-100))
        txt = f_sys.render('BETA 1', True, WHITE)
        sc.blit(txt, (W//2-450, H-50))
        txt = f_sys.render('Q to turn on Prime, W to dissable', True, WHITE)
        sc.blit(txt, (W//2-450, H-250))
        txt = f_sys.render('A to turn on Darker, S to dissable', True, WHITE)
        sc.blit(txt, (W//2-450, H-300))
        if Prime == 2:
            txt = f_sys.render('PRIME mode, Characters move speed x2', True, RED)
            sc.blit(txt, (W//2-450, H-200))
        if DarkerMode == 2:
            txt = f_sys.render('DARKER mode, Less vision, new power waste item', True, GRAY)
            sc.blit(txt, (W//2-450, H-150))



        if View_achivments == True:
            sc.blit(Main_Menu_spr, (0,0))
            #Achivment 1
            sc.blit(Achiv_1,(10,10))
            txt = f_sys.render('So Close!', True, WHITE)
            sc.blit(txt, (110, 10))
            txt = f_sys.render('Die at 5am', True, WHITE)
            sc.blit(txt, (110, 70))
            #Achivment 2
            sc.blit(Achiv_2,(10,120))
            txt = f_sys.render('oh? Whats wrong? Cant use your mask?', True, WHITE)
            sc.blit(txt, (110, 120))
            txt = f_sys.render('Get Yellow in office with Blue and die to him', True, WHITE)
            sc.blit(txt, (110, 180))
            #Achivment 3
            sc.blit(Achiv_3,(10,230))
            txt = f_sys.render('WOW! I hate it :D', True, WHITE)
            sc.blit(txt, (110, 230))
            txt = f_sys.render('Win game with Darker mode', True, WHITE)
            sc.blit(txt, (110, 290))
            #Achivment 4
            sc.blit(Achiv_4,(10,340))
            txt = f_sys.render('You think your speed matters?', True, WHITE)
            sc.blit(txt, (110, 340))
            txt = f_sys.render('Win game with Prime', True, WHITE)
            sc.blit(txt, (110, 400))
            #Achivment 5
            sc.blit(Achiv_5,(10,450))
            txt = f_sys.render('7/30', True, WHITE)
            sc.blit(txt, (110, 450))
            txt = f_sys.render('Beat 7/30 with/without modifiers (Beta 0.2)', True, WHITE)
            sc.blit(txt, (110, 510))

            #Achiv_1 = pygame.image.load("FNAB_sprites/Achivment_1.png")
            #Achiv_2 = pygame.image.load("FNAB_sprites/Achivment_2.png")
            #Achiv_3 = pygame.image.load("FNAB_sprites/Achivment_3.png")
            #Achiv_4 = pygame.image.load("FNAB_sprites/Achivment_4.png")
            #Achiv_5 = pygame.image.load("FNAB_sprites/Achivment_5.png")


        pygame.display.update()
        clock.tick(FPS)
    am = 0
    Time = 0
    E_Time = 0
    Energy_use = 0
    Energy = 100
    Cameras = 0
    Cameras_use_cd = 10
    Mask = 0
    Mask_use_cd = 10
    Mask_Y = -800
    CAM = 1
    Springlocks = 1000
    Win = 0
    Flashlight = 0

    BlackCamera = 0
    BlackChance = 30

    GreenCamera = 0
    GreenChance = 30

    BlueCamera = 0
    BlueChance = 30

    RedCamera = 0
    RedChance = 30

    YellowCamera = 0
    YellowChance = 30
    Yellow_atk_time = 49586

    PurpleCamera = 0
    PurpleFlipsAmount = 0
    WalkTimeCD = FPS

    GrayMaxPatience = 3500 - (95 * GrayAI)
    GrayPatience = GrayMaxPatience
    GrayPosCam = random.randint(1,10)
    GrayCD = 5

    L_Door_light = 0
    R_Door_light = 0
    L_Door_closed = 0
    R_Door_closed = 0

    L_door_use_cd = 10
    R_door_use_cd = 10

    BlackPowerCd = 0
    PowerOut = False
    Music_box_played = 0
    BlackMusicLast = 0
    Death_reason = 0

#//////////////////////////////////////////////////////
    while Night != 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                cliking = True
                print("NesaO")
            else:
                cliking = False
        bt = pygame.key.get_pressed()
        if bt[pygame.K_ESCAPE]:
            exit()
        #LEFT DOOR
        if (bt[pygame.K_a] or BOTinputs == "a"):
            L_Door_light = 1
        else:
            L_Door_light = 0
        if (bt[pygame.K_q] or BOTinputs == "q") and L_door_use_cd <= 0:
            L_door_use_cd = 10
            if L_Door_closed == 0:
                L_Door_closed = 1
            else:
                L_Door_closed = 0
        #RIGHT DOOR
        if bt[pygame.K_d] or BOTinputs == "d":
            R_Door_light = 1
        else:
            R_Door_light = 0
        if (bt[pygame.K_e] or BOTinputs == "e") and R_door_use_cd <= 0:
            R_door_use_cd = 10
            if R_Door_closed == 0:
                R_Door_closed = 1
            else:
                R_Door_closed = 0
        if (bt[pygame.K_SPACE] and Cameras_use_cd <= 0):
            if Mask == 0:
                Cameras_use_cd = 10
                if Cameras == 0:
                    Cameras = 1
                    if PurpleCamera == 1:
                        PurpleFlipsAmount += 1
                else:
                    Cameras = 0
                    YellowChance = random.randint(0,75)
                    if YellowCamera == 0:
                        if YellowChance < YellowAI:
                            YellowCamera = 1

        if (bt[pygame.K_LSHIFT] or BOTinputs == "LSHIFT") and Mask_use_cd <= 0 and Cameras == 0 and Springlocks > -1:
            Mask_use_cd = 10
            if Mask == 0:
                Mask = 1
            else:
                Mask = 0

        if bt[pygame.K_LCTRL] and Flashlightcd <= 0:
            Flashlightcd = 10
            if Flashlight == 0:
                Flashlight = 1
            else:
                Flashlight = 0

        if bt[pygame.K_w] and Cameras == 1 and CAM == GrayPosCam:
            if GrayPatience <= GrayMaxPatience:
                GrayPatience += 5
            else:
                GrayPatience = GrayMaxPatience
        if bt[pygame.K_1] and Cameras == 1:
            CAM = 1
        if bt[pygame.K_2] and Cameras == 1:
            CAM = 2
        if bt[pygame.K_3] and Cameras == 1:
            CAM = 3
        if bt[pygame.K_4] and Cameras == 1:
            CAM = 4
        if bt[pygame.K_5] and Cameras == 1:
            CAM = 5
        if bt[pygame.K_6] and Cameras == 1:
            CAM = 6
        if bt[pygame.K_7] and Cameras == 1:
            CAM = 7
        if bt[pygame.K_8] and Cameras == 1:
            CAM = 8
        if bt[pygame.K_9] and Cameras == 1:
            CAM = 9
        if bt[pygame.K_0] and Cameras == 1:
            CAM = 10

        #NO POWERRRRRRRRRRRRRRRRRR
        if PowerOut == False:
            if Energy <= -1:
                L_Door_closed = 0
                R_Door_closed = 0
                Mask = 0
                Cameras = 0
                R_Door_light = 0
                L_Door_light = 0
                BlackCamera = -99999
                BlueCamera = -99999
                GreenCamera = -99999
                RedCamera = -99999
                if Energy > -100:
                    Energy -= 0.5
            if Energy <= -100 and PowerOut == False:
                BlackPowerCd = random.randint(10,330)
                BlackMusicLast = random.randint(50,2000)
                PowerOut = True
        else:
            pass
        CursorPosX,CursorPosY = pygame.mouse.get_pos()

        ################################
        if Cameras == 0:
            sc.blit(Night_Office_spr, (0,0))

            if L_Door_light == 0:
                sc.blit(LDoor_NL, (25,190))
            else:
                sc.blit(LDoor_WL, (25,190))
                if GreenCamera == 5:
                    sc.blit(LDoor_WL_Gr, (25,190))
            if L_Door_closed == 0:
                pass
            else:
                sc.blit(OfficeDoor, (25,190))

            if R_Door_light == 0:
                sc.blit(RDoor_NL, (W-244-25,190))
            else:
                sc.blit(RDoor_WL, (W-244-25,190))
                if BlackCamera == 4:
                    sc.blit(RDoor_WL_Bl, (W-244-25,190))
            if R_Door_closed == 0:
                pass
            else:
                sc.blit(OfficeDoor, (W-244-25,190))
            if BlueCamera == 6:
                sc.blit(Blue_holdOffice, (0,0))



            if YellowCamera == 1:
                sc.blit(Yellow_PlaceHolder, (0,0))

            #YellowCamera = 0
            #YellowAI = 1


            sc.blit(MaskOffice, (0,Mask_Y))




        #CAMERAAAAAAAAAAAAAAAAAAAAAASSS
        if Cameras == 0:
            if Mask == 0:
                sc.blit(CameraButton, (W//2-200,H-70))
            if Springlocks > -1:
                sc.blit(MaskButton, (W//2+150,H-70))
            else:
                sc.blit(MaskButtonBroke, (W//2+150,H-70))
        else:
            sc.fill(BLACK)
            if CAM == 1:
                sc.blit(Cam_1,(0,0))
                if BlackCamera == 0:
                    sc.blit(Black_PlaceHolder,(0,0))
                if GreenCamera == 0:
                    sc.blit(Green_PlaceHolder,(0,0))
            if CAM == 2:
                sc.blit(Cam_2,(0,0))
                if BlackCamera == 1:
                    sc.blit(Black_PlaceHolder,(0,0))
                if GreenCamera == 2:
                    sc.blit(Green_PlaceHolder,(0,0))
            if CAM == 3:
                sc.blit(Cam_3,(0,0))
                if BlackCamera == 2:
                    sc.blit(Black_PlaceHolder,(0,0))
            if CAM == 4:
                sc.blit(Cam_4,(0,0))
                if GreenCamera == 4:
                    sc.blit(Green_PlaceHolder,(0,0))
            if CAM == 5:
                sc.blit(Cam_5,(0,0))
                if BlackCamera == 3:
                    sc.blit(Black_PlaceHolder,(0,0))
            if CAM == 6:
                sc.blit(Cam_6,(0,0))
                if GreenCamera == 1:
                    sc.blit(Green_PlaceHolder,(0,0))
            if CAM == 7:
                sc.blit(Cam_7,(0,0))
            if CAM == 8:
                if RedCamera == 0:
                    sc.blit(Cam_80,(0,0))
                if RedCamera == 1:
                    sc.blit(Cam_81,(0,0))
                if RedCamera == 2:
                    sc.blit(Cam_82,(0,0))
                if RedCamera == 3:
                    sc.blit(Cam_83,(0,0))
                if RedCamera == 4:
                    sc.blit(Cam_84,(0,0))
                if RedCamera >= 5:
                    sc.blit(Cam_85,(0,0))
            if CAM == 9:
                sc.blit(Cam_9,(0,0))
                if BlueCamera <= 4:
                    sc.blit(Blue_PlaceHolder,(0,0))
                if GreenCamera == 3:
                    sc.blit(Green_PlaceHolder,(0,0))
            if CAM == 10:
                sc.blit(Cam_10,(0,0))
            if CAM == GrayPosCam and GrayAI != -1:
                sc.blit(Gray_PlaceHolder, (0,0))
                sc.blit(WButton, (130,H//2))
                f_sys = pygame.font.SysFont('comicsans', 20)
                txt = f_sys.render(f"{GrayPatience}", True, WHITE)
                sc.blit(txt, (130, H//2+80))

            sc.blit(CameraButton, (W//2-200,H-70))
            sc.blit(CameraMap, (W//2+130,H//2))
        if DarkerMode == 2:
            if Flashlight == 1:
                sc.blit(FlashlightOffice, (CursorPosX-(W//2*2),CursorPosY-(H//2*2)))
            else:
                sc.fill(BLACK)



        f_sys = pygame.font.SysFont('comicsans', 50)
        txt = f_sys.render(f"AM: {am}", True, WHITE)
        sc.blit(txt, (20, 0))
        f_sys = pygame.font.SysFont('comicsans', 20)
        txt = f_sys.render(f"Time: {Time}", True, WHITE)
        sc.blit(txt, (20, 70))
        f_sys = pygame.font.SysFont('comicsans', 30)
        txt = f_sys.render(f"Energy use: {Energy_use}", True, WHITE)
        sc.blit(txt, (20, H-65))
        f_sys = pygame.font.SysFont('comicsans', 45)
        txt = f_sys.render(f"Energy: {Energy}", True, WHITE)
        sc.blit(txt, (20, H-120))
        f_sys = pygame.font.SysFont('comicsans', 20)
        txt = f_sys.render(f"Energy Time: {E_Time}", True, WHITE)
        sc.blit(txt, (20, H-25))
        f_sys = pygame.font.SysFont('comicsans', 30)
        if PurpleCamera != 0:
            f_sys = pygame.font.SysFont('comicsans', 50)
            txt = f_sys.render(f"Camera flips left: {(PurpleMAXFLIPSAM-PurpleFlipsAmount)}", True, PURPLE)
            sc.blit(txt, (W//2-100, 150))
        f_sys = pygame.font.SysFont('comicsans', 30)
        if Mask == 1:
            txt = f_sys.render(f"Springlocks: {Springlocks}", True, RED)
            sc.blit(txt, (W//2-150, 25))
            f_sys = pygame.font.SysFont('comicsans', 30)
        #botplay
        #    BOTPLAY()
        #NUH UH, NO ENERGY OLOLOLO
        if PowerOut == True:
            sc.fill(BLACK)
            GrayAI = -1
            if BlackPowerCd > 0:
                BlackPowerCd -= 1
            else:
                sc.blit(Black_PlaceHolderDARK, (0,0))
                if Music_box_played == 0:
                    if am != 5:
                        Music = 0
                    else:
                        Music = 1
                    Music_box_played = 1
                BlackPowerCd -= 1
                if BlackPowerCd <= -BlackMusicLast:
                    print("Black:'L energy use XD'")
                    exit()
        ###############################################
        if Mask == 1 and Mask_Y < 0:
            Mask_Y += 100
        if Mask == 0 and Mask_Y > -800:
            Mask_Y -= 100

        if Mask == 1:
            Springlocks -= (Night+am)//3
        else:
            if Springlocks < 1000:
                Springlocks += 0.5
        if Springlocks < 0:
            Springlocks = -99999999999999999999999
            Mask = 0
        L_door_use_cd -= 1
        R_door_use_cd -= 1
        Cameras_use_cd -= 1
        Mask_use_cd -= 1
        Flashlightcd -= 1
        Time += 1
        E_Time += Energy_use
        if Time >= 3600:
            am += 1
            Time = 0
        if E_Time >= 220:
            Energy -= 1
            E_Time = 0
        WalkTimeCD -= 1
        if WalkTimeCD < 0:
            if BlackCamera == 4:
                BlackChance = random.randint(0,15)
            else:
                BlackChance = random.randint(0,30)
            if GreenCamera == 5:
                GreenChance = random.randint(0,15)
            else:
                GreenChance = random.randint(0,30)
            if BlueCamera == 6:
                BlueChance = random.randint(0,15)
            else:
                BlueChance = random.randint(0,30)
            if GrayAI >= random.randint(0,175):
                GrayPosCam = random.randint(1,10)
            if Cameras == 1 and CAM == 8:
                RedChance = 999
            else:
                if RedCamera == 6:
                    RedChance = random.randint(0,15)
                else:
                    RedChance = random.randint(0,30)
            if BlackChance <= BlackAI:
                BlackCamera += 1
            if GreenChance <= GreenAI:
                GreenCamera += 1
            if BlueChance <= BlueAI:
                BlueCamera += 1
            if RedChance <= RedAI:
                RedCamera += 1
            WalkTimeCD = FPS // Prime

        if PurpleFlipsAmount > PurpleMAXFLIPSAM:
            print("Purple:'Thats it! im taking away your breathing previleges!'")
            Death_reason = 8



        if YellowCamera == 1:
            if Mask == 1:
                print("Yellow:'Mask? Really? Do you think im THAT dumb?'")
                Death_reason = 7
            if Cameras == 1:
                YellowCamera = 0

        #1 - Death to Black
        #2 - Death to Green (Door)
        #3 - Death to Green (Mask)
        #4 - Death to Red (Door)
        #5 - Death to Red (Mask)
        #6 - Death to Blue (Mask)
        #7 - Death to Yellow
        #8 - Death to Purple

        Energy_use = L_Door_closed + L_Door_light + R_Door_closed + R_Door_light + Cameras + Flashlight
        if GrayAI >= 1:
            GrayCD -= 1
            if GrayCD <= 0:
                GrayPatience -= 2 # * Prime
                GrayCD = 5 // Prime



        if BlackCamera == 5:
            if R_Door_closed == 0:
                if Mask == 0:
                    print("Black:'Uhh... close the door next time or put that... mask? whatever...'")
                    Death_reason = 1
                else:
                    BlackCamera = 0
            else:
                BlackCamera = 0

        if GreenCamera == 6:
            if L_Door_closed == 0:
                if Mask == 0:
                    print("Green:'Maybe pressing Q while im not on cameras will help?'")
                    Death_reason = 2
                else:
                    print("Green:'HOW DARE YOU'")
                    Death_reason = 3
            else:
                GreenCamera = 0

        if RedCamera == 7:
            if L_Door_closed == 0:
                if Mask == 0:
                    print("Red:'Awww... Too slow!'")
                    Death_reason = 4
                else:
                    print("Red:'Impersonating my friend? So weird...'")
                    Death_reason = 5
            else:
                RedCamera = 0
                Energy -= ((1 + am)//2)

        if BlueCamera == 7:
            if Mask == 0:
                print("Blue:'Wear a mask next time'")
                Death_reason = 6
            else:
                BlueCamera = 0
        if GrayPatience <= 0:
            print("Gray:'beep boop baap'")
            Death_reason = 9


        if Death_reason != 0:
            Night = 0
        if am >= 6:
            Win = 1

        if Music != -1:
            pygame.mixer.music.stop()
            if Music == 0:
                pygame.mixer.music.load("FNAB_ost/Music_Box.mp3")
            if Music == 1:
                pygame.mixer.music.load("FNAB_ost/Music_Box_5_am_variant.mp3")
            pygame.mixer.music.play(-1)
            Music = -1

        if am == 4 and PurpleAI != 0:
            PurpleCamera = 1

        L_Door_closed = door_leftYN(L_Door_closed,GreenCamera,RedCamera)
        R_Door_closed = door_rightYN(R_Door_closed,BlackCamera)
        Mask, Cameras = Maskconfig(Mask,BlueCamera,YellowCamera,Cameras) #mask blue yellow cameras
        GrayPatience, Cameras, CAM = Graywindup(Mask,Cameras,GrayPatience,GrayMaxPatience,GrayPosCam,CAM) #windupleft,cameras,cam

        print(L_Door_closed,GreenCamera,RedCamera,GrayMaxPatience)

        #print(BOTinputs,BOTstate,BOTknowsaboutRED,botGRAYCAM)
        #print(Cameras, YellowAI,  YellowChance,YellowCamera)
        pygame.display.update()
        clock.tick(FPS)
        while Win == 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    cliking = True
                    print("NesaO")
                else:
                    cliking = False
            bt = pygame.key.get_pressed()
            if bt[pygame.K_ESCAPE]:
                exit()
            if bt[pygame.K_SPACE]:
                Win = 0
            Night = 0

            sc.fill(BLACK)
            f_sys = pygame.font.SysFont('comicsans', 100)
            txt = f_sys.render("^_^ 6 AM ^_^", True, WHITE)
            sc.blit(txt, (W//2-350, H//2))
            txt = f_sys.render("Space to main menu", True, WHITE)
            sc.blit(txt, (W//2-350, H//2+150))
            pygame.display.update()
            clock.tick(FPS)
            f_sys = pygame.font.SysFont('comicsans', 30)

    while CustomNight == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                cliking = True
                print("NesaO")
            else:
                cliking = False
        bt = pygame.key.get_pressed()
        if bt[pygame.K_ESCAPE]:
            exit()
        if bt[pygame.K_q]:
            BlackAI += 1
        if bt[pygame.K_a]:
            BlackAI -= 1

        if bt[pygame.K_w]:
            GreenAI += 1
        if bt[pygame.K_s]:
            GreenAI -= 1

        if bt[pygame.K_e]:
            BlueAI += 1
        if bt[pygame.K_d]:
            BlueAI -= 1

        if bt[pygame.K_r]:
            RedAI += 1
        if bt[pygame.K_f]:
            RedAI -= 1

        if bt[pygame.K_t]:
            YellowAI += 1
        if bt[pygame.K_g]:
            YellowAI -= 1

        if bt[pygame.K_y]:
            PurpleAI += 1
        if bt[pygame.K_h]:
            PurpleAI -= 1

        if bt[pygame.K_u]:
            GrayAI += 1
        if bt[pygame.K_j]:
            GrayAI -= 1



        if bt[pygame.K_x]:
            if Primecdchange < 0:
                if Prime == 1 and Primecdchange < 0:
                    Prime = 2
                    Primecdchange = 10
                if Prime == 2 and Primecdchange < 0:
                    Prime = 1
                    Primecdchange = 10

        if bt[pygame.K_v]:
            if Primecdchange < 0:
                if DarkerMode == 1 and Primecdchange < 0:
                    DarkerMode = 2
                    Primecdchange = 10
                if DarkerMode == 2 and Primecdchange < 0:
                    DarkerMode = 1
                    Primecdchange = 10

        if bt[pygame.K_z]:
            if Primecdchange < 0:
                BlackAI = random.randint(0,30)
                GreenAI = random.randint(0,30)
                BlueAI = random.randint(0,30)
                RedAI = random.randint(0,30)
                YellowAI = random.randint(0,30)
                PurpleAI = random.randint(0,30)
                GrayAI = random.randint(0,30)
                Prime = random.randint(1,2)
                DarkerMode = random.randint(1,2)
                Primecdchange = 10

        if bt[pygame.K_c]:
            CustomNight = False
            Night = 8
            PurpleMAXFLIPSAM = 60 - PurpleAI

        if BlackAI >= 31:
            BlackAI = 30
        if BlackAI <= -2:
            BlackAI = -1
        if GreenAI >= 31:
            GreenAI = 30
        if GreenAI <= -2:
            GreenAI = -1
        if BlueAI >= 31:
            BlueAI = 30
        if BlueAI <= -2:
            BlueAI = -1
        if RedAI >= 31:
            RedAI = 30
        if RedAI <= -2:
            RedAI = -1
        if YellowAI >= 31:
            YellowAI = 30
        if YellowAI <= -2:
            YellowAI = -1
        if PurpleAI >= 31:
            PurpleAI = 30
        if PurpleAI <= -2:
            PurpleAI = -1
        if GrayAI >= 31:
            GrayAI = 30
        if GrayAI <= -2:
            GrayAI = -1

        if Prime == 1:
            sc.blit(CustomNightNoPrime, (0,0))
        else:
            sc.blit(CustomNightPrime, (0,0))

        sc.blit(CNPlaceBlack, (50,H//2-350))
        sc.blit(CNPlaceGreen, (250,H//2-350))
        sc.blit(CNPlaceBlue, (450,H//2-350))
        sc.blit(CNPlaceRed, (650,H//2-350))
        sc.blit(CNPlaceYellow, (50,H//2-150))
        sc.blit(CNPlacePurple, (250,H//2-150))
        sc.blit(CNPlaceGray, (450,H//2-150))

        f_sys = pygame.font.SysFont('comicsans', 20)
        txt = f_sys.render("Q +1/A -1", True, WHITE)
        sc.blit(txt, (50,H//2-200))
        txt = f_sys.render(f"AI: {BlackAI}", True, WHITE)
        sc.blit(txt, (50,H//2-225))

        txt = f_sys.render("W +1/S -1", True, WHITE)
        sc.blit(txt, (250,H//2-200))
        txt = f_sys.render(f"AI: {GreenAI}", True, WHITE)
        sc.blit(txt, (250,H//2+-225))

        txt = f_sys.render("E +1/D -1", True, WHITE)
        sc.blit(txt, (450,H//2-200))
        txt = f_sys.render(f"AI: {BlueAI}", True, WHITE)
        sc.blit(txt, (450,H//2-225))

        txt = f_sys.render("R +1/A -1", True, WHITE)
        sc.blit(txt, (650,H//2-200))
        txt = f_sys.render(f"AI: {RedAI}", True, WHITE)
        sc.blit(txt, (650,H//2-225))

        txt = f_sys.render("T +1/G -1", True, WHITE)
        sc.blit(txt, (50,H//2))
        txt = f_sys.render(f"AI: {YellowAI}", True, WHITE)
        sc.blit(txt, (50,H//2-25))

        txt = f_sys.render("Y +1/H -1", True, WHITE)
        sc.blit(txt, (250,H//2))
        txt = f_sys.render(f"AI: {PurpleAI}", True, WHITE)
        sc.blit(txt, (250,H//2-25))

        txt = f_sys.render("U +1/J -1", True, WHITE)
        sc.blit(txt, (450,H//2))
        txt = f_sys.render(f"AI: {GrayAI}", True, WHITE)
        sc.blit(txt, (450,H//2-25))

        f_sys = pygame.font.SysFont('comicsans', 30)
        txt = f_sys.render(f"Score: {Score}", True, WHITE)
        sc.blit(txt, (250,H-120))
        f_sys = pygame.font.SysFont('comicsans', 20)

        Score = ((60 + (((BlackAI + GreenAI + BlueAI + RedAI + YellowAI + PurpleAI + GrayAI) * 10)) * Prime * DarkerMode))
        txt = f_sys.render("(C) - Start, (Z) - Random AI diff, (X) - Prime on/off, (V) - Darker on/off", True, WHITE)
        sc.blit(txt, (15,H-75))
        f_sys = pygame.font.SysFont('comicsans', 30)
        if Prime == 2:
            txt = f_sys.render('PRIME mode, Characters move speed x2', True, DBLUE)
            sc.blit(txt, (W//2-450, H-150))
        if DarkerMode == 2:
            txt = f_sys.render('Darker mode, Dont forget a flashlight!', True, DGRAY)
            sc.blit(txt, (W//2-450, H-200))



        Primecdchange -= 1

        #print(Prime, Primecdchange)


        pygame.display.update()
        clock.tick(FPS)
    while Death_reason != 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                cliking = True
                print("NesaO")
            else:
                cliking = False
        bt = pygame.key.get_pressed()
        if bt[pygame.K_ESCAPE]:
            exit()
        if bt[pygame.K_SPACE]:
            Death_reason = 0
        Night = 0

        #1 - Death to Black
        #2 - Death to Green (Door)
        #3 - Death to Green (Mask)
        #4 - Death to Red (Door)
        #5 - Death to Red (Mask)
        #6 - Death to Blue (Mask)
        #7 - Death to Yellow
        #8 - Death to Purple
        #9 - Death to Gray

        sc.fill(DRED)
        f_sys = pygame.font.SysFont('comicsans', 50)
        txt = f_sys.render("U died", True, BLACK)
        sc.blit(txt, (W//2-350, H//2))
        txt = f_sys.render("Space to main menu", True, BLACK)
        sc.blit(txt, (W//2-350, H//2+150))
        f_sys = pygame.font.SysFont('comicsans', 40)
        if Death_reason == 1:
            txt = f_sys.render("Yo, close the door or put mask on next time lol", True, BLACK)
        if Death_reason == 2:
            txt = f_sys.render("Press Q next time BOZO", True, GREEN)
        if Death_reason == 3:
            txt = f_sys.render("You think youre funny? Pathetic..", True, GREEN)
        if Death_reason == 4:
            txt = f_sys.render("TOO SLOW HAHAHAHAHHAHAAHAHAHA", True, RED)
        if Death_reason == 5:
            txt = f_sys.render("Copying my friend? Such a loser you are", True, RED)
        if Death_reason == 6:
            txt = f_sys.render("Okay bro. you have mask for a reason yknow", True, BLUE)
        if Death_reason == 7:
            txt = f_sys.render("I said no mask!", True, YELLOW)
        if Death_reason == 8:
            txt = f_sys.render("Thats it! Im taking away your breathing previleges!", True, PURPLE)
        if Death_reason == 9:
            txt = f_sys.render("I prefer if you keep attention to me, thanks", True, GRAY)
        sc.blit(txt, (10, H//2-150))
        f_sys = pygame.font.SysFont('comicsans', 30)
        pygame.display.update()
        clock.tick(FPS)