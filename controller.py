import pyautogui
import time
import random

class Controller:
    def __init__(self, game):
        self.game = game

    def go_to_iteration(self, iteration):
        self.rotate_to_iteration(iteration.rotation_state)
        self.move_to_iteration(iteration.position)

    def rotate_to_iteration(self, rotation_state):
        if rotation_state == 0:
            pass
        elif rotation_state == 1:
            pyautogui.keyDown('right')
            self.game.rotate()
            self.random_sleep()
            pyautogui.keyUp('right')
            self.random_sleep()
        elif rotation_state == 2:
            pyautogui.keyDown('up')
            self.game.rotate_180()
            self.random_sleep()
            pyautogui.keyUp('up')
            self.random_sleep()
        elif rotation_state == 3:
            pyautogui.keyDown('left')
            self.game.rotate_left()
            self.random_sleep()
            pyautogui.keyUp('left')
            self.random_sleep()

    def move_to_iteration(self, position):
        spawn_position_column = self.game.current_block.spawn_position.column
        iteration_column = position.column

        moves = iteration_column - spawn_position_column

        if moves > 0:
            for i in range(moves):
                pyautogui.keyDown('d')
                self.short_sleep()
                pyautogui.keyUp('d')
                self.game.move_right()
                print("moving right")
                self.random_sleep()

        elif moves < 0:
            for i in range(abs(moves)):
                pyautogui.keyDown('a')
                self.short_sleep()
                pyautogui.keyUp('a')
                self.game.move_left()
                print("moving left")
                self.random_sleep()
        
        pyautogui.keyDown('s')
        self.game.drop()
        self.short_sleep()
        pyautogui.keyUp('s')
        self.random_sleep()

    def random_sleep(self):
        ms = random.randint(100, 150)
        time.sleep(ms / 1000)

    def random_short_sleep(self):
        ms = random.randint(10, 20)
        time.sleep(ms / 1000)