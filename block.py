from colors import Colors
import pygame
from position import Position
class Block:
    def __init__(self, id):
        self.id = id
        self.cells = {}
        #posición del origen (esquina superior izquierda)
        self.row_ofset = 0
        self.column_offset = 0
        #importante 
        self.rotation_state = 0
        self.colors = Colors.get_cell_colors()

    def move(self, row, column):
        self.row_ofset += row
        self.column_offset += column

    def get_cell_positions(self):
        tiles = self.cells[self.rotation_state]
        moved_tiles = []
        for position in tiles:
            moved_tiles.append(Position(position.row + self.row_ofset, position.column + self.column_offset))
        return moved_tiles
    
    def get_center_position(self):
        return Position(self.row_ofset + self.center.row, self.column_offset + self.center.column)
    def rotate(self):
        self.rotation_state = (self.rotation_state + 1) % len(self.cells)

    def undo_rotation(self):
        self.rotation_state = (self.rotation_state - 1) % len(self.cells)

    def rotate_180(self):
        self.rotation_state = (self.rotation_state + 2) % len(self.cells)