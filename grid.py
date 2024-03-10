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

    def is_inside(self, row, column):
        x = 0
        y = 0
        if row < 0:
            x = 0 - row
        elif row >= self.num_rows:
            x = self.num_rows - row  - 1
        if column < 0:
            y = 0 - column
        elif column >= self.num_columns:
            y = self.num_columns - column - 1
        return (x, y)

    def is_empty(self, row, column):
        return self.grid[row][column] == 0
    
    ##UTIL PARA EL ALGORITMO
    def is_row_full(self, row):
        for column in range(self.num_columns):
            if self.grid[row][column] == 0:
                return False
        return True

    def move_row_down(self, row, num_rows):
        for column in range(self.num_columns):
            self.grid[row+num_rows][column] = self.grid[row][column]
            self.grid[row][column] = 0
    
    def clear_row(self, row):
        for column in range(self.num_columns):
            self.grid[row][column] = 0

    def clear_full_rows(self):
        completed = 0
        for row in range(self.num_rows-1,0,-1): #Estas dos
            if self.is_row_full(row): # Son el verdadero puntaje la verdad
                self.clear_row(row)
                completed += 1
            elif completed > 0:
                self.move_row_down(row, completed)
        ###ESENCIAL; AQUI ESTA EL VALOR COMPLETED
        return completed


    #dibujar cada celda con un color especifico
    def draw(self, screen):
        for row in range(self.num_rows):
            for column in range(self.num_columns):
                #Obtenemos el valor de cada celda
                cell_value = self.grid[row][column]
                cell_rect = pygame.Rect(column * self.cell_size +1, row * self.cell_size +1, self.cell_size - 1, self.cell_size -1)
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)