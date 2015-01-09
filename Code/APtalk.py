#Adventure Posts Complete, v6.4 (Windows Version)
#by evil_jaga_genius
#v.6, Like a ninja kick
#To the glory of God

#Activate the scene pack
import scenes
from scenes import *

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
    if folder != None:
        filePath = os.path.join('..', 'Resources', folder, txtFile)
        return filePath

class Companion:
    def __init__(self, name, fileName, sprite, screenName):
        #A lot like an NPC, except they travel around with you
        self.sprite = pygame.transform.scale(imgLoad(sprite, 'n'), (50,65)).convert()
        self.sprite.set_colorkey(self.sprite.get_at((0,0)))
        self.words = open(txtLoad(fileName, 'n'))
        self.name = name
        self.screenName = screenName
        self.part = 0

        self.words = []
        txtPath = txtLoad(fileName, 'n')
        for line in open(txtPath, 'r'):
            self.words.append(line.strip())

    def follow(self, player):
        #You're being followed... DUN DUN DUN
        player.addCompanion(self)
        return True

    def leave(self, player):
        player.delCompanion(self)
        return True

    def getLine(self, part):
        '''Takes the beginning part of a line in the words file (e.g "O") and returns the string that follows it.'''
        #g = general, preface specific words with the desired scene name, e.g "scenes.greatMine1~Are we there yet?"
        #addCmds is a string to execute, preface multiple commands with "exec( *command* )"
        #...you know what, you get the idea...
        for line in self.words:
            if line.startswith(part):
                line = line.split(part + '~')
                line = ''.join(line)
                line = line.split('|')
                return line
        return False

    def talk(self, currentScene, player):
        #...he won't shut up AAUGH
        faceRect = pygame.Rect(480,5,60,60)
        blahRect = pygame.Rect(0,0,450,100)
        bkg = window.copy()
        clicked = False
        mousePos = pygame.mouse.get_pos()
        clicks = 0
        while True:
            window.blit(bkg, (0,0))
            blah = pygame.Surface((450,90))
            blah.set_alpha(200)
            blah.fill((100, 100, 100))
            if self.getLine(currentScene) != False:
                line = self.getLine(currentScene)
            else:
                line = self.getLine('g')

            for event in pygame.event.get():
                if event.type == QUIT:
                    DTquit(player)
                if event.type == MOUSEBUTTONUP:
                    clicked = True
                    clicks += 1

            if clicked:
                if faceRect.collidepoint(mousePos) and clicks > 1:
                    self.part = 0
                    return
                elif blahRect.collidepoint(mousePos) and self.part < len(line)-1:
                    self.part += 1

            
            words = line[self.part].split(' ')

            #Insert code which displays the text here
            y = 0
            x = 0
            for i in words:
                
                txtSurf = txt.render(i, True, (0,0,0))
                if x + txtSurf.get_width() < blah.get_width():
                    blah.blit(txtSurf, (x,y))
                    x += txtSurf.get_width()+5
                else:
                    x = 0
                    y += 20
                    blah.blit(txtSurf, (x,y))
                    x += txtSurf.get_width()+10
                
            mousePos = pygame.mouse.get_pos()                    
            clicked = False
            window.blit(blah, (0,0))
            if self.getLine('addCmds') != False:
                exec(self.getLine('addCmds')[0])
            pygame.display.update()

    def editWords(self, newFile, player):
        self.words = []
        lineToWrite = "scenes."+self.name+".startEdits('"+newFile+"')\n"
        actuallyWrite = False
        for line in open(txtLoad(newFile, 'n'), 'r'):
            self.words.append(line.strip())
        #The following code documents the edit
        if player.name != 'admin':
            editFile = open(txtLoad(player.name+'edits.txt', 's'), 'r')
            lineList = [None]
            for line in editFile:
                lineList.append(line.strip())
            if str(lineList[-1]) + '\n' != lineToWrite:
                actuallyWrite = True
            if actuallyWrite:
                editFile = open(txtLoad(player.name+'edits.txt','s'),'a')
                editFile.write(lineToWrite)
            editFile.close()

    def startEdits(self, newFile):
        self.words = []
        for line in open(txtLoad(newFile, 'n'), 'r'):
            self.words.append(line.strip())

#Special items
class PiatarasLetter:
    def __init__(self):
        self.sprite = pygame.transform.scale(imgLoad('PiatarasLetter.bmp', 'i'), (50,50))
        self.sprite.set_colorkey((255,0,0))
        self.name = "Piataras_Letter"
        self.screenName = "Piatara's Letter"
        self.amt = 1
        self.maxcount = 1

    def use(self, player, currentScene):
        if currentScene == 'Onepu':
            scenes.Onepu.state = 'o'
            scenes.Onepu.part = 0
            scenes.Onepu.editWords('onepu2.txt', player)
        elif currentScene == 'Jala':
            scenes.Jala.state = 'o'
            scenes.Jala.part = 0
            scenes.Jala.editWords('jala2.txt', player)
            scenes.Onepu.editWords('onepu3.txt', player)

    def setAmt(self, junk):
        return self

class Empty_Bottle:
    def __init__(self):
        self.sprite = pygame.transform.scale(imgLoad('EmptyBottle.bmp', 'i'), (50,50))
        self.sprite.set_colorkey((0,255,0))
        self.name = 'Empty_Bottle'
        self.screenName = 'Empty Bottle'
        self.amt = 1
        self.maxcount = 1

    def use(self, player, currentScene):
        if (currentScene == 'scenes.onuKoro4') or(currentScene == 'scenes.onuKoro5') or (currentScene == 'scenes.onuKoro6'):
            player.add(scenes.Water_Bottle)
            player.remove(self)

    def setAmt(self, junk):
        return self

class Water_Bottle:
    def __init__(self):
        self.sprite = pygame.transform.scale(imgLoad('WaterBottle.bmp', 'i').convert(), (50,50))
        self.sprite.set_colorkey((0,255,0))
        self.name = 'Water_Bottle'
        self.screenName = 'Bottle of Water'
        self.maxcount = 1
        self.amt = 1

    def use(self, player, currentScene):
        if (currentScene == 'scenes.lightMine7') or (currentScene == 'Kaj'):
            player.add(scenes.Pure_Water)
            player.remove(self)

    def setAmt(self, junk):
        return self

class Pure_Water:
    def __init__(self):
        self.sprite = pygame.transform.scale(imgLoad('PureWater.bmp', 'i').convert(), (50,50))
        self.sprite.set_colorkey((0,255,0))
        self.name = 'Pure_Water'
        self.screenName = 'Bottle of Pure Water'
        self.maxcount = 1
        self.amt = 1

    def use(self, player, currentScene):
        if (currentScene == 'Dashka'):
            scenes.Dashka.editWords('dashka3.txt', player)
            scenes.Dashka.state='o'
            scenes.Dashka.part = 0
            player.remove(self)

    def setAmt(self, junk):
        return self

