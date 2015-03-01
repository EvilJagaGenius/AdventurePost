#Items, special and generic

import APtalk
from APtalk import *

print('Loading items')

#Special items

class HammerHatchet:
    def __init__(self):
        self.sprite = pygame.transform.scale(imgLoad('HammerHatchet.png', 'i'), (50,50)).convert()
        self.sprite.set_colorkey((0,255,0))
        self.name = "HammerHatchet"
        self.screenName = "Hammer-Hatchet"
        self.amt = 1
        self.maxcount = 1

    def use(self, player, currentScene):
        if currentScene == 'FortressDamek' and player.contains(APtalk.Disk):
            APtalk.FortressDamek.state = 'o'
            APtalk.FortressDamek.part = 0
            APtalk.FortressDamek.editWords('damek4.txt', player)

    def setAmt(self, junk):
        return self

class Disk:
    def __init__(self):
        self.sprite = pygame.transform.scale(imgLoad('Disk.png', 'i'), (50,50)).convert()
        self.sprite.set_colorkey((0,255,0))
        self.name = "Disk"
        self.screenName = "Disk"
        self.amt = 1
        self.maxcount = 1

    def use(self, player, currentScene):
        if currentScene == 'FortressDamek' and player.contains(APtalk.HammerHatchet):
            APtalk.FortressDamek.state = 'o'
            APtalk.FortressDamek.part = 0
            APtalk.FortressDamek.editWords('damek4.txt', player)

    def setAmt(self, junk):
        return self


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
            APtalk.Onepu.state = 'o'
            APtalk.Onepu.part = 0
            APtalk.Onepu.editWords('onepu2.txt', player)
        elif currentScene == 'Jala':
            APtalk.Jala.state = 'o'
            APtalk.Jala.part = 0
            APtalk.Jala.editWords('jala2.txt', player)
            APtalk.Onepu.editWords('onepu3.txt', player)

    def setAmt(self, junk):
        return self

class Plate:
    def __init__(self):
        self.sprite = pygame.transform.scale(imgLoad('Plate.png', 'i'), (50,50))
        self.sprite.set_colorkey((0,255,0))
        self.name = "Plate"
        self.screenName = "Plate of... something"
        self.amt = 1
        self.maxcount = 1

    def use(self, player, currentScene):
        if currentScene == 'Nuhrii':
            APtalk.Nuhrii.state = 'o'
            APtalk.Nuhrii.part = 0
            APtalk.Nuhrii.editWords('nuhrii3.txt', player)
            player.remove(self)

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
        if (currentScene == 'APtalk.onuKoro4') or(currentScene == 'APtalk.onuKoro5') or (currentScene == 'APtalk.onuKoro6'):
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
        if (currentScene == 'APtalk.lightMine7') or (currentScene == 'Kaj'):
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
            APtalk.Dashka.editWords('dashka3.txt', player)
            APtalk.Dashka.state='o'
            APtalk.Dashka.part = 0
            player.remove(self)

    def setAmt(self, junk):
        return self

#End special items

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


print('Done loading items')
