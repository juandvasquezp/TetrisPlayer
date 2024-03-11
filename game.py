from grid import Grid
from blocks import *
import random
from scanner import Scanner
class Game:
    def __init__(self):
        self.grid = Grid()
        self.scanner = Scanner()
        #DELETEME
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        #Tal vez se pueda usar esto??
        #TODO
        self.current_block = self.set_current_block()
        self.game_over = False

    def move_down(self):
        self.current_block.move(1, 0)
        if (correction := self.block_inside()) != (0, 0):
            self.current_block.move(correction[0], correction[1])
            self.lockblock()
            return False
        #En serio que no me gusta este block_fits, si puedo cambiarlo en el futuro lo haré, sin embargo sirve para lo que quiero, solo un drop
        if not self.block_fits():
            self.current_block.move(-1, 0)
            self.lockblock()
            return False
        return True
    
    def lockblock(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            self.grid.grid[tile.row][tile.column] = self.current_block.id

        #TODO
        self.set_current_block()
        self.grid.clear_full_rows()

        ##No mes gusta, si cambias el blockfits, debes cambiar esta logica
        if not self.block_fits():
            self.game_over = True
            


    def block_fits(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.is_empty(tile.row, tile.column) == False:
                return False
        return True

    #MUCH BETTER COMMAND
    """
    def block_fits(self):
        tiles = self.current_block.get_cell_positions()
        center = self.current_block.get_center_position()
        x_correct_offset = 0
        y_correct_offset = 0
        for tile in tiles:
            center_x_distance = tile.column - center.column
            center_y_distance = tile.row - center.row
            if self.grid.is_empty(tile.row, tile.column):
                continue
            else:
                if abs(center_x_distance) > abs(x_correct_offset):
                    x_correct_offset = center_x_distance
                if abs(center_y_distance) > abs(y_correct_offset):
                    y_correct_offset = center_y_distance
        return (-x_correct_offset, -y_correct_offset)
    """
    def rotate(self):
        self.current_block.rotate()
        if (correction := self.block_inside()) != (0, 0):
            self.current_block.move(correction[0], correction[1])
        if not self.block_fits():
            self.current_block.undo_rotation()

    def drop(self):
        while True:
            if not self.move_down():
                break
        # self.current_block.move(-1, 0)


    # Better blockinside command
    def block_inside(self):
        tiles = self.current_block.get_cell_positions()
        x_correct_offset = 0
        y_correct_offset = 0
        for tile in tiles:
            values = self.grid.is_inside(tile.row, tile.column)
            if abs(values[0]) > abs(x_correct_offset):
                x_correct_offset = values[0]
            if abs(values[1]) > abs(y_correct_offset):
                y_correct_offset = values[1]
        return (x_correct_offset, y_correct_offset)

    def set_current_block(self):
        self.current_block = self.scanner.scan()

    #DELETEME

    """
    def reset(self):
        self.grid = Grid()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.game_over = False
    """
