#APPLE level editor, v.1
#TTG

import pygame, sys, os
from pygame import *
pygame.init()

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
        
        self.origin = [0,0]
        self.imgSource = imgLoad(imgSource, 'al')
        self.txtSource = txtLoad(txtSource, 'a')
        self.lvlX = self.imgSource.get_width()*10
        self.lvlY = self.imgSource.get_height()*10
        print(self.lvlX)
        print(self.lvlY)
        self.blocks = []
        self.monsters = []
        self.healths = []
        self.spikes = []
        self.start = Start((0,0))
        self.exit = Exit((0,0))
        for x in range(self.imgSource.get_width()):
            for y in range(self.imgSource.get_height()):
                if self.imgSource.get_at((x, y)) == (0,0,0):
                    self.blocks.append(Block('Block', pygame.Rect(x*10, y*10, 10, 10)))
                if self.imgSource.get_at((x, y)) == (0,255,0):
                    self.start = Start((x*10, y*10))#Spawn point is the green pixel
                if self.imgSource.get_at((x, y)) == (0,0,255):#Exit is the blue pixel
                    self.exit = Exit((x*10, y*10))
                if self.imgSource.get_at((x, y)) == (255,0,0):#Red pixels are wall-running surfaces
                    self.blocks.append(Block('WallRunBlock', pygame.Rect(x*10, y*10, 10, 10)))
                if self.imgSource.get_at((x, y)) == (100,0,0):#Dark red pixels are breakable
                    self.blocks.append(Block('BreakBlock', pygame.Rect(x*10, y*10, 10, 10)))

                if self.imgSource.get_at((x, y)) == (25,0,0):#Red: Up-spike
                    self.spikes.append(Spike(8, (x*10, y*10)))
                if self.imgSource.get_at((x, y)) == (0,25,0):#Green: Left-spike
                    self.spikes.append(Spike(6, (x*10, y*10)))
                if self.imgSource.get_at((x, y)) == (0,0,25):#Blue: Down-spike
                    self.spikes.append(Spike(2, (x*10, y*10)))
                if self.imgSource.get_at((x, y)) == (25,25,25):#Grey: Right-spike
                    self.spikes.append(Spike(4, (x*10, y*10)))
                if self.imgSource.get_at((x, y)) == (0,100,0):
                    self.healths.append(Health((x*10, y*10)))
        self.loadTxtFile()
        self.objects = self.blocks + self.monsters + self.spikes + self.healths
        self.objects.append(self.start)
        self.objects.append(self.exit)

    def save(self):
        pass

    def loadTxtFile(self):
        for line in open(self.txtSource, 'r'):
            line = line.strip()
            cmdList = line.split('|')
            if cmdList[0] == '+block':
                print('Adding block')
                self.blocks.append(Block(cmdList[1], pygame.Rect(int(cmdList[2]), int(cmdList[3]), int(cmdList[4]), int(cmdList[5]))))
            elif cmdList[0] == '+monster':
                print('Adding monster')
                self.monsters.append(Monster(cmdList[1], (int(cmdList[2]), int(cmdList[3])), cmdList[4], bool(cmdList[5])))

    def getViewSurf(self, coord):
        viewRect = pygame.Rect(0,0,600,400)
        if (self.lvlX < coord[0] + 600):
            viewRect.left = self.lvlX - 600
        elif not (self.lvlX < coord[0] + 600):
            viewRect.left = coord[0]

        if (self.lvlY < coord[1] + 400):
            viewRect.top = self.lvlY - 400
        elif not (self.lvlY < coord[1] + 400):
            viewRect.top = coord[1]

        viewSurf = self.lvlSurf.subsurface(viewRect)
        return viewSurf
        
    def moveOrigin(self, deltaX, deltaY):
        if (self.origin[0] + deltaX + 600 < self.lvlX) and (self.origin[0] + deltaX > 0):
            self.origin[0] += deltaX
        if (self.origin[1] + deltaY + 400 < self.lvlY) and (self.origin[1] + deltaY > 0):
            self.origin[1] += deltaY

    def edit(self):
        lastMousePos = pygame.mouse.get_pos()
        mousePos = pygame.mouse.get_pos()
        deltaX = 0
        deltaY = 0
        monsters = ['NuiJagaP', 'CCGPunk']
        blocks = ['Block', 'WallRunBlock', 'HitBlock']
        tools = ['move', 'stretch', 'delete']
        usedTool = 0
        selected = None
        leftClicked = False
        releaseLeftClick = True
        rightClicked = False
        releaseRightClick = True
        while True:
            upPress = False
            downPress = False
            leftPress = False
            rightPress = False
            mousePos = pygame.mouse.get_pos()
            deltaX = mousePos[0] - lastMousePos[0]
            deltaY = mousePos[1] - lastMousePos[1]
            
            self.lvlSurf = pygame.Surface((self.lvlX, self.lvlY))
            self.lvlSurf.fill((102, 51, 0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    DTQuit()
                if event.type == MOUSEBUTTONUP:
                    if event.button == 1:
                        leftClicked = False
                        releaseLeftClick = True
                    if event.button == 3:
                        rightClicked = False
                        releaseRightClick = True
                    if event.button == 4:
                        upPress = True
                    if event.button == 5:
                        downPress = True
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        leftClicked = True
                    if event.button == 3:
                        rightClicked = True
                if event.type == KEYUP:
                    if event.key == K_UP:
                        upPress = True
                    if event.key == K_DOWN:
                        downPress = True
                    if event.key == K_LEFT:
                        leftPress = True
                    if event.key == K_RIGHT:
                        rightPress = True

            for i in self.objects:
                self.lvlSurf.blit(i.sprite, i.rect)
                
            if rightClicked:
                self.moveOrigin(deltaX, deltaY)
            if leftClicked:
                for i in self.objects:
                    dectRect = pygame.Rect(i.rect.left - self.origin[0], i.rect.top - self.origin[1], i.rect.width, i.rect.height)
                    if dectRect.collidepoint(mousePos):
                        selected = i
                releaseLeftClick = False

            window.blit(self.getViewSurf(self.origin), (0,0))
            if selected != None:
                window.blit(txt.render(selected.name + str(selected.rect), True, (255,255,255)), (0,0))
                pygame.draw.rect(window, (0,255,0), pygame.Rect(selected.rect.left - self.origin[0], selected.rect.top - self.origin[1], selected.rect.width, selected.rect.height), 1)
            else:
                window.blit(txt.render('Nothing selected', True, (255,255,255)), (0,0))

            window.blit(txt.render(str(mousePos), True, (255,255,255)), (0, 25))
            lastMousePos = mousePos
            
            pygame.display.update()

class Block:
    def __init__(self, kind, rect):
        self.name = kind
        self.rect = rect
        if self.name == 'Block':
            self.sprite = imgLoad('BlockSprite.bmp', 'a')
        elif self.name == 'WallRunBlock':
            self.sprite = imgLoad('WallRunBlock.bmp', 'a')
        elif self.name == 'BreakBlock':
            self.sprite = imgLoad('HitBlock.bmp', 'a')
        else:
            self.sprite = pygame.Surface(10,10)
            self.sprite.fill((255,255,255))
        self.sprite = pygame.transform.scale(self.sprite, (self.rect.width, self.rect.height))
            
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
        self.name = 'Health'
        self.rect = pygame.Rect(coord[0], coord[1], 10, 10)
        self.sprite = imgLoad('Health.bmp', 'a')
        self.sprite.set_colorkey((0,255,0))

class Spike:
    #Don't step on the pointy bits
    #Finished for now...
    def __init__(self, side, position):
        self.name = 'Spike'
        self.sprite = imgLoad('Spike.bmp', 'a').convert()
        self.sprite.set_colorkey((0,255,0))
        if side == 4:
            self.name += '-4'
            self.rect = pygame.Rect(position[0]-10, position[1], 20, 10)
        elif side == 6:
            self.name += '-6'
            self.sprite = pygame.transform.flip(self.sprite, True, False)
            self.rect = pygame.Rect(position[0], position[1], 20, 10)
        elif side == 2:
            self.name += '-2'
            self.sprite = pygame.transform.rotate(self.sprite, 90)
            self.rect = pygame.Rect(position[0], position[1], 10, 20)
        elif side == 8:
            self.name += '-8'
            self.sprite = pygame.transform.rotate(self.sprite, 270)
            self.rect = pygame.Rect(position[0], position[1]-10, 10, 20)

class Monster:
    def __init__(self, name, coord, direction, mood):
        self.name = name
        self.direction = direction
        self.mood = mood
        self.sprite = imgLoad(name+'.bmp', 'a')
        self.sprite.set_colorkey(self.sprite.get_at((0,0)))
        self.rect = pygame.Rect(coord[0], coord[1], self.sprite.get_width(), self.sprite.get_height())

class Start:
    def __init__(self, coord):
        self.name = 'Player'
        self.rect = pygame.Rect(coord[0], coord[1], 20, 40)
        self.sprite = imgLoad('HuxStand.bmp', 'a')

    def move(self):
        print('\nCoords will be rounded to 10.')
        newX = input('New X coord:')
        newY = input('New Y coord:')
        if newX != '':
            newX = int(newX[0:-1] + '0')
            self.rect.left = newX
        if newY != '':
            newY = int(newY[0:-1] + '0')
            self.rect.top = newY

class Exit:
    def __init__(self, coord):
        self.name = 'Exit'
        self.rect = pygame.Rect(coord[0], coord[1], 20, 20)
        self.sprite = imgLoad('ExitBlock.bmp', 'a')

    def move(self):
        print('\nCoords will be rounded to 10.')
        newX = input('New X coord:')
        newY = input('New Y coord:')
        if newX != '':
            newX = int(newX[0:-1] + '0')
            self.rect.left = newX
        if newY != '':
            newY = int(newY[0:-1] + '0')
            self.rect.top = newY


def DTQuit():
    pygame.quit()
    sys.exit()



print(".bmp file name")
bmpFile = 'Level2.bmp'#input()
print(".txt file name")
txtFile = 'Level2.txt'#input()
print('Loading...')

WX = 600
WY = 400
window = pygame.display.set_mode((WX, WY), 0, 32)
txt = pygame.font.Font('cour.ttf', 20)
txt.set_bold(True)

level = Level(bmpFile, txtFile)
level.edit()
