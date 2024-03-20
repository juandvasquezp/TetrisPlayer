import time, keyboard, sys

from game import Game
from genetic_algorithm import genetic_algorithm
from controller import Controller

game = Game()
genetic_algorithm = genetic_algorithm(game)
controller = Controller(game)

print("Bienvenido al bot, para continuar presione 'p'")
print("Si quiere entrar en modo scanner, presione 'o'")

def wait_for_game_start():
    px = game.scanner.scan_and_print()
    while True:
        if px != game.scanner.scan_and_print():
            break

def run_bot():
    while True:
        if keyboard.is_pressed('q'):  # Si se presiona la tecla 'p', salir del bucle
            sys.exit()
            break

        if not game.game_over:
            iteration = genetic_algorithm.test_current_block_iterations()
            controller.go_to_iteration(iteration)
            # game.grid.print_grid()
            
    
def scanner_mode():
    from scanner import Scanner
    scanner = Scanner()
    o_pressed = False  # Flag to track if 'o' key has been pressed
    while True:
        if keyboard.is_pressed('q'):  # Si se presiona la tecla 'p', salir del bucle
            sys.exit()
            break
        elif keyboard.is_pressed('o') and not o_pressed:  # Check if 'o' key is pressed and flag is False
            o_pressed = True
            scanner.scan_and_print()
        elif not keyboard.is_pressed('o'):  # Reset flag when 'o' key is released
            o_pressed = False


#Start program
while True:
    if keyboard.is_pressed('p'):
        game.set_current_block()
        wait_for_game_start()
        run_bot()
        break

    if keyboard.is_pressed('o'): #Entar en modo scanner
        scanner_mode()
        break