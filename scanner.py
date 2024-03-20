import mss
import mss.tools
from PIL import Image
from blocks import *
from colors import Colors

##TODO: Finde the correct region for only one screen
# region = {'top': 1032, 'left': 2188, 'width':1 , 'height': 1}
## Only one screen
# region = {'top': 278, 'left': 908, 'width': 1, 'height': 1}
## Two screen Edge with configs
# region = {'top': 1020, 'left': 2179, 'width': 1, 'height': 1}
## One screen Edge with configs
region = {'top': 266, 'left': 899, 'width': 1, 'height': 1}

class Scanner:
    def __init__(self):
        self.colors = Colors.get_cell_colors()
        self.color_i_block = self.colors[1]
        self.color_j_block = self.colors[2]
        self.color_t_block = self.colors[3]
        self.color_z_block = self.colors[4]
        self.color_o_block = self.colors[5]
        self.color_l_block = self.colors[6]
        self.color_s_block = self.colors[7]
        pass

    def scan(self):
        #image = pyautogui.screenshot("imagen.png", region=())
        with mss.mss() as sct:
            image = sct.grab(region)
            image = Image.frombytes("RGB", image.size, image.bgra, "raw", "BGRX")
        #image = Image.open("imagen.png")

        px = image.getpixel((0,0))
        #print(px)
        #print("Pixel con valor: ", px)
        if px == (0, 0, 0):
            print("nada")
        elif px == self.color_i_block:
            #print("I Block")
            return IBlock()
        elif px == self.color_j_block:
            #print("J Block")
            return JBlock()
        elif px == self.color_t_block:
            #print("T Block")
            return TBlock()
        elif px == self.color_z_block:
            #print("Z Block")
            return ZBlock()
        elif px == self.color_o_block:
            #print("O Block")
            return OBlock()
        elif px == self.color_l_block:
            #print("L Block")
            return LBlock()
        elif px == self.color_s_block:
            #print("S Block")
            return SBlock()
        else:
            print("error")
    
    def scan_and_print(self):
        with mss.mss() as sct:
            image = sct.grab(region)
            image = Image.frombytes("RGB", image.size, image.bgra, "raw", "BGRX")
        
        px = image.getpixel((0,0))
        # print(px)
        return px