#End special items

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



class Lock:
    #Combination lock
    def __init__(self, realCombination, name, tries=-1):
        self.tries = tries
        self.realCombo = str(realCombination)
        self.name = 'scenes.'+name
                 
    def play(self, player, junkCoord):
        tries = self.tries
        combo = []
        comboString = ''
        shiftOn = False
        solved = False
        failed = False
        while True:
            window.fill((0,0,0))
            window.blit(storyTxt.render('Type in a ' + str(len(self.realCombo)) + ' -digit combination, press ENTER to test, press ESC to exit.', True, (255,255,255)), (0,0))
            comboString = ''
            for i in combo:
                comboString += i
            window.blit(storyTxt.render(comboString, True, (255,255,255)), (0,50))
            for event in pygame.event.get():
                if event.type == QUIT:
                    DTquit(player)
                if event.type == KEYDOWN:
                    if event.key == K_LSHIFT or event.key == K_RSHIFT:
                        shiftOn = True
                if event.type == KEYUP:
                    if event.key == K_LSHIFT or event.key == K_RSHIFT:
                        shiftOn = False
                    if event.key == K_ESCAPE:
                        return (self.failTarget, player, pygame.mouse.get_pos())
                    keyName = pygame.key.name(event.key)
                    if keyName in '1234567890':
                        if shiftOn:
                            keyName = keyName.upper()
                        if failed:
                            failed = False
                        combo.append(keyName)
                    elif keyName == 'backspace' and len(combo) > 0:
                        del combo[-1]
                    elif keyName == 'return':
                        if comboString == self.realCombo:
                            solved = True
                        else:
                            combo = []
                            comboString = ''
                            failed = True
                            tries -= 1

            if failed:
                window.blit(storyTxt.render('Try a different combination.', True, (255,255,255)), (0,100))
                if tries > 0:
                    window.blit(storyTxt.render(str(tries) + ' tries left', True, (255,255,255)), (0,125))

            if solved:
                return (self.winTarget, player, pygame.mouse.get_pos())

            if tries == 0:
                return (self.failTarget, player, pygame.mouse.get_pos())
                
            pygame.display.update()

    def addTargets(self, winTarget, failTarget):
        self.winTarget = winTarget
        self.failTarget = failTarget

class CutChapter:
    def __init__(self, txtFile, name, addCmds=''):
        #This deserves some explanation, so I'll try my best.
#I can't do animation to save my life.  But I can write stories.  That's why
#I joined the BMPRPG.  What this does is instead of showing a cutscene to
#advance the story, is show a text file--a story, a "chapter", if you will.
#That said, txtFile is a string for your desired story's file name.
#endScene is where you end up after you exit the story.
#name is the name you give the variable so you can load your game correctly.
#addCmds is a string that will be executed at the end of viewing the story, left blank by default.
        filePath = txtLoad(txtFile, 'c')
        self.txt = open(filePath, 'r')
        #Code will create a surface containing the story's text
        self.storySurf = pygame.Surface((600, 400))
        self.storySurf.fill((0,0,0))
        self.endScene = None
        x = 0
        y = 0
        for pg in self.txt: #pg for paragraph, paragraphs will look like they're all on one line in the .txt file
            pg = pg.split(' ')
            for word in pg:
                if word.endswith('\n'):
                    word = word[0:-1]
                    if storyTxt.size(word)[0] <= WX-x:
                        self.storySurf.blit(storyTxt.render(word, True, (255,255,255)), (x,y))
                        x += storyTxt.size(word)[0] + 5
                    else:
                        x = 0
                        if y > WY-36:
                            self.extend()
                        y += 18
                        self.storySurf.blit(storyTxt.render(word, True, (255,255,255)), (x,y))
                        x += storyTxt.size(word)[0] + 5
                    if y > WY-36:
                        self.extend()
                    y += 18
                    x = 0
                else:
                    if storyTxt.size(word)[0] <= WX-x:
                        self.storySurf.blit(storyTxt.render(word, True, (255,255,255)), (x,y))
                        x += storyTxt.size(word)[0] + 5
                    else:
                        x = 0
                        if y > WY-36:
                            self.extend()
                        y += 18
                        self.storySurf.blit(storyTxt.render(word, True, (255,255,255)), (x,y))
                        x += storyTxt.size(word)[0] + 5
                    
        #End story code
        self.addCmds = addCmds
        self.name = 'scenes.' + name


    def extend(self):
        #Extends self.storySurf by 18 pixels down.
        height = self.storySurf.get_height()
        saveSurf = self.storySurf.copy()
        self.storySurf = pygame.Surface((600, height+18))
        self.storySurf.fill((0,0,0))
        self.storySurf.blit(saveSurf, (0,0))

    def addTarget(self, target):
        self.endScene = target

    def play(self, player, junkCoord):
        viewPoint = 0
        viewRect = pygame.Rect(0,0,600,400)
        viewSurf = pygame.Surface((0,0))
        while True:
            moveUp = False
            moveDown = False
            for event in pygame.event.get():
                if event.type == QUIT:
                    DTquit(player)
                if event.type == KEYUP:
                    if event.key == K_RETURN:
                        exec(self.addCmds)
                        return (self.endScene, player, pygame.mouse.get_pos())
                    if event.key == K_UP:
                        moveUp = True
                    if event.key == K_DOWN:
                        moveDown = True
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 4:
                        moveUp = True
                    if event.button == 5:
                        moveDown = True

            if moveUp and viewPoint >= 18:
                viewPoint -= 18
            if moveDown and viewPoint < (self.storySurf.get_height()-400):
                viewPoint += 18

            viewRect = pygame.Rect(0,viewPoint,600,400)
            viewSurf = self.storySurf.subsurface(viewRect)
            window.blit(viewSurf, (0,0))
            
                    
            pygame.display.update()
            

#Prototype stuff I'm not being bothered to work on

