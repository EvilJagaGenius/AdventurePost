#APPLE level editor.
#TTG

import pygame, sys, os
from pygame import *

def imgLoad(imgFile, mode):
    if mode == 'i':
        folder = 'ItemImgs'
    elif mode == 's':
        folder = 'SceneImgs'
    elif mode == 'n':
        folder = 'NPC_Imgs'
    elif mode == 'ic':
        folder = 'Icons'
    elif mode == 'a':
        folder = 'APPLEimgs'
    elif mode == 'al':
        folder = 'APPLElvls'
    else:
        folder = None
    if folder != None:
        filePath = os.path.join('..', 'Resources', folder, imgFile)
        returnFile = pygame.image.load(filePath)
        return returnFile

def txtLoad(txtFile, mode):
    if mode == 'n':
        folder = 'NPC_Text'
    elif mode == 'c':
        folder = 'Chapters'
    elif mode == 's':
        folder = 'SaveGames'
    elif mode == 'a':
        folder = 'APPLElvls'
    if folder != None:
        filePath = os.path.join('..', 'Resources', folder, txtFile)
        return filePath



class Level:
    def __init__(self, imgSource, txtSource):
        self.imgSource = imgLoad(imgSource, 'al')
        self.txtSource = open(txtLoad(txtSource, 'a'), 'r')
        self.lvlX = self.imgSource.get_width()
        self.lvlY = self.imgSource.get_height()
        self.blocks = []
        self.monsters = []
        self.healths = []
        self.spikes = []
        self.start = (0,0)
        self.exit = (0,0)
        for x in self.imgSource.get_width():
            for y in self.imgSource.get_height():
                if self.source.get_at((x, y)) == (0,0,0):
                    self.blocks.append(Block('Block', pygame.Rect(x*10, y*10, 10, 10)))
                if self.source.get_at((x, y)) == (0,255,0):
                    self.start = (x*10, y*10)#Spawn point is the green pixel
                if self.source.get_at((x, y)) == (0,0,255):#Exit is the blue pixel
                    self.exit = (x*10, y*10)
                if self.source.get_at((x, y)) == (255,0,0):#Red pixels are wall-running surfaces
                    self.blocks.append(Block('WallRunBlock', pygame.Rect(x*10, y*10, 10, 10)))
                if self.source.get_at((x, y)) == (100,0,0):#Dark red pixels are breakable
                    self.blocks.append(Block('BreakBlock', pygame.Rect(x*10, y*10, 10, 10)))

                if self.source.get_at((x, y)) == (25,0,0):#Red: Up-spike
                    self.spikes.append(Spike(8, (x*10, y*10)))
                if self.source.get_at((x, y)) == (0,25,0):#Green: Left-spike
                    self.spikes.append(Spike(6, (x*10, y*10)))
                if self.source.get_at((x, y)) == (0,0,25):#Blue: Down-spike
                    self.spikes.append(Spike(2, (x*10, y*10)))
                if self.source.get_at((x, y)) == (25,25,25):#Grey: Right-spike
                    self.spikes.append(Spike(4, (x*10, y*10)))
                if self.source.get_at((x, y)) == (0,100,0):
                    self.healths.append(Health(10, (x*10, y*10)))

    def save(self):
        pass

    def loadTxtFile(self):
        pass

    def edit(self):
        selected = None
        clicked = False
        releaseClick = True
        wheelDown = False
        wheelUp = False
        while True:
            self.lvlSurf = pygame.Surface((self.lvlX, self.lvlY))
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
                    if event.button == 1:
                        clicked = True

            for i in self.blocks:
                self.lvlSurf.blit(self.sprite, self.rect)
            for i in self.spikes:
                self.lvlSurf.blit(self.sprite, self.rect)
            for i in self.healths:
                self.lvlSurf.blit(self.sprite, self.rect)
            for i in self.monsters:
                self.lvlSurf.blit(self.sprite, self.rect)


        pygame.display.update()

class Block:
    def __init__(self, kind, rect):
        self.kind = kind
        self.rect = rect
        if self.kind == 'Block':
            self.sprite = imgLoad('BlockSprite.bmp', 'a')
        elif self.kind == 'WallRunBlock':
            self.sprite = imgLoad('WallRunBlock.bmp', 'a')
        elif self.kind == 'BreakBlock':
            self.sprite = imgLoad('HitBlock.bmp', 'a')
        else:
            self.sprite = pygame.Surface(10,10)
            self.sprite.fill((255,255,255))
            
    def stretch(self):
        print('Stretch how far in the X direction?')
        deltaX = int(input())
        print('Stretch how far in the Y direction?')
        deltaY = int(input())
        if self.rect.width - deltaX > 0:
            self.rect.width += deltaX
        else:
            print('Invalid input for X')
        if self.rect.height - deltaY > 0:
            self.rect.height += deltaY
        else:
            print('Invalid input for Y')


class Health:
    def __init__(self, coord):
        self.coord = coord
        self.sprite = imgLoad('Health.bmp', 'a')
        self.sprite.set_colorkey((0,255,0))

class Spike:
    #Don't step on the pointy bits
    #Finished for now...
    def __init__(self, side, position):
        self.sprite = imgLoad('Spike.bmp', 'a').convert()
        self.sprite.set_colorkey((0,255,0))
        if side == 4:
            self.rect = pygame.Rect(position[0]-10, position[1], 20, 10)
        elif side == 6:
            self.sprite = pygame.transform.flip(self.sprite, True, False)
            self.rect = pygame.Rect(position[0], position[1], 20, 10)
        elif side == 2:
            self.sprite = pygame.transform.rotate(self.sprite, 90)
            self.rect = pygame.Rect(position[0], position[1], 10, 20)
        elif side == 8:
            self.sprite = pygame.transform.rotate(self.sprite, 270)
            self.rect = pygame.Rect(position[0], position[1]-10, 10, 20)

class Monster:
    def __init__(self, name, coord, direction, mood, sprite):
        self.name = name
        self.direction = direction
        self.mood = mood
        self.sprite = imgLoad(sprite, 'a')
        self.sprite.set_colorkey(self.sprite.get_at((0,0)))
        self.rect = pygame.Rect(coord[0], coord[1], 


WX = 600
WY = 400
window = pygame.display.set_mode((WX, WY), 0, 32)
