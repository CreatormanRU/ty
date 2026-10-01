import random
def door_leftYN(a=0,b=0,c=0):
    if b >= 5 or c >= 6:
        a = 1
    else:
        a = 0
    return a

def door_rightYN(door=0,black=0):
    if black >= 4:
        door = 1
    else:
        door = 0
    return door

def Maskconfig(mask=0,blue=0,yellow=0,camflip=0):
    if blue >= 6:
        if yellow == 1:
            if camflip == 1:
                camflip = 0
            else:
                camflip = 1
        else:
            mask = 1
            camflip = 0
    else:
        mask = 0
    return mask, camflip

def Graywindup(mask,camflip,graystate,graymax,graycam,cam):
    if mask == 0:
        if graystate <= 400:
            camflip = 1
        if camflip == 1:
            if cam != graycam:
                cam = random.randint(1,10)
            else:
                if graymax > graystate:
                    graystate += 5
                else:
                    camflip = 0
        else:
            camflip = 0
    else:
        pass
    return graystate,camflip,cam #windupleft,cameras,cam
