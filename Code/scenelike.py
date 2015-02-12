#Scenes and scene-like classes

import APtalk
from APtalk import *
print('Loading scenelikes')

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
                    DTquit(player, self.name)
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
                teleport = CNPC.talk(player, self.bkg, self.name)
                if teleport != None:
                    return (teleport, player, mousePos)
            if dispPack:
                player.dispInventory(self.name)
            if dispPals:
                player.dispCompanions(self.name)
            if editMode:
                window.blit(sTxt.render(self.name, True, (255,51,0)), (0,WY-40))
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
        self.endScene = None
                            
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
        self.storySurf = pygame.Surface((600, 400))
        self.storySurf.fill((0,0,0))
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

        viewPoint = 0
        viewRect = pygame.Rect(0,0,600,400)
        viewSurf = pygame.Surface((0,0))
        while True:
            moveUp = False
            moveDown = False
            for event in pygame.event.get():
                if event.type == QUIT:
                    DTquit(player, self.name)
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
                    DTquit(player, self.name)
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

print('Done loading scenelikes')
