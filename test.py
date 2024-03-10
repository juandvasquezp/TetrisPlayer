import pyautogui
import time
import pygame

"""
time.sleep(5) #sleeps for 5 seconds
pyautogui.keyDown('space') #holds space key down
time.sleep(5) #sleeps for 5 seconds
pyautogui.keyUp('space') #releases the space key
"""

pygame.init()
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            #quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print("S")
