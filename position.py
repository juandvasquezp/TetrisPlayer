class Position:
    def __init__(self, row, column):
        self.row = row
        self.column = column
class Iteration:
    def __init__(self, position, rotation_state):
        self.position = position #gets start position
        self.rotattion_state = rotation_state