class NuiJagaP:
    #My usernamesake the Jaga
    #Has a sprite, can move from side to side.
    #NTS: Give it stinging and goober-throwing attacks.
    def __init__(self, coord, direction, angry=False):
        self.spawn = coord
        self.startDirection = direction
        self.startMood = angry
        self.spriteL = imgLoad('NuiJagaP.bmp', 'a').convert()
        self.spriteL.set_colorkey((0,255,0))
        self.spriteR = pygame.transform.flip(self.spriteL, True, False).convert()
        self.sprite = self.spriteL
        self.rect = pygame.Rect(coord[0], coord[1], self.sprite.get_width(), self.sprite.get_height())
        self.KOd = False
        if angry:
            self.angry = True
        else:
            self.angry = False
        self.direction = direction
        self.pointL = (self.rect.left, self.rect.bottom -5)
        self.pointR = (self.rect.right, self.rect.bottom -5)
        self.pointD = (self.rect.center[0], self.rect.bottom +1)
        

    def move(self, target, blocks):
        touching = self.collides(blocks)
        if self.direction == 'l':
            self.sprite = self.spriteL
        if self.direction == 'r':
            self.sprite = self.spriteR
        if self.angry and 'D' in touching:
            if (target[0] < self.rect.center[0]) and 'L' not in touching:
                self.direction = 'l'
                self.rect.left -= 1
            elif (target[0] > self.rect.center[0]) and 'R' not in touching:
                self.direction = 'r'
                self.rect.left += 1
        elif (self.direction == 'r' and target[0] > self.rect.center[0]) or (self.direction == 'l' and target[0] < self.rect.center[0]):
            self.angry = True
        self.pointL = (self.rect.left, self.rect.bottom -5)
        self.pointR = (self.rect.right, self.rect.bottom -5)

    def collides(self, lester):
        touchList = []
        for i in lester:
            if i.rect.collidepoint(self.pointR):
                touchList.append('R')
            elif i.rect.collidepoint(self.pointL):
                touchList.append('L')
            elif i.rect.collidepoint(self.pointD):
                touchList.append('D')
        return touchList

    def revive(self):
        self.KOd = False
        self.rect = pygame.Rect(self.spawn[0], self.spawn[1], self.sprite.get_width(), self.sprite.get_height())
        self.angry = self.startMood
        self.direction = self.startDirection
        
class CCGPunk:
    #Kylae the Shadow Matoran, trying to blow up the Great Mine
    #The CCG is a hitscan weapon
    def __init__(self, coord, junkDirection, junkMood):
        self.spawn = coord
        self.spriteR = imgLoad('Kylae.bmp', 'a').convert()
        self.spriteR.set_colorkey((255,255,255))
        self.spriteL = pygame.transform.flip(self.spriteR, True, False).convert()
        self.spriteL.set_colorkey((255,255,255))
        self.sprite = self.spriteR
        self.rect = pygame.Rect(coord[0], coord[1], self.sprite.get_width(), self.sprite.get_height())
        self.pointD = (self.rect.center[0], self.rect.bottom)
        self.targetPoint = (0,0)

    def collides(self, blocks):
        for i in blocks:
            if i.rect.collidepoint(self.pointD):
                return True
        
    def move(self, target, blocks):
        self.targetPoint = target
        if self.targetPoint[0] < self.pointD[0]:
            self.sprite = self.spriteL
        elif self.targetPoint[0] > self.pointD[0]:
            self.sprite = self.spriteR
        if not self.collides(blocks):
            self.rect.top += 6
            self.pointD = (self.rect.center[0], self.rect.bottom)
        else:
            return 'restart'

    def revive(self):
        self.rect = pygame.Rect(self.spawn[0], self.spawn[1], self.sprite.get_width(), self.sprite.get_height())
        self.pointD = (self.rect.center[0], self.rect.bottom)
        self.targetPoint = (0,0)
    
class MoveBlock:
    #Blocks that move toward a certain point at a certain speed.
    def __init__(self, startPoint, endPoint, speed, repeat=True, stepTrigger=True):
        self.sprite = imgLoad('MoveBlock.bmp', 'a').convert()
        self.startPoint = startPoint
        self.endPoint = endPoint
        self.speed = speed
        #This is gonna be a pain
        pass

    def move(self):
        pass



class Slope:
    #Eventually, you could specify two points in the level and this makes a slope between them
    #Numerous parkour uses left to the reader's imagination
    def __init__(self, pointA, pointB):
        pass

#The Rama Brothers, Speedy and Sneaky
class NuiRamaG:
    #Sneaky the green Rama
    def __init__(self):
        #What to do:
        #Give it the ability to hover through walls, become transparent
        #Quickly attack and hover out of range
        #Grab the player and drop them... somewhere.  On spikes or down holes.
        #CANNOT attack while flying
        pass

class NuiRamaO:
    #Speedy the orange Rama
    def __init__(self):
        #What to do:
        #Let it attack while flying
        #Go on berserker charges for the player
        #Hurricane Charge:  wait for five seconds, then teleport across the player and do immense damage.
        #Does less damage than Sneaky, but moves faster
        #CANNOT go through walls
        pass

#End prototypes

class Spike:
    #Don't step on the pointy bits
    #Finished for now...
    def __init__(self, side, position):
        self.sprite = imgLoad('Spike.bmp', 'a').convert()
        self.sprite.set_colorkey((0,255,0))
        if side == 4:
            self.point = (position[0]-11, position[1]+6)
            self.rect = pygame.Rect(position[0]-10, position[1], 20, 10)
        elif side == 6:
            self.sprite = pygame.transform.flip(self.sprite, True, False)
            self.point = (position[0]+21, position[1]+6)
            self.rect = pygame.Rect(position[0], position[1], 20, 10)
        elif side == 2:
            self.sprite = pygame.transform.rotate(self.sprite, 90)
            self.point = (position[0]+5, position[1]+20)
            self.rect = pygame.Rect(position[0], position[1], 10, 20)
        elif side == 8:
            self.sprite = pygame.transform.rotate(self.sprite, 270)
            self.point = (position[0]+5, position[1]-11)
            self.rect = pygame.Rect(position[0], position[1]-10, 10, 20)

class Health:
    #Berries that heal you in a level
    #Finished for now...
    def __init__(self, health, coord):
        self.sprite = imgLoad('Health.bmp', 'a').convert()
        self.sprite.set_colorkey((0,255,0))
        self.health = health
        self.coord = coord



class Voice:
    def __init__(self, rect, string, delRect):
        '''Text that shows up in an APPLE level when the player walks in the corresponding Rect()'''
        if sprite != None:
            self.sprite = sprite
        else:
            self.sprite = pygame.Surface((0,0))
        self.string = string
        self.rect = rect
        self.delRect = delRect #delRect is where the voice is deleted.


class Meelee:
    #Not quite sure what to do with this yet... bashing blocks and Jaga
    #Also needs LOTS of improvement
    def __init__(self, rect):
        self.rect = rect

    def move(self, newPoint):
        self.point = newPoint

    def remove(self):
        del(self)

class Block:
    def __init__(self, rect, colorScheme=POWAHI):
        '''These are the blocks that compose the Level they are in.'''
        self.sprite = pygame.transform.scale(imgLoad('BlockSprite.bmp', 'a'), (rect.width, rect.height)).convert()
        self.type = 's'
        for x in range(self.sprite.get_width()):
            for y in range(self.sprite.get_height()):
                if self.sprite.get_at((x, y)) == (0,0,0):
                    self.sprite.set_at((x, y), colorScheme[0])
                if self.sprite.get_at((x, y)) == (100,100,100):
                    self.sprite.set_at((x, y), colorScheme[1])
        self.rect = rect

