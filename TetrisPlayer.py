import pyautogui
import time
import keyboard

def detectar_ficha():
    image = pyautogui.screenshot("imagen.png")
    px = image.getpixel((2188,1032))
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
    elif keyboard.is_pressed('s'):  # Si se presiona la tecla 'q', detectar la siguiente ficha
        
        time.sleep(0.001)  # Espera corta para evitar la repetición de detecciones
        detectar_ficha()
