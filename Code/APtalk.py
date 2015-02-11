#Adventure Posts Complete, v6.4 (Windows Version)
#by evil_jaga_genius
#v.6, Like a ninja kick
#To the glory of God
print('Loading APtalk')

#Imports and stuff
import sys, pygame, pyganim, os
from pygame import *
pygame.init()

#Color schemes for APPLE levels.  POWAHI is default.
POWAHI = [(185, 122, 87), (239,228,176)]
ONUWAHI = [(100, 50, 20), (185, 122, 87)]
TAWAHI = [(150, 150, 150), (150, 50, 25)]
LEWAHI = [(15, 100, 30), (50, 25, 10)]
KOWAHI = [(213, 213, 213), (122,167,213)]

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
    elif mode == 'au':
        folder = 'Audio'
    if folder != None:
        filePath = os.path.join('..', 'Resources', folder, txtFile)
        return filePath


#Menu screen and schtuff
def viewCredits():
    theTxt = CutChapter('credits.txt', 'theTxt', '')
    theTxt.play(Player('admin', 0), (0,0))
    return

def newGame():
    name = []
    nameString = ''
    shiftOn = False
    while True:
        window.fill((0,0,0))
        window.blit(txt.render('Type in your name.', True, (255,255,255)), (0,0))
        nameString = ''
        for i in name:
            nameString += i
        window.blit(txt.render(nameString, True, (255,255,255)), (0,50))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_LSHIFT or event.key == K_RSHIFT:
                    shiftOn = True
            if event.type == KEYUP:
                if event.key == K_LSHIFT or event.key == K_RSHIFT:
                    shiftOn = False
                keyName = pygame.key.name(event.key)
                if keyName in 'abcdefghijklmnopqrstuvwxyz1234567890':
                    if shiftOn:
                        keyName = keyName.upper()
                    name.append(keyName)
                elif keyName == 'backspace' and len(name) > 0:
                    del name[-1]
                elif keyName == 'return':
                    open(txtLoad(nameString+'edits.txt', 's'), 'w')
                    return (scenes.chap1, Player(nameString, 0), (0,0))

        pygame.display.update()


def loadGame():
    games = []
    mousePos = pygame.mouse.get_pos()
    for i in os.listdir(os.path.join('..', 'Resources', 'SaveGames')):
        if not i.endswith('edits.txt'):
            if len(games) < 8:
                games.append(i)
    button0 = pygame.Rect(0,0,300,100)
    button1 = pygame.Rect(0,100,300,100)
    button2 = pygame.Rect(0,200,300,100)
    button3 = pygame.Rect(0,300,300,100)
    button4 = pygame.Rect(300,0,300,100)
    button5 = pygame.Rect(300,100,300,100)
    button6 = pygame.Rect(300,200,300,100)
    button7 = pygame.Rect(300,300,300,100)
    buttons = [button0,button1,button2,button3,button4,button5,button6,button7]
    while True:
        mousePos = pygame.mouse.get_pos()
        window.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONUP:
                for b in range(len(buttons)-1):
                    if buttons[b].collidepoint(mousePos):
                        if b < len(games):
                            openGame = open(txtLoad(games[b], 's'), 'r')
                            return (eval(openGame.readline()), eval(openGame.readline()), (0,0))
                        else:
                            return False
        for b in range(len(buttons)-1):
            if buttons[b].collidepoint(mousePos):
                pygame.draw.rect(window,(255,51,0),buttons[b],1)
            else:
                pygame.draw.rect(window,(255,204,102),buttons[b],1)
            if b < len(games):
                window.blit(txt.render(games[b][0:-4],True,(255,255,255)), buttons[b])

        pygame.display.update()


