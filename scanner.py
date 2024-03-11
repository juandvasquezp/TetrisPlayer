import mss
import mss.tools
from PIL import Image
from blocks import *

##TODO: Finde the correct region for only one screen
# region = {'top': 1032, 'left': 2188, 'width':1 , 'height': 1}
## Only one screen
region = {'top': 278, 'left': 908, 'width': 1, 'height': 1}

class Scanner:
    def __init__(self):
        pass

    def scan(self):
        #image = pyautogui.screenshot("imagen.png", region=())
        with mss.mss() as sct:
            image = sct.grab(region)
            image = Image.frombytes("RGB", image.size, image.bgra, "raw", "BGRX")
        #image = Image.open("imagen.png")

        px = image.getpixel((0,0))
        #print(px)
        if px == (0, 0, 0):
            print("nada")
        elif px == (64, 193, 146):
            #print("I Block")
            return IBlock()
        elif px == (84, 67, 167):
            #print("J Block")
            return JBlock()
        elif px == (167, 67, 157):
            #print("T Block")
            return TBlock()
        elif px == (184, 57, 64):
            #print("Z Block")
            return ZBlock()
        elif px == (192, 167, 62):
            #print("O Block")
            return OBlock()
        elif px == (184, 104, 56):
            #print("L Block")
            return LBlock()
        elif px == (135, 183, 55):
            #print("S Block")
            return SBlock()
        else:
            print("error")