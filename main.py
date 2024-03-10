import time
import keyboard
import sys
from game import Game

game = Game()

#Start program
while True:
    if keyboard.is_pressed('p'):
        game.set_current_block()
        time.sleep(2)
        break

prev_s_pressed = False
while True:
    if keyboard.is_pressed('q'):  # Si se presiona la tecla 'p', salir del bucle
        sys.exit()
        break
    if keyboard.is_pressed('s') and not prev_s_pressed:
        game.set_current_block()  # Detectar la ficha
        prev_s_pressed = True  # Actualizar el estado previo de la tecla 's'
        game.grid.print_grid()    
    elif not keyboard.is_pressed('s'):  # Si la tecla 's' no está presionada
        prev_s_pressed = False  # Actualizar el estado previo de la tecla 's'