def intro():
    mousePos = pygame.mouse.get_pos()
    state = 'm'
    button0 = pygame.Rect(0,0,300,100)#Start new game
    button1 = pygame.Rect(0,100,300,100)#Load game
    button2 = pygame.Rect(0,200,300,100)#Play as admin (No save)
    button3 = pygame.Rect(0,300,300,100)#Credits
    while True:
        window.fill((0,0,0))
        mousePos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONUP and state == 'm':
                if button0.collidepoint(mousePos):
                    return newGame()
                if button1.collidepoint(mousePos):
                    loadedGame = loadGame()
                    if loadedGame != False:
                        return loadedGame
                if button2.collidepoint(mousePos):
                    return (scenes.chap1, Player('admin', 0), mousePos)
                if button3.collidepoint(mousePos):
                    viewCredits()
        if state == 'm':
            #Display the buttons, make them light up if hovered on.
            window.blit(txt.render('New Game', True, (255,255,255)), button0)
            window.blit(txt.render('Load Game', True, (255,255,255)), button1)
            window.blit(txt.render('Play W/O Saving', True, (255,255,255)), button2)
            window.blit(txt.render('View Credits', True, (255,255,255)), button3)
            if button0.collidepoint(mousePos):
                pygame.draw.rect(window,(255,51,0),button0,1)
            else:
                pygame.draw.rect(window,(204,102,0),button0,1)
            if button1.collidepoint(mousePos):
                pygame.draw.rect(window,(255,51,0),button1,1)
            else:
                pygame.draw.rect(window,(204,102,0),button1,1)
            if button2.collidepoint(mousePos):
                pygame.draw.rect(window,(255,51,0),button2,1)
            else:
                pygame.draw.rect(window,(204,102,0),button2,1)
            if button3.collidepoint(mousePos):
                pygame.draw.rect(window,(255,51,0),button3,1)
            else:
                pygame.draw.rect(window,(204,102,0),button3,1)

        pygame.display.update()

#End schtuff




#Prototype stuff I'm not being bothered to work on

