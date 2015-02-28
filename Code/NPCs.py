#NPCs and companions

print('Loading NPCs')

import APtalk
from APtalk import *


class NPC:
    #Non-Player Character.  The other beings you can talk to in the game.
    def __init__(self, name, imgName, fileName, spriteName=None):
        self.name = name
        if spriteName != None:
            self.sprite = imgLoad(spriteName, 'n').convert()
            self.sprite.set_colorkey(self.sprite.get_at((0,0)))
        else:
            self.sprite = None
        if imgName != None:
            self.image = pygame.transform.scale(imgLoad(imgName, 'n').convert(), (WX, WY))
        else:
            self.image = None
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
        
    def talk(self, player, junkCoord, currentScene):
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
            if self.image != None:
                window.blit(self.image, bkgRect)
            else:
                window.blit(sceneBkg, bkgRect)

            window.blit(inventoryIcon, (550, 0))
            window.blit(palIcon, (520, 0))
            
            clickedOnArrow = False
            for event in pygame.event.get():
                if event.type == QUIT:
                    DTquit(player, currentScene)
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

print('Done with NPCs')
