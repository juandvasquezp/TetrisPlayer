import pygame,sys
from grid import Grid
from blocks import *

pygame.init()
#dark_blue = (44, 44, 127)

screen = pygame.display.set_mode((300, 600))
pygame.display.set_caption("Python Tetris")

#Será necesario? controla el framerate
clock = pygame.time.Clock()

game_grid = Grid()
game_grid.print_grid()

block = IBlock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            #quit()
            sys.exit()
    screen.fill((255, 255, 255)) #Tal vez se pueda sacar para optimizar
    game_grid.draw(screen)
    block.draw(screen)
    pygame.display.update()
    clock.tick(60)