class Player:
    def __init__(self, name, quest, stuff=[]):
        #APTalk stuff
        self.stuff = stuff #That's the stuff
        self.quest = quest #Not quite sure what to do with this variable yet
        self.bar = imgLoad('InventBar.bmp', 'ic').convert()
        self.bar = pygame.transform.scale(self.bar, (WX, 130))
        self.bar.set_colorkey((0, 255, 0))
        self.cBar = imgLoad('palBar.bmp', 'ic').convert()
        self.cBar = pygame.transform.scale(self.cBar, (150,130))
        self.cBar.set_colorkey((0,255,0))
        self.companions = []
        self.viewedCompanion = 0
        self.releasedClick = True

        self.name = name

        #APPLE stuff

        #Sprites and/or animations
        self.standR = pyganim.PygAnimation([(imgLoad('HuxStand.bmp', 'a').convert(), 0.1)])
        self.standL = self.standR.getCopy()
        self.standL.flip(True, False)
        self.jumpR = pyganim.PygAnimation([(imgLoad('HuxJump.bmp' ,'a').convert(), 0.1)])
        self.jumpL = self.jumpR.getCopy()
        self.jumpL.flip(True, False)
        self.WR_R = pyganim.PygAnimation([(imgLoad('HuxWallRun.bmp', 'a').convert(), 0.1)])
        self.WR_L = self.WR_R.getCopy()
        self.WR_L.flip(True, False)
        self.roll1 = imgLoad('HuxRoll.bmp', 'a').convert()
        self.roll2 = pygame.transform.rotate(self.roll1.copy(), -90)
        self.roll3 = pygame.transform.rotate(self.roll1.copy(), -180)
        self.roll4 = pygame.transform.rotate(self.roll1.copy(), -270)
        self.rollR = pyganim.PygAnimation([(self.roll1, 0.1),
                                           (self.roll2, 0.1),
                                           (self.roll3, 0.1),
                                           (self.roll4, 0.1)])
        self.rollL = self.rollR.getCopy()
        self.rollL.flip(True, False)
        self.slideR = pyganim.PygAnimation([(imgLoad('HuxSlide.bmp', 'a').convert(), 0.1)])
        self.slideL = self.slideR.getCopy()
        self.slideL.flip(True, False)
        self.diveR = pyganim.PygAnimation([(imgLoad('HuxDive.bmp', 'a').convert(), 0.1)])
        self.diveL = self.diveR.getCopy()
        self.diveL.flip(True, False)
        #End of sprites.

        self.sprite = self.standR
        self.sprite.set_colorkey((255, 255, 255))
        self.sprite.play()
        #The sprites are NOT pygame.Surface's but pyganim.PygAnimation's.
        #Edit the code accordingly.
        self.lastHeight = self.sprite.getCurrentFrame().get_height()
        self.lastWidth = self.sprite.getCurrentFrame().get_width()
        self.topLeft = (0,0)
        self.rect = pygame.Rect(self.topLeft[0], self.topLeft[1], self.sprite.getCurrentFrame().get_width(), self.sprite.getCurrentFrame().get_height())
        self.points = {}
        self.direction = 'R'
        #self.points is a ring of xy coords that surrounds the player.
        #See shift(), below, for details.
        

    def shift(self, coord, compensate=False):
        #Move the player to a new location on an APPLE level
        coordToShift = coord
        currentHeight = self.sprite.getCurrentFrame().get_height()
        currentWidth = self.sprite.getCurrentFrame().get_width()
        if currentHeight > self.lastHeight:
            #If the current sprite height is taller than the last recorded height, raise the location of self.topLeft accordingly.
            coordToShift = [coordToShift[0], coordToShift[1]-(currentHeight-self.lastHeight)]
        if currentWidth > self.lastWidth and compensate and self.direction == 'R':
            coordToShift = [coordToShift[0]-(currentWidth-self.lastWidth), coordToShift[1]]
        self.topLeft = coordToShift
        self.rect = pygame.Rect(self.topLeft[0], self.topLeft[1], self.sprite.getCurrentFrame().get_width(), self.sprite.getCurrentFrame().get_height())
        self.points.update({1:(self.topLeft[0]+4, self.topLeft[1]+self.rect[3])})
        self.points.update({2:(self.topLeft[0]+self.rect[2]//2, self.topLeft[1]+self.rect[3])})
        self.points.update({3:(self.topLeft[0]+self.rect[2]-4, self.topLeft[1]+self.rect[3])})
        self.points.update({4:(self.topLeft[0], self.topLeft[1]+self.rect[3]//2)})
        self.points.update({5:self.rect.center})
        self.points.update({6:(self.topLeft[0]+self.rect[2], self.topLeft[1]+self.rect[3]//2)})
        self.points.update({7:(self.topLeft[0]+4, self.topLeft[1])})
        self.points.update({8:(self.topLeft[0]+self.rect[2]//2, self.topLeft[1])})
        self.points.update({9:(self.topLeft[0]+self.rect[2]-4, self.topLeft[1])})
        self.points.update({47:(self.topLeft[0], self.topLeft[1]+10)})
        self.points.update({69:(self.topLeft[0]+self.rect[2], self.topLeft[1]+10)})
        #Points 14 and 36 are stair detectors.
        self.points.update({14:(self.topLeft[0], self.topLeft[1]+self.rect[3]-10)})
        self.points.update({36:(self.topLeft[0]+self.rect[2], self.topLeft[1]+self.rect[3]-10)})
        self.lastHeight = currentHeight
        self.lastWidth = currentWidth
        return self.topLeft

    def collides(self, lester):
        #Everything in Lester the List hast to have a 'rect' attribute
        #If a point is touching a Block, the point's number is returned in a list
        hits = []
        for i in lester:
            for j in self.points:
                if i.rect.collidepoint(self.points[j]):
                    hits.append(j)
        return hits

    def dectVoice(self, lester):
        #A lot like collides(), but it returns what exactly you hit instead of which points went off.
        for i in lester:
            for j in self.points:
                if i.rect.collidepoint(self.points[j]):
                    return i
        return None

    def dectDelVoice(self, lester):
        for i in lester:
            for j in self.points:
                if i.delRect.collidepoint(self.points[j]):
                    return i
        return None

    def dectSpikes(self, lester):
        for i in lester:
            if self.rect.collidepoint(i.point):
                return True

    def dectWallRun(self, lester):
        #A dedicated function for detecting wall-running blocks
        for i in lester:
            if i.rect.collidepoint(self.points[5]):
                return True


    def changeSprite(self, changeTo):
        self.sprite = eval('self.'+changeTo)
        self.sprite.set_colorkey(self.sprite.getCurrentFrame().get_at((0,0)))
        self.sprite.play()
        if changeTo[-1] == 'R':
            self.direction = 'R'
        elif changeTo[-1] == 'L':
            self.direction = 'L'


    #More APTalk stuff
    def add(self, item):
        '''Adds an InventoryItem to the inventory, returns bool indicating the item was added'''
        if self.stuff.count(item) < item.maxcount:
            self.stuff.append(item)
            return True
        return False

    def increase(self, item, amount):
        for i in self.stuff:
            if item == i:
                i.amt += amount
        
    def remove(self, item):
        '''Removes one InventoryItem from the inventory, returns bool indicating the item was removed'''
        if self.contains(item):
            self.stuff.remove(item)
            return True
        return False
        
    def contains(self, item):
        '''Returns bool indicating if an InventoryItem is in the inventory'''
        return item in self.stuff
        
    def dispInventory(self, currentScene):
        '''Displays the inventory and the items in it'''
        x = 50
        window.blit(self.bar, (0,0))
        for i in self.stuff:
            i.rect = pygame.Rect(x,10,50,50)
            window.blit(i.sprite, (x, 10))
            if i.rect.collidepoint(pygame.mouse.get_pos()):
                if i.screenName != 'None':
                    window.blit(sTxt.render(i.screenName + '  (' + str(i.amt) + ')', True, (255,255,255)), (WX//2-sTxt.size(i.screenName)[0]//2, 80))
                else:
                    window.blit(sTxt.render(i.name + '  (' + str(i.amt) + ')', True, (255,255,255)), (WX//2-sTxt.size(i.name)[0]//2, 80))
                if True in pygame.mouse.get_pressed():
                    i.use(self, currentScene)
            x += 50

    def dispCompanions(self, currentScene):
        #Note: Companion sprites should blit at (480, 5)
        window.blit(self.cBar, (450,0))
        faceRect = pygame.Rect(480,5,60,60)
        buttonL = pygame.Rect(450,0,25,70)
        buttonR = pygame.Rect(540,0,25,70)
        if self.companions == []:
            window.blit(sTxt.render('No Companions', True, (255,255,255)), (455,75))
        else:
            window.blit(self.companions[self.viewedCompanion].sprite, (480, 5))
            window.blit(sTxt.render(self.companions[self.viewedCompanion].screenName, True, (255,255,255)), (455, 75))
            if True in pygame.mouse.get_pressed():
                if faceRect.collidepoint(pygame.mouse.get_pos()):
                    self.companions[self.viewedCompanion].talk(currentScene, self)
                if buttonL.collidepoint(pygame.mouse.get_pos()) and self.releasedClick:
                    self.releasedClick = False
                    if self.viewedCompanion > 0:
                        self.viewedCompanion -= 1
                    else:
                        self.viewedCompanion = len(self.companions)-1
                if buttonR.collidepoint(pygame.mouse.get_pos()) and self.releasedClick:
                    self.releasedClick = False
                    if self.viewedCompanion < len(self.companions)-1:
                        self.viewedCompanion += 1
                    else:
                        self.viewedCompanion = 0
            else:
                self.releasedClick = True
                
    def addCompanion(self, companion, start=False):
        if companion not in self.companions:
            self.companions.append(companion)
            if not start:
                actuallyWrite = False
                lineToWrite = 'player.addCompanion(scenes.'+companion.name+', True)\n'
                if self.name != 'admin':
                    editFile = open(txtLoad(self.name+'edits.txt', 's'), 'r')
                    lineList = [None]
                    for line in editFile:
                        lineList.append(line.strip())
                    if str(lineList[-1]) + '\n' != lineToWrite:
                        actuallyWrite = True
                    if actuallyWrite:
                        editFile = open(txtLoad(self.name+'edits.txt','s'),'a')
                        editFile.write(lineToWrite)
                    editFile.close()

    def delCompanion(self, companion, start=False):
        self.companions.remove(companion)
        if not start:
            actuallyWrite = False
            lineToWrite = 'player.delCompanion(scenes.'+companion.name+', True)\n'
            if self.name != 'admin':
                editFile = open(txtLoad(self.name+'edits.txt', 's'), 'r')
                lineList = [None]
                for line in editFile:
                    lineList.append(line.strip())
                if str(lineList[-1]) + '\n' != lineToWrite:
                    actuallyWrite = True
                if actuallyWrite:
                    editFile = open(txtLoad(self.name+'edits.txt','s'),'a')
                    editFile.write(lineToWrite)
                editFile.close()


#The rest of the APTalk stuff





def DTquit(player, currentScene):
    saveGame(player, currentScene)
    #Long live the evil geniuses.
    if player.name == 'admin':
        pygame.quit()
        sys.exit()
    else:
        pygame.quit()
        sys.exit()


def saveGame(player, currentScene):
    #Writes a Player() object and the name of the current scene to a text file
    if player.name != 'admin':
        stuffInPack = '['
        fileToWrite = open(txtLoad(player.name+'.txt','s'),'w')
        fileToWrite.write(currentScene + '\n')
        for i in player.stuff:
            stuffInPack += 'scenes.'+i.name+'.setAmt('+str(i.amt)+'),'
        stuffInPack += ']'
        fileToWrite.write('Player("'+player.name+'",'+str(player.quest)+','+stuffInPack +')')
        fileToWrite.close()


#The following global variables are here for convienience, and to prevent the game from hogging too much memory
#So please don't get all angry with my use of them. 

WX = 600
WY = 400
bkgRect = pygame.Rect(0, 0, WX, WY)
window = pygame.display.set_mode((WX, WY), 0, 32)
pygame.display.set_caption('Adventure Posts! [beta v.6.4]')

#This sets the font, large and small
txt = pygame.font.Font(None, 30)
sTxt = pygame.font.Font(None, 16)
cTxt = pygame.font.Font('cour.ttf', 12)
storyTxt = pygame.font.Font('cour.ttf', 13)

window.blit(txt.render('Loading...', True, (255,255,255)), (100, 100))
pygame.display.update()
#Patience, young grasshopper

#gravList is an imporant part in APPLE's jumps
gravList = [6, 6, 7, 7, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1]
chrono = pygame.time.Clock()
exitSprite = imgLoad('ExitBlock.bmp', 'a').convert()


#This loads the arrow picture and the rect it shows up on
arrow = pygame.transform.scale(imgLoad('Arrow.bmp', 'ic').convert(), (50, 50))
arrow.set_colorkey((0, 255, 0))
arrowRect = pygame.Rect(WX-50, WY-50, WX-50, WY-50)

inventButton1 = pygame.Rect(WX-30, 0, 30, 35)
inventButton2 = pygame.Rect(WX-50, 85, 50, 50)
inventoryIcon = pygame.transform.scale(imgLoad('PackIcon.bmp', 'ic').convert(), (50, 35))
inventoryIcon.set_colorkey((0,255,0))
palButton1 = pygame.Rect(530,0,40,40)
palButton2 = pygame.Rect(530,90,40,40)
palIcon = pygame.transform.scale(imgLoad('PalIcon.bmp', 'ic').convert(), (50, 35))
palIcon.set_colorkey((0,255,0))

leftRect=pygame.Rect(0,0,50,WY)
rightRect=pygame.Rect(WX-50,135,50,WY)

#more cursor stuff
sceneCursor = pygame.transform.scale(imgLoad('SceneCursor.bmp', 'ic').convert(), (25, 25))
sceneCursor.set_colorkey((0, 255, 0))
returnCursor = pygame.transform.scale(imgLoad('ReturnCursor.bmp', 'ic').convert(), (25, 25))
returnCursor.set_colorkey((0,255,0))
talkCursor = pygame.transform.scale(imgLoad('TalkCursor.bmp', 'ic').convert(), (25, 25))
talkCursor.set_colorkey((0,255,0))
pickupCursor = pygame.transform.scale(imgLoad('PickupCursor.bmp', 'ic').convert(), (25,25))
pickupCursor.set_colorkey((0,255,0))


#Activate the scene pack
import APPLE
from APPLE import *

import NPCs
from NPCs import *

import items
from items import *

import scenelike
from scenelike import *

import scenes
from scenes import *


print('Done with APtalk, ready to play')

#DO NOT EDIT THE FOLLOWING CODE
if scenes.finished and APPLE.finished:
    data = intro()
    #currentScene = data[0].name

    if data[1].name != 'admin':
        editFile = open(txtLoad(data[1].name + 'edits.txt', 's'), 'r')
        player = data[1]
        for line in editFile:
            exec(line.strip())
        editFile.close()
    while True:
        data = data[0].play(data[1], data[2])
        #currentScene = data[0].name
