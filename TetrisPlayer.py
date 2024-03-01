import pyautogui
import time
import keyboard
import mss
import mss.tools
from PIL import Image

##TODO: Finde the correct region for only one screen
region = {'top': 1032, 'left': 2188, 'width':1 , 'height': 1}


prev_s_pressed = False


class TetrisBoard:
    def __init__(self, board):
        self.board = [[0 for x in range(20)] for y in range(10)] # 10 columnas y 20 filas

    def calculateMinimumColumnPossition(self,column):
        for i in range(20):
            if self.board[column][i] == 1:
                return i-1

    def clearRow(self, row):
        for i in range(10):
            del self.board[i][row]
            self.board[i] = [0] + self.board[i]
    
    


def detectar_ficha():
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
        print("barra")
    elif px == (84, 67, 167):
        print("L invertida")
    elif px == (167, 67, 157):
        print("T")
    elif px == (187, 163, 62):
        print("espacio")
    elif px == (184, 57, 64):
        print("S invertida")
    elif px == (192, 167, 62):
        print("cuadrado")
    elif px == (184, 104, 56):
        print("L")
    elif px == (135, 183, 55):
        print("S")
    else:
        print("error")

while True:
    if keyboard.is_pressed('p'):  # Si se presiona la tecla 'p', salir del bucle
        break
    if keyboard.is_pressed('s') and not prev_s_pressed:
        detectar_ficha()  # Detectar la ficha
        prev_s_pressed = True  # Actualizar el estado previo de la tecla 's'
    elif not keyboard.is_pressed('s'):  # Si la tecla 's' no está presionada
        prev_s_pressed = False  # Actualizar el estado previo de la tecla 's'