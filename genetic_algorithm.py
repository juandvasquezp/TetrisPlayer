from math import inf

class genetic_algorithm:

    def __init__(self, game):
        self.agregate_height_coefficient = -0.510066
        self.complete_lines_coefficient = 0.760666
        self.holes_coefficient = -0.35663
        self.bumpiness_coefficient = -0.184483
        self.game = game
        # self.score_coefficient = 0.760666
    
    def test_current_block_iterations(self):
        max_score = -inf
        for iteration in self.game.current_block.iterations:
            self.game.current_block.rotation_state = iteration.rotation_state
            self.game.current_block.row_ofset = iteration.position.row
            self.game.current_block.column_offset = iteration.position.column
            
            self.game.simulate_drop()

            score = self.calculate_grid_score()
            if score > max_score:
                max_score = score
                good_iteration = iteration

        self.game.reset_block_position()

        print("Besti iteration is to rotate to position " + str(good_iteration.rotation_state) + " and move to column " + str(good_iteration.position.column) + " and row " + str(good_iteration.position.row))
        return good_iteration

    def calculate_grid_score(self):
        agregate_height = self.game.grid.agregate_height
        complete_lines = self.game.grid.complete_lines
        holes = self.game.grid.holes
        bumpiness = self.game.grid.bumpiness

        score = 0

        score = agregate_height * self.agregate_height_coefficient
        score += complete_lines * self.complete_lines_coefficient
        score += holes * self.holes_coefficient
        score += bumpiness * self.bumpiness_coefficient

        return score