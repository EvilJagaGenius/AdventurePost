#APPLE level editor.
#TTG

import pygame, sys, os
from pygame import *

WX = 600
WY = 400
window = pygame.display.set_mode((WX, WY), 0, 32)

def startScreen():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
    pass

def loadLevel():
    directory = os.path.join('..', 'Resources', 'APPLElvls')
    bmpFiles = []
    txtFiles = []
    for i in os.listdir(directory):
        if i.endswith('bmp'):
            bmpFiles.append(i)
        elif i.endswith('txt'):
            txtFiles.append(i)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
    #Select .bmp file
    #Select .txt file
    pass

def newLevel():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
    #Type in the level's name
    pass

def edit():
    while True:
        for event in pygame.event.get:
            if event.type == QUIT:
                DTQuit()
            if event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    clicked = False
                    releaseClick = True
                if event.button == 4:
                    wheelDown = True
                if event.button == 5:
                    wheelUp = True
            if event.type == MOUSEBUTTONDOWN:
                if event.button = 1:
                    clicked = True
