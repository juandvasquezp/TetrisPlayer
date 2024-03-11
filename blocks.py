from block import Block
from position import Position, Iteration

class IBlock(Block):
    def __init__(self):
        super().__init__(id = 1)
        self.cells = {
            0: [Position(1, 0), Position(1, 1), Position(1, 2), Position(1, 3)],
            1: [Position(0, 2), Position(1, 2), Position(2, 2), Position(3, 2)],
            2: [Position(2, 0), Position(2, 1), Position(2, 2), Position(2, 3)],
            3: [Position(0, 1), Position(1, 1), Position(2, 1), Position(3, 1)]
        }
        self.iterations = self.fill_iterations()
        #Tal vez el move se pueda quitar, recordar que aquí no esperamos que se mueva por parte del usuario, sino evaluamos todo, y esto se hace mejor manualmente
        self.center = Position(1.5, 1.5) ##Recordar que esto tiene que ver con la cuadricula
        # self.move(-1, 3)
        self.spawn_position = Position(-1, 3)
        # print("Iblock spawned")
    def fill_iterations(self):
        iterations = []
        #position 0
        for i in range(7):
            iterations.append(Iteration(Position(-1, i), 0))
        #position 1:
        for i in range(3, 8):
            iterations.append(Iteration(Position(0, i), 1))
        #position 3
        for i in range(-1, 4):
            iterations.append(Iteration(Position(0, i), 3))

        return iterations
    
    
class JBlock(Block):
    def __init__(self):
        super().__init__(id = 2)
        self.cells = {
            0: [Position(0, 0), Position(1, 0), Position(1, 1), Position(1, 2)],
            1: [Position(0, 1), Position(0, 2), Position(1, 1), Position(2, 1)],
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 2)],
            3: [Position(0, 1), Position(1, 1), Position(2, 0), Position(2, 1)]
        }
        self.center = Position(1, 1)
        self.iterations = self.fill_iterations()
        # self.move(0, 3)
        self.spawn_position = Position(0, 3)
        # print("Jblock spawned")

    def fill_iterations(self):
        iterations = []
        #position 0
        for i in range(8):
            iterations.append(Iteration(Position(0, i), 0))
        #position 1:
        for i in range(-1, 8):
            iterations.append(Iteration(Position(0, i), 1))
        #position 2:
        for i in range(8):
            iterations.append(Iteration(Position(0, i), 2))
        #position 3
        for i in range(0, 9):
            iterations.append(Iteration(Position(0, i), 3))

        return iterations

class TBlock(Block):
    def __init__(self):
        super().__init__(id = 3)
        self.cells = {
            0: [Position(0, 1), Position(1, 0), Position(1, 1), Position(1, 2)],
            1: [Position(0, 1), Position(1, 1), Position(1, 2), Position(2, 1)],
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 1)],
            3: [Position(0, 1), Position(1, 0), Position(1, 1), Position(2, 1)]
        }
        self.center = Position(1, 1)
        self.iterations = self.fill_iterations()
        # self.move(0, 3)
        self.spawn_position = Position(0, 3)
        # print("Tblock spawned")

    def fill_iterations(self):
        iterations = []
        #position 0
        for i in range(8):
            iterations.append(Iteration(Position(0, i), 0))
        #position 1:
        for i in range(-1, 8):
            iterations.append(Iteration(Position(0, i), 1))
        #position 2:
        for i in range(8):
            iterations.append(Iteration(Position(0, i), 2))
        #position 3
        for i in range(0, 9):
            iterations.append(Iteration(Position(0, i), 3))

        return iterations

class ZBlock(Block):
    def __init__(self):
        super().__init__(id = 4)
        self.cells = {
            0: [Position(0, 0), Position(0, 1), Position(1, 1), Position(1, 2)],
            1: [Position(0, 2), Position(1, 1), Position(1, 2), Position(2, 1)],
            2: [Position(1, 0), Position(1, 1), Position(2, 1), Position(2, 2)],
            3: [Position(0, 1), Position(1, 0), Position(1, 1), Position(2, 0)]
        }
        self.center = Position(1, 1)
        self.iterations = self.fill_iterations()
        # self.move(0, 3)
        self.spawn_position = Position(0, 3)
        # print("Zblock spawned")
    
    def fill_iterations(self):
        iterations = []
        #position 0
        for i in range(8):
            iterations.append(Iteration(Position(0, i), 0))
        #position 1:
        for i in range(3, 8):
            iterations.append(Iteration(Position(0, i), 1))
        #position 2:
        for i in range(8):
            iterations.append(Iteration(Position(0, i), 2))
        #position 3
        for i in range(0, 4):
            iterations.append(Iteration(Position(0, i), 3))

        return iterations

class OBlock(Block):
    def __init__(self):
        super().__init__(id = 5)
        self.cells = {
            0: [Position(0, 0), Position(0, 1), Position(1, 0), Position(1, 1)]
        }
        self.center = Position(0.5, 0.5)
        self.iterations = self.fill_iterations()
        # self.move(0, 4)
        self.spawn_position = Position(0, 4)
        # print("Oblock spawned")
    
    def fill_iterations(self):
        iterations = []
        #position 0
        for i in range(9):
            iterations.append(Iteration(Position(0, i), 0))
        return iterations

class LBlock(Block):
    def __init__(self):
        super().__init__(id = 6)
        self.cells = {
            0: [Position(0, 2), Position(1, 0), Position(1, 1), Position(1, 2)],
            1: [Position(0, 1), Position(1, 1), Position(2, 1), Position(2, 2)],
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 0)],
            3: [Position(0, 0), Position(0, 1), Position(1, 1), Position(2, 1)]
        }
        self.center = Position(1, 1)
        self.iterations = self.fill_iterations()
        # self.move(0, 3)
        self.spawn_position = Position(0, 3)
        # print("Lblock spawned")
    
    def fill_iterations(self):
        iterations = []
        #position 0
        for i in range(8):
            iterations.append(Iteration(Position(0, i), 0))
        #position 1:
        for i in range(-1, 8):
            iterations.append(Iteration(Position(0, i), 1))
        #position 2:
        for i in range(8):
            iterations.append(Iteration(Position(0, i), 2))
        #position 3
        for i in range(0, 9):
            iterations.append(Iteration(Position(0, i), 3))

        return iterations

class SBlock(Block):
    def __init__(self):
        super().__init__(id = 7)
        self.cells = {
            0: [Position(0, 1), Position(0, 2), Position(1, 0), Position(1, 1)],
            1: [Position(0, 1), Position(1, 1), Position(1, 2), Position(2, 2)],
            2: [Position(1, 1), Position(1, 2), Position(2, 0), Position(2, 1)],
            3: [Position(0, 0), Position(1, 0), Position(1, 1), Position(2, 1)]
        }
        self.center = Position(1, 1)
        self.iterations = self.fill_iterations()
        # self.move(0, 3)
        self.spawn_position = Position(0, 3)
        # print("Sblock spawned")
    
    def fill_iterations(self):
        iterations = []
        #position 0
        for i in range(8):
            iterations.append(Iteration(Position(0, i), 0))
        #position 1:
        for i in range(3, 8):
            iterations.append(Iteration(Position(0, i), 1))
        #position 2:
        for i in range(8):
            iterations.append(Iteration(Position(0, i), 2))
        #position 3
        for i in range(0, 4):
            iterations.append(Iteration(Position(0, i), 3))

        return iterations