class WallRunBlock:
    def __init__(self, rect, colorScheme=POWAHI):
        '''These wall-running surfaces allow the player to run in midair with very low gravity.'''
        self.sprite = imgLoad('WallRunBlock.bmp', 'a').convert()
        self.type = 'p'
        for x in range(self.sprite.get_width()):
            for y in range(self.sprite.get_height()):
                if self.sprite.get_at((x, y)) == (0,0,0):
                    self.sprite.set_at((x, y), colorScheme[0])
                if self.sprite.get_at((x, y)) == (100,100,100):
                    self.sprite.set_at((x, y), colorScheme[1])
        self.rect = rect

class BreakBlock:
    def __init__(self, rect, colorScheme=POWAHI):
        '''Blocks that can be broken apart by punches, kicks and disk throws'''
        #Needs improvement, set the health of the block
        self.sprite = imgLoad('HitBlock.bmp', 'a').convert()
        self.type = 's'
        for x in range(self.sprite.get_width()):
            for y in range(self.sprite.get_height()):
                if self.sprite.get_at((x, y)) == (0,0,0):
                    self.sprite.set_at((x, y), colorScheme[0])
                if self.sprite.get_at((x, y)) == (100,100,100):
                    self.sprite.set_at((x, y), colorScheme[1])
        self.rect = rect

    def kaboom(self, lester):
        #Because I couldn't use the word 'break'
        lester.remove(self)
        
class exitBlock:
    def __init__(self, rect):
        self.rect = rect

