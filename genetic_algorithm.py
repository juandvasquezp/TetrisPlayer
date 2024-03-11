from main import Game

class genetic_algorithm:

    def __init__(self):
        self.agregate_height_coefficient = -0.510066
        self.complete_lines_coefficient = 0.760666
        self.holes_coefficient = -0.35663
        self.bumpiness_coefficient = -0.184483
        # self.score_coefficient = 0.760666
    
    def test_current_block_iterations(self, block):
        