import time, keyboard, sys

from game import Game
from genetic_algorithm import genetic_algorithm
from controller import Controller

game = Game()
genetic_algorithm = genetic_algorithm(game)
controller = Controller(game)

#Start program
while True:
    if keyboard.is_pressed('p'):
        game.set_current_block()
        time.sleep(2)
        break

while True:
    if keyboard.is_pressed('q'):  # Si se presiona la tecla 'p', salir del bucle
        sys.exit()
        break

    if not game.game_over:
        iteration = genetic_algorithm.test_current_block_iterations()
        controller.go_to_iteration(iteration)
        # game.grid.print_grid()
        
        