class Level: #Platformer levels.  Tap 'E' to see the FPS you're running at, should average at 60
    def __init__(self, imgName, name, txtFile, bkg=None, colorScheme=POWAHI):
        '''Takes a bitmap (.bmp) image and converts it into a level.'''
        if bkg != None:
            self.bkg = imgLoad(bkg, 's').convert()
        else:
            self.bkg = pygame.Surface((10,10))
        self.source = imgLoad(imgName, 'al').convert()
        self.blocks = []
        self.wallRuns = []
        self.breaks = []
        self.voices = []
        self.beasties = []
        self.spikes = []
        self.healths = []
        self.target = None
        self.name = 'scenes.' + name
        self.colorScheme = colorScheme
        for x in range(self.source.get_width()):
            for y in range(self.source.get_height()):
                if self.source.get_at((x, y)) == (0,0,0):
                    self.blocks.append(Block(pygame.Rect(x*10, y*10, 10, 10), colorScheme))
                if self.source.get_at((x, y)) == (0,255,0):
                    self.start = (x*10, y*10)#Spawn point is the green pixel
                if self.source.get_at((x, y)) == (0,0,255):#Exit is the blue pixel
                    self.exitBlock = exitBlock(pygame.Rect(x*10, y*10, 20, 20))
                if self.source.get_at((x, y)) == (255,0,0):#Red pixels are wall-running surfaces
                    self.wallRuns.append(WallRunBlock(pygame.Rect(x*10, y*10, 10, 10), colorScheme))
                if self.source.get_at((x, y)) == (100,0,0):#Dark red pixels are breakable
                    self.breaks.append(BreakBlock(pygame.Rect(x*10, y*10, 10, 10), colorScheme))

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
        self.lvlSurf = pygame.Surface((self.source.get_width()*10, self.source.get_height()*10))
        self.lvlX = self.lvlSurf.get_width()
        self.lvlY = self.lvlSurf.get_height()

        self.bkg = pygame.transform.scale(self.bkg, (self.lvlX, self.lvlY))
        darker = pygame.Surface((self.lvlX, self.lvlY))
        darker.fill((0,0,0))
        darker.set_alpha(50)
        self.bkg.blit(darker, (0,0))
        self.txtFile = txtLoad(txtFile, 'a')

    def loadTxtFile(self):
        '''Shorthand:
+block
+monster
+voice

do exactly what you'd think they'd do.
        '''
        for line in open(self.txtFile, 'r'):
            line = line.strip()
            cmdList = line.split('|')
            if cmdList[0] == '+block':
                self.blocks.append(Block(pygame.Rect(int(cmdList[1]), int(cmdList[2]), int(cmdList[3]), int(cmdList[4])), self.colorScheme))
            if cmdList[0] == '+monster':
                self.beasties.append(eval(cmdList[1])((int(cmdList[2]), int(cmdList[3])), cmdList[4], bool(cmdList[5])))
            if cmdList[0] == '+voice':
                pass

    def addMonster(self, monster):
        self.beasties.append(monster)
        return True

    def addTarget(self, target):
        #Make sure you eventually call this on every level
        self.target = target
    
    def addVoice(self, voice):
        self.voices.append(voice)

    def getViewSurf(self, coord):
        viewRect = pygame.Rect(0,0,600,400)
        if (self.lvlX < coord[0] + 300) and (coord[0] - 300 > 0):
            viewRect.left = self.lvlX - 600
        elif not (self.lvlX < coord[0] + 300) and (coord[0] - 300 > 0):
            viewRect.left = coord[0] - 300
                
        if (self.lvlY < coord[1] + 200) and (coord[1] - 200 > 0):
            viewRect.top = self.lvlY - 400
        elif not (self.lvlY < coord[1] + 200) and (coord[1] - 200 > 0):
            viewRect.top = coord[1] - 200

        viewSurf = self.lvlSurf.subsurface(viewRect)
        return viewSurf

    def play(self, player, junkCoord):
        #Setting variables, blah blah blah
        #I actually made a level and saved the game so I can't leave until I finish work on the platformer
        self.loadTxtFile()
        
        
        playerHealth = 100
        upMomentum = 0
        framePause = 3
        jumpFrame = 0
        jumpSpeed = 9
        fallingTime = 0
        lowGrav = False
        shieldFrames = 0
        shielded = False
        rollFrames = 0
        rollDir = None
        fallingDamageTime = 60
        fallingDamageFactor = 4
        releaseDown = True
        downTaps = 0
        diving = False

        
        editMode = False
        gravity = 0
        moveSpeed = 2
        lvlX = self.lvlSurf.get_width()
        lvlY = self.lvlSurf.get_height()
        player.shift(self.start)
        playerCoord = list(self.start)
        jumping = False
        rising = False
        doubleJump = False
        releaseJump = True
        leftPress = False
        rightPress = False
        moveLeft = False
        moveRight = False
        moveDown = False
        moveUp = False
        parkour = False
        spacePress = False
        fPress = False
        releaseF = True
        releaseSpace = True
        shiftPress = False
        player.shift(playerCoord)
        while True:

            #Generate the hitList.  Where the player is being touched by blocks.
            touchList = self.blocks + self.spikes+ self.breaks
            hits = []
            hitList = player.collides(touchList)
            
            self.lvlSurf.blit(self.bkg, (0,0))
            for i in self.healths:
                self.lvlSurf.blit(i.sprite, i.coord)
                if player.rect.collidepoint(i.coord):
                    if playerHealth < 100:
                        if playerHealth <= 90:
                            playerHealth += i.health
                            self.healths.remove(i)
                        else:
                            playerHealth = 100
                            self.healths.remove(i)
            for i in self.blocks:
                self.lvlSurf.blit(i.sprite, i.rect)
            for i in self.wallRuns:
                self.lvlSurf.blit(i.sprite, i.rect)
            for i in self.breaks:
                self.lvlSurf.blit(i.sprite, i.rect)
            for i in self.beasties:
                self.lvlSurf.blit(i.sprite, i.rect)
                if i.move(playerCoord, touchList) == 'restart':
                    self.reset()
                    return (self, player, (0,0))
                    
            for i in self.spikes:
                self.lvlSurf.blit(i.sprite, i.rect)

        
            for event in pygame.event.get():
                if event.type == QUIT:
                    DTquit(player)
                if event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        leftPress = True
                    if event.key == K_RIGHT:
                        rightPress = True
                    if event.key == K_UP:
                        moveUp = True
                    if event.key == K_DOWN:
                        moveDown = True
                    if event.key == K_SPACE:
                        spacePress = True
                    if event.key == K_LSHIFT:
                        shiftPress = True
                    if event.key == K_f:
                        fPress = True
                if event.type == KEYUP:
                    if event.key == K_LEFT:
                        leftPress = False
                    if event.key == K_RIGHT:
                        rightPress = False
                    if event.key == K_UP:
                        moveUp = False
                        releaseJump = True
                    if event.key == K_DOWN:
                        moveDown = False
                        releaseDown = True
                    if event.key == K_SPACE:
                        spacePress = False
                        releaseSpace = True
                    if event.key == K_LSHIFT:
                        shiftPress = False
                    if event.key == K_f:
                        fPress = False
                        releaseF = True
                    if event.key == K_e:
                        editMode = not editMode

        
            #Shields activated when injured
            if shieldFrames > 0:
                shielded = True
                shieldFrames -= 1
            else:
                shielded = False
                        
            #Running at its most basic form
            if shiftPress:
                moveSpeed = 3
            elif not shiftPress:
                moveSpeed = 2

            if moveUp and ((1 in hitList) or (2 in hitList) or (3 in hitList)) and releaseJump:
                #Starts a single jump
                jumping = True
                upMomentum = jumpSpeed
                releaseJump = False
            elif not moveUp and ((1 in hitList) or (2 in hitList) or (3 in hitList)):
                #Resets the jumping when you land on some Blocks
                jumping = False
                jumpFrame = 0

            if (7 in hitList) or (8 in hitList) or (9 in hitList):
                #Stops rising as soon as you hit your head on more Blocks
                upMomentum = 0
                jumping = False
                
            if jumping: #What actually makes the player rise
                jumpFrame += 1
                if upMomentum > -3:
                    if jumpFrame % framePause == 0:
                        #jumpFrame is divisible by framePause (default: 2)
                        upMomentum -= 1
                    if upMomentum < 0 and lowGrav:
                        upMomentum = 0

                    
            if upMomentum > gravity:
                rising = True
            else:  #rising only tells APPLE you're moving up
                rising = False
                fallingTime += 1
                #Used to determine when to reduce gravity when you're sliding down a wall
            

            if moveUp and releaseJump and (not doubleJump) and ((1 not in hitList) and (2 not in hitList) and (3 not in hitList)):
                #Repeats the jump code if you're in the air and bash UP again
                fallingTime = 0
                doubleJump = True
                releaseJump = False
                jumping = True
                upMomentum = jumpSpeed

            if 6 in hitList:
                compensate = True
            else:
                compensate = False

            #Moving along the X-axis and handling stairs
            if moveRight and (6 not in hitList) and (69 not in hitList):
                playerCoord[0] += moveSpeed
                player.changeSprite('standR')
                player.direction = 'R'
                if 36 in hitList:
                    playerCoord[1] -= 10
            if moveLeft and (4 not in hitList) and (47 not in hitList):
                playerCoord[0] -= moveSpeed
                player.changeSprite('standL')
                player.direction = 'L'
                if 14 in hitList:
                    playerCoord[1] -= 10

           
            if spacePress and releaseSpace and parkour == False:
                #Bouncing off walls
                if (4 in hitList):
                    moveLeft = False
                    moveRight = True
                    parkour = True
                    releaseSpace = False
                    jumping = True
                    upMomentum = jumpSpeed
                    fallingTime = 0
                if (6 in hitList):
                    moveRight = False
                    moveLeft = True
                    parkour = True
                    releaseSpace = False
                    jumping = True
                    upMomentum = jumpSpeed
                    fallingTime = 0

            if ((6 in hitList) or (4 in hitList)):
                if spacePress and releaseSpace and ((1 not in hitList) or (2 not in hitList) or (3 not in hitList)):
                    parkour = False #Reset parkour when you bounce off a wall.

            if (1 in hitList) or (2 in hitList) or (3 in hitList):
                #Don't fall if there are Blocks beneath you, and reset doubleJump.
                if parkour or fallingTime > 60 or diving: #Roll on landing
                    if leftPress and moveDown:
                        moveLeft = True
                        moveRight = False
                        rollFrames = 30
                        rollDir = 'L'
                    elif rightPress and moveDown:
                        moveRight = True
                        moveLeft = False
                        rollFrames = 30
                        rollDir = 'R'
                    else:
                        moveLeft = False
                        moveRight = False
               
                #Falling damage
                if fallingTime > fallingDamageTime and not lowGrav and not shielded:
                    playerHealth -= fallingTime//fallingDamageFactor
                    shieldFrames = 60
                    shielded = True
                #Reset variables
                downTaps = 0
                diving = False
                fallingTime = 0
                gravity = 0
                doubleJump = False
                jumpFrame = 0
                if upMomentum < 0:
                    upMomentum = 0
                
                parkour = False
                player.changeSprite('stand'+player.direction)
                

            #Are there no blocks beneath you?  Too bad...
            elif (1 not in hitList) and (2 not in hitList) and (3 not in hitList):
                player.changeSprite('jump'+player.direction)# Happy bouncing Huki
                if not diving:
                    if (6 in hitList or 4 in hitList) and (moveRight or moveLeft) and not rising:
                        gravity = 1 #Sliding down a wall
                    elif (player.dectWallRun(self.wallRuns)) and spacePress and shiftPress:
                        gravity = 1 #Wall-Running
                        player.changeSprite('WR_'+player.direction)
                        parkour = True
                    else:
                        gravity = 3

            #Sliding down a wall, continued
            if gravity == 1:
                lowGrav = True
                fallingTime = 0
            else:
                lowGrav = False

            #Tap DOWN twice to dive down
            if moveDown and releaseDown:
                releaseDown = False
                downTaps += 1

            if downTaps > 1:
                diving = True

            if diving:
                gravity = 6
                player.changeSprite('dive' + player.direction)
                if moveUp:
                    diving = False
                    downTaps = 0

            #Exiting the level
            if player.collides([self.exitBlock]) != []:
                self.reset()
                return (self.target, player, (0,0))

            #Hitting things.  Will need improvement.
            if fPress and releaseF:
                if player.direction == 'R':
                    hits.append(Meelee(pygame.Rect((playerCoord[0]+player.rect[2]+5, playerCoord[1]-10, 20, 20))))
                elif player.direction == 'L':
                    hits.append(Meelee(pygame.Rect((playerCoord[0]-5, playerCoord[1]-10, 20, 20))))
                releaseF = False

            for i in hits:
                for j in self.breaks:
                    if j.rect.colliderect(i.rect):
                        j.kaboom(self.breaks)

            #Spikes
            if player.dectSpikes(self.spikes) and not shielded:
                playerHealth -= 25
                shielded = True
                shieldFrames = 60


            #Dealing with voices.
            voice = player.dectVoice(self.voices)
            delVoice = player.dectDelVoice(self.voices)

            if delVoice != None:
                self.voices.remove(delVoice)

            #Displaying health, and later, weapons and ammo
            dataSurf = pygame.Surface((150, 50))
            dataSurf.fill((102,51,0))
            dataSurf.blit(cTxt.render(str(playerHealth) + '% Health', False, (255,255,255)), (0,0))
            dataSurf.blit(cTxt.render('Weapon: None', False, (255,255,255)), (0,12))
            dataSurf.blit(cTxt.render('Ammo: 999x99 Reloads', False, (255,255,255)), (0,24))

            if playerHealth <= 0: #Oh noes
                self.reset()
                return (self, player, (0,0))
            
            #Slide down a wall at 1 pixel per frame
            if not jumping or (lowGrav and upMomentum < 0):
                upMomentum = 0

            #Sliding, the basics
            if shiftPress and moveDown and not diving:
                player.changeSprite('slide'+player.direction)

            #Rolling
            if rollFrames > 0:
                player.changeSprite('roll' + player.direction)
                rollFrames -= 1
                if rollDir == 'R':
                    moveRight = True
                    moveLeft = False
                if rollDir == 'L':
                    moveLeft = True
                    moveRight = False
            else:
                rollDir = None

            #If you crouch on landing, you take less damage
            #On the other hand, if you dive-bomb the floor, you're gonna take more damage...
            if moveDown:
                fallingDamageTime = 120
                fallingDamageFactor = 8
            elif diving:
                fallingDamageTime = 45
                fallingDamageFactor = 4
            else:
                fallingDamageTime = 60
                fallingDamageFactor = 6

            
            #More motion on the X-axis, don't execute if you're rolling
            if not parkour and rollFrames <= 0:
                if leftPress:
                    moveLeft = True
                if rightPress:
                    moveRight = True
                if not rightPress:
                    moveRight = False
                if not leftPress:
                    moveLeft = False

           
            #Moving the player, blitting things, etc.
            
            playerCoord[1] -= upMomentum
            playerCoord[1] += gravity
            playerCoord = player.shift(playerCoord, compensate)
            if shieldFrames % 2 == 0:
                player.sprite.blit(self.lvlSurf, (playerCoord[0], playerCoord[1]))
            self.lvlSurf.blit(exitSprite, self.exitBlock)
            viewSurf = self.getViewSurf(playerCoord)
            if editMode:
                #Note: the fps clock may not be accurate.
                #If anyone knows a good way to get a loop's iterations per second, let me know
                viewSurf.blit(txt.render(str(int(chrono.get_fps())), True, (255,51,0)), (100,100))
                viewSurf.blit(txt.render(str(playerCoord), True, (255,51,0)), (100,120))
            viewSurf.blit(dataSurf, (0,350))

            window.blit(viewSurf, (0,0))
            if voice != None:
                toBlit = cTxt.render(voice.string, False, (255,255,255),(0,0,0))
                window.blit(toBlit, (0,0))

            
            pygame.display.update()
            chrono.tick(60)

    def reset(self):
        #Copied a bunch of code from the __init__() function, but the levels reset now
        self.blocks = []
        self.wallRuns = []
        self.breaks = []
        self.voices = []
        self.delVoices = []
        self.spikes = []
        self.healths = []
        for i in self.beasties:
            i.revive()
        for x in range(self.source.get_width()):
            for y in range(self.source.get_height()):
                if self.source.get_at((x, y)) == (0,0,0):
                    self.blocks.append(Block(pygame.Rect(x*10, y*10, 10, 10), self.colorScheme))
                if self.source.get_at((x, y)) == (0,255,0):
                    self.start = (x*10, y*10)#Spawn point is the green pixel
                if self.source.get_at((x, y)) == (0,0,255):#Exit is the blue pixel
                    self.exitBlock = exitBlock(pygame.Rect(x*10, y*10, 20, 20))
                if self.source.get_at((x, y)) == (255,0,0):#Red pixels are wall-running surfaces
                    self.wallRuns.append(WallRunBlock(pygame.Rect(x*10, y*10, 10, 10), self.colorScheme))
                if self.source.get_at((x, y)) == (100,0,0):#Dark red pixels are breakable
                    self.breaks.append(BreakBlock(pygame.Rect(x*10, y*10, 10, 10), self.colorScheme))

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
        self.lvlSurf = pygame.Surface((self.source.get_width()*10, self.source.get_height()*10))


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
class InventoryItem:
    # The different items--like lightstones and koli balls--that get picked up by the player and put in the inventory
    def __init__(self, spriteName, name, screenName=None, maxcount=1):
        self.sprite = pygame.transform.scale(imgLoad(spriteName, 'i').convert(), (50, 50))
        self.sprite.set_colorkey(self.sprite.get_at((0,0)))
        self.name = name
        if screenName == None:
            self.screenName = name
        else:
            self.screenName = screenName
        self.maxcount = maxcount
        self.amt = 1

    def use(self, player, currentScene):
        pass

    def setAmt(self, number):
        self.amt = number
        return self

    def __str__(self):
        return self.name
                
            
class NPC:
    #Non-Player Character.  The other beings you can talk to in the game.
    def __init__(self, name, spriteName, fileName):
        self.name = name
        if spriteName != None:
            self.sprite = pygame.transform.scale(imgLoad(spriteName, 'n').convert(), (WX, WY))
        else:
            self.sprite = None
        self.words = []
        txtPath = txtLoad(fileName, 'n')
        for line in open(txtPath, 'r'):
            self.words.append(line.strip())
        
    def getLine(self, part):
        '''Takes the beginning part of a line in the words file (e.g "O") and returns the string that follows it.'''
        for line in self.words:
            if line.startswith(part):
                line = line.split(part + '~')
                line = ''.join(line)
                line = line.split('|')
                return line
        return False

    def editWords(self, newFile, player):
        self.words = []
        lineToWrite = "scenes."+self.name+".startEdits('"+newFile+"')\n"
        actuallyWrite = False
        for line in open(txtLoad(newFile, 'n'), 'r'):
            self.words.append(line.strip())
        #The following code documents the edit
        if player.name != 'admin':
            editFile = open(txtLoad(player.name+'edits.txt', 's'), 'r')
            lineList = [None]
            for line in editFile:
                lineList.append(line.strip())
            if str(lineList[-1]) + '\n' != lineToWrite:
                actuallyWrite = True
            if actuallyWrite:
                editFile = open(txtLoad(player.name+'edits.txt','s'),'a')
                editFile.write(lineToWrite)
            editFile.close()

    def startEdits(self, newFile):
        self.words = []
        for line in open(txtLoad(newFile, 'n'), 'r'):
            self.words.append(line.strip())
    
    def drawQCross(self):
        '''Draws black lines in a cross along the bottom of the screen.'''
        pygame.draw.line(window, (0,0,0), (0, WY), (WX, WY))
        pygame.draw.line(window, (0,0,0), (0, WY-25), (WX, WY-25))
        pygame.draw.line(window, (0,0,0), (0, WY-50), (WX, WY-50))
        pygame.draw.line(window, (0,0,0), (WX//2, WY-50), (WX//2, WY))
        
    def talk(self, player, junkCoord):
        self.state = 'o'
        self.part = 0
        blitArrow = False
        self.dispPack = False
        self.teleport = None
        sceneBkg = window.copy()
        while True:
            
            if self.teleport != None:
                return self.teleport
            
            clickedOnQ0 = False
            clickedOnQ1 = False
            clickedOnQ2 = False
            clickedOnQ3 = False
            
            Q0 = pygame.Rect(0, 375, 300, 25)
            Q1 = pygame.Rect(300, 375, 300, 25)
            Q2 = pygame.Rect(0, 350, 300, 25)
            Q3 = pygame.Rect(300, 350, 300, 25)
            
            blah = pygame.Surface((WX, 150))
            blah.set_alpha(200)
            blah.fill((100, 100, 100))
            #This is the equivalent of clearing the surface for blah.
            if self.sprite != None:
                window.blit(self.sprite, bkgRect)
            else:
                window.blit(sceneBkg, bkgRect)

            window.blit(inventoryIcon, (550, 0))
            window.blit(palIcon, (520, 0))
            
            clickedOnArrow = False
            for event in pygame.event.get():
                if event.type == QUIT:
                    DTquit(player)
                if event.type == MOUSEBUTTONUP:
                    if arrowRect.collidepoint(event.pos):
                        clickedOnArrow = True
                    elif Q0.collidepoint(event.pos):
                        clickedOnQ0 = True
                    elif Q1.collidepoint(event.pos):
                        clickedOnQ1 = True
                    elif Q2.collidepoint(event.pos):
                        clickedOnQ2 = True
                    elif Q3.collidepoint(event.pos):
                        clickedOnQ3 = True  
                    elif inventButton1.collidepoint(event.pos):
                        self.dispPack = True
                    elif inventButton2.collidepoint(event.pos):
                        self.dispPack = False
                        
                    
            if self.state == 'm':
                y = 0
                x = 0
                txtSurf = txt.render('', True, (0,0,0))
                blitArrow = False
                Q0 = pygame.Rect(0, 125, 300, 25)
                Q1 = pygame.Rect(300, 125, 300, 25)
                Q2 = pygame.Rect(0, 100, 300, 25)
                Q3 = pygame.Rect(300, 100, 300, 25)
                
                TxtToBlit = ''.join(self.getLine('m'))
                TxtToBlit = TxtToBlit.split(' ')
                for i in TxtToBlit:
                    if txt.size(i)[0] <= WX-x:
                        blah.blit(txt.render(i, True, (0,0,0)), (x, y))
                        x += txt.size(i + ' ')[0]
                    else:
                        y += 20
                        x = 0
                        blah.blit(txt.render(i, True, (0,0,0)), (x, y))
                        x += txt.size(i + ' ')[0]
                q0s = sTxt.render(''.join(self.getLine('q0')), True, (0,0,0))
                blah.blit(q0s, Q0)
                q1s = sTxt.render(''.join(self.getLine('q1')), True, (0,0,0))
                blah.blit(q1s, Q1)
                q2s = sTxt.render(''.join(self.getLine('q2')), True, (0,0,0))
                blah.blit(q2s, Q2)
                q3s = sTxt.render(''.join(self.getLine('q3')), True, (0,0,0))
                blah.blit(q3s, Q3)
                if clickedOnQ0 and self.getLine('r0') != False:
                    self.state = 'r0'
                if clickedOnQ1 and self.getLine('r1') != False:
                    self.state = 'r1'
                if clickedOnQ2 and self.getLine('r2') != False:
                    self.state = 'r2'
                if clickedOnQ3 and self.getLine('r3') != False:
                    self.state = 'r3'
                self.drawQCross()
                
            if self.state != 'm':
                y = 0
                x = 0
                txtSurf = txt.render('', True, (0,0,0))
                if self.state == ''.join(self.getLine('bye')) and self.part==1:
                    self.state = 'o'
                    self.part = 0
                    return
                if self.part<len(self.getLine(self.state)):
                    TxtToBlit = self.getLine(self.state)[self.part].split(' ')
                    for i in TxtToBlit:
                        if txt.size(i)[0] <= WX-x:
                            blah.blit(txt.render(i, True, (0,0,0)), (x, y))
                            x += txt.size(i + ' ')[0]
                        else:
                            y += 20
                            x = 0
                            blah.blit(txt.render(i, True, (0,0,0)), (x, y))
                            x += txt.size(i + ' ')[0]
                    blitArrow = True
                    if clickedOnArrow:
                        self.part+=1
                else:
                    self.state = 'm'
                    self.part = 0
            addCmds = self.getLine('addCmds')
            if addCmds != False:
                for i in range(len(addCmds)):
                    exec(addCmds[i])

            

            blah.blit(txtSurf, (0, 0))
            if blitArrow:
                window.blit(arrow, arrowRect)
            if self.dispPack:
                player.dispInventory(self.name)
            window.blit(blah, (0, 250))
            pygame.display.update()
              
    def giveStuff(self, inventory, whatToGive):
        '''Takes an Inventory and an InventoryItem, and adds the InventoryItem to the Inventory.
        Returns a bool indicating it was successful.'''
        self.dispPack = True
        return inventory.add(whatToGive)


class Scene: #Note:  Tap 'E' to see what scene you're in
    def __init__(self, imageName, name):
        self.bkg = imageName
        self.hotSpots = []
        self.talks = []
        self.items = []
        self.name = 'scenes.' + name
        
    def play(self, player, mousePos):
        '''Executes a while True: game loop that will display a background, pickup items, and NPC's.
        Will add the pickup to the inventory if it is clicked on, talk to the NPC if it is clicked on, and go to another scene if the hotspots are clicked on.''' 
        dispPack = False
        dispPals = False
        editMode = False
        mouseState = True
        bkg = pygame.transform.scale(imgLoad(self.bkg, 's').convert(), (WX, WY))
        while True:
            mouseState=True
            window.blit(bkg, (0,0))
            window.blit(inventoryIcon, (550, 0))
            window.blit(palIcon, (520, 0))
            events = pygame.event.get()
            mousePos = pygame.mouse.get_pos()
            for i in events:
                if i.type == QUIT:
                    DTquit(player)
                if i.type == MOUSEBUTTONUP:
                    if i.button == 1:
                        if inventButton1.collidepoint(i.pos):
                            dispPack=True
                        if inventButton2.collidepoint(i.pos):
                            dispPack=False
                        if palButton1.collidepoint(i.pos):
                            dispPals = True
                        if palButton2.collidepoint(i.pos):
                            dispPals = False
                if i.type == KEYUP:
                    if i.key == K_e:
                        editMode = not editMode
            for i in self.items:
                if player.contains(i[0]):
                    self.delItem(i[0])
                else:
                    window.blit(i[0].sprite, i[1])
            CHS = self.chkHotSpots(events)
            CI = self.chkItems(events)
            CNPC = self.chkNPC(events)
            if CI != False:
                player.add(CI)
                dispPack = True
                self.delItem(CI)
            elif CHS != False:
                return (CHS, player, mousePos)
            elif CNPC != False:
                pygame.mouse.set_visible(True)
                teleport = CNPC.talk(player, self.bkg)
                if teleport != None:
                    return (teleport, player, mousePos)
            if dispPack:
                player.dispInventory(self.name)
            if dispPals:
                player.dispCompanions(self.name)
            if editMode:
                window.blit(sTxt.render(scenes.currentScene, True, (255,51,0)), (0,WY-40))
                window.blit(sTxt.render(str(mousePos), True, (255,51,0)), (0,WY-50))
            for i in self.hotSpots:
                if i[1].collidepoint(mousePos):
                    mouseState = False
                    if i[1] != rightRect and i[1] != leftRect:
                        window.blit(sceneCursor, (mousePos[0]-12, mousePos[1]-12))
                    elif i[1] == rightRect or i[1] == leftRect:
                        window.blit(returnCursor, (mousePos[0]-12, mousePos[1]-12))
            for i in self.talks:
                if i[1].collidepoint(mousePos):
                    mouseState=False
                    window.blit(talkCursor, (mousePos[0]-12, mousePos[1]-12))
            for i in self.items:
                if i[1].collidepoint(mousePos):
                    mouseState=False
                    window.blit(pickupCursor, (mousePos[0]-12, mousePos[1]-12))
            pygame.mouse.set_visible(mouseState)
            pygame.display.update()
            
    def addHotSpot(self, scene, rect, start=True, player=None):
        '''Takes a scene and the rect to click on to go to that scene, and adds it to the hotspots.'''
        self.hotSpots.append((scene, rect))
        if not start:
            actuallyWrite = False
            lineToWrite = self.name+".startAdd("+scene.name+', '+'pygame.Rect('+str(rect.left)+','+str(rect.top)+','+str(rect.width)+','+str(rect.height)+'))\n'
            if player.name != 'admin':
                editFile = open(txtLoad(player.name+'edits.txt', 's'), 'r')
                lineList = [None]
                for line in editFile:
                    lineList.append(line.strip())
                if str(lineList[-1]) + '\n' != lineToWrite:
                    actuallyWrite = True
                if actuallyWrite:
                    editFile = open(txtLoad(player.name+'edits.txt','s'),'a')
                    editFile.write(lineToWrite)
                editFile.close()

    def startAdd(self, scene, rect):
        self.hotSpots.append((scene, rect))

    def returnSpot(self, scene):
        self.addHotSpot(scene, leftRect)
        self.addHotSpot(scene, rightRect)
        
    def chkHotSpots(self, events):
        '''If any of the hotspots were clicked on, returns that hotspot's scene.  Else, returns False.'''
        for i in self.hotSpots:
            for event in events:
                if event.type == MOUSEBUTTONUP and event.button == 1:#aka left-click
                    if i[1].collidepoint(event.pos):
                        return i[0]
        return False

    def delHotSpot(self, scene, player, start=False):
        for i in self.hotSpots:
            if i[0] == scene:
                self.hotSpots.remove(i)
                if not start:
                    actuallyWrite = False
                    lineToWrite = self.name+".delHotSpot("+scene.name+', player, True)\n'
                    if player.name != 'admin':
                        editFile = open(txtLoad(player.name+'edits.txt', 's'), 'r')
                        lineList = [None]
                        for line in editFile:
                            lineList.append(line.strip())        
                        if str(lineList[-1]) + '\n' != lineToWrite:
                            actuallyWrite = True
                        if actuallyWrite:
                            editFile = open(txtLoad(player.name+'edits.txt','s'),'a')
                            editFile.write(lineToWrite)
                        editFile.close()
        
    def addNPC(self, npc, rect):
        '''Takes an NPC and a corresponding rect, and adds it to the NPCs in the scene.'''
        self.talks.append((npc, rect))
        
    def chkNPC(self, events):
        '''If any of the NPCs were clicked on, it returns the NPC(object) that was clicked on.  Else, returns False.'''
        for i in self.talks:
            for event in events:
                if event.type == MOUSEBUTTONUP and event.button == 1:
                    if i[1].collidepoint(event.pos):
                        return i[0]
        return False
        
    def addItem(self, item, rect):
        '''Takes an InventoryItem and a corresponding Rect, and adds it to the items to pick up in the scene.'''
        self.items.append((item, rect))
        
    def chkItems(self, events):
        '''If any items in the scene were clicked on, returns the corresponding InventoryItem.  Else, returns False.'''
        for i in self.items:
            for event in events:
                if event.type == MOUSEBUTTONUP:
                    if event.button == 1:
                        if i[1].collidepoint(event.pos):
                            return i[0]
        return False

    def delItem(self, item):
        '''Deletes an item from a scene'''
        for i in self.items:
            if i[0] == item:
                self.items.remove(i)
                return True
        return False




def DTquit(player):
    saveGame(player)
    #Long live the evil geniuses.
    if player.name == 'admin':
        pygame.quit()
        sys.exit()
    else:
        pygame.quit()
        sys.exit()


def saveGame(player):
    #Writes a Player() object and the name of the current scene to a text file
    if player.name != 'admin':
        stuffInPack = '['
        fileToWrite = open(txtLoad(player.name+'.txt','s'),'w')
        fileToWrite.write(scenes.currentScene + '\n')
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


