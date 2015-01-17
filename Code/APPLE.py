finished = False
print('Loading APPLE')




import APtalk
from APtalk import *

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
        
class ExitBlock:
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
                    self.exitBlock = ExitBlock(pygame.Rect(x*10, y*10, 20, 20))
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
                    DTquit(player, self.name)
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


finished = True
print('Done loading APPLE')
