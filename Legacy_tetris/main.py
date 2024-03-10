import pygame,sys
from game import Game
#import keyboard
# from grid import Grid
# from blocks import *

pygame.init()
#dark_blue = (44, 44, 127)

screen = pygame.display.set_mode((300, 600))
pygame.display.set_caption("Python Tetris")

#Será necesario? controla el framerate
clock = pygame.time.Clock()

"""
game_grid = Grid()
game_grid.print_grid()

block = IBlock()
block.move(6, 3)
"""

game = Game()

#eVENTO CUSTOMIAdo, y aigna el valor de userevent
GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 200)

while True:
    #if keyboard.is_pressed('o'):
    #    game.move_left()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            #quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if game.game_over:
                game.reset()
            if event.key == pygame.K_UP and not game.game_over:
                game.rotate()
            if event.key == pygame.K_LEFT and not game.game_over:
                game.move_left()
            if event.key == pygame.K_RIGHT and not game.game_over:
                game.move_right()
            if event.key == pygame.K_DOWN and not game.game_over:
                game.move_down()
            if event.key == pygame.K_SPACE and not game.game_over:
                game.current_block.drop()
        if event.type == GAME_UPDATE and not game.game_over:
            #DELETEME
            game.move_down()
            
    screen.fill((255, 255, 255)) #Tal vez se pueda sacar para optimizar
    """
    game_grid.draw(screen)
    block.draw(screen)
    """
    game.draw(screen)
    pygame.display.update()
    clock.tick(60)