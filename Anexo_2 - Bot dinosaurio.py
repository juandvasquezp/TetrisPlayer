import pyautogui
from PIL import ImageGrab, ImageOps
import time
from numpy import array

move = 1.6

class coordinates():
    start_button = (1472, 454)
    dino_limit = (1249, 454)




def start():
    pyautogui.click(coordinates.start_button)

    
    
def jump():
    pyautogui.keyDown('space')
    time.sleep(0.1)
    pyautogui.keyUp('space')
    
    
def hitbox():
    box =(coordinates.dino_limit[0]+50    +move, coordinates().dino_limit[1], 
           coordinates.dino_limit[0] +100  +move, coordinates().dino_limit[1] + 25)
    vision = ImageGrab.grab(box) 
    gray_image = ImageOps.grayscale(vision)
    image_array = array(gray_image.getcolors())
    print(image_array.sum())
    return image_array.sum()


def main ():
    start()
    global move
    while True:
        if(hitbox() != 1497):
           jump()
           time.sleep(0.02)
           move += 2.5;   
           print(move)

main()