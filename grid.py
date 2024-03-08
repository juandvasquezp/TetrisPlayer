import pygame
from colors import Colors

class Grid:
    def __init__(self):
        self.num_rows = 20
        self.num_columns = 10
        self.cell_size = 30
        self.grid = [[0 for j in range(self.num_columns)] for i in range(self.num_rows)]
        self.colors = Colors.get_cell_colors()
    
    def print_grid(self):
        for i in range(self.num_rows):
            for j in range(self.num_columns):
                print(self.grid[i][j], end=" ")
            print()
        print()

    #dibujar cada celda con un color especifico
    def draw(self, screen):
        for row in range(self.num_rows):
            for column in range(self.num_columns):
                #Obtenemos el valor de cada celda
                cell_value = self.grid[row][column]
                cell_rect = pygame.Rect(column * self.cell_size +1, row * self.cell_size +1, self.cell_size - 1, self.cell_size -1)
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)