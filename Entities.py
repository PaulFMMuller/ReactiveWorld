import pygame
from pygame.locals import *


STEP_SIZE = 10
move_dictionary = {'Move_Left' : (-STEP_SIZE, 0),\
                   'Move_Right': (STEP_SIZE,  0),\
                   'Move_Up'   : (0, -STEP_SIZE),\
                   'Move_Down' : (0,  STEP_SIZE)}

class Object:
    def __init__(self, passable=False, level=1):
        self.passable = passable
        self.level = 1


class Entity:
    def __init__(self, position, name):
        self.position = position
        self.name = name

        self.currentTask = None
        self.taskList = []


class Character(Entity,Object):
    def __init__(self, position, name, sex, family=None, portraitPath=None):
        super().__init__(False, 4)
        super().__init__(position, name)
        self.sex = sex
        self.family = family
        self.currentAction = ('',)

        self.graphics = CharacterGraphics(self, portraitPath)
        self.forbidden = False

    def setAction(self, action):
        self.currentAction = action
        self.graphics.loadAnimation(action)


    # World will have to deal with collision.
    def executeAction(self, worldLimits):
        if 'Move' in self.currentAction[0]:
            alpha = (self.forbidden == False)
            addedPosition = move_dictionary[self.currentAction[0]]
            self.position = (self.position[0]+alpha*addedPosition[0] % worldLimits[0], self.position[1]+alpha*addedPosition[1] % worldLimits[1])
            self.forbidden = False


    def animateImage(self, count):
        self.graphics.update(count)
        return self.getImage()


    def getImage(self):
        return self.graphics.image


    def getCurrentPosition(self, count, maxCount, worldLimits):
        if 'Move' in self.currentAction[0]:
            alpha = (self.forbidden == False)
            staticPos  = self.position
            addedPosition = move_dictionary[self.currentAction[0]]
            currentPos = (alpha * (addedPosition[0]) * (count+1) / (maxCount+1) + staticPos[0] % worldLimits[0], (alpha * (addedPosition[1]) * (count+1) / (maxCount+1) + staticPos[1] + 32) % (worldLimits[1]+32) - 32)
        else:
            currentPos = self.position
        return currentPos


    def getCurrentImage(self):
        return self.graphics.getCurrentImage()


    def animateImage(self, t):
        return self.graphics.animateImage(t)


    def getFuturePosition(self,worldLimits):
        pos = self.getCurrentPosition(0, 0, worldLimits)
        pos = (int(pos[0]), int(pos[1]))
        return pos


    def getCollisionBoxCoordinates(self):
        return (self.position[0], self.position[1],24,16)


    def forbidAction(self):
        self.forbidden = True


class CharacterGraphics:
    def __init__(self, character, portraitPath=None):
        self.portraitPath = portraitPath
        self.character = character
        self.imageBank = None
        self.animationBank = None
        self.animationLoop = None
        if portraitPath is None:
            self.image = pygame.Surface((50, 50))
            self.image.set_colorkey((0,0,0))
            pygame.draw.circle(self.image, pygame.Color('Blue'), (int(50/2),int(50/2)), int(50 / 2)-1)
            self.animationLoop = [self.image]
        else:
            self.extractImagesFromCharset()
            self.extractAnimationsFromImages()
            self.initiateImage()


    def extractImagesFromCharset(self):
        size=(288//4, 256//2)
        i = self.portraitPath[1] % 4
        j = self.portraitPath[1] // 4
        try:
            image = pygame.image.load(self.portraitPath[0]).convert()
        except:
            image = pygame.image.load(self.portraitPath[0])
        image.set_colorkey(image.get_at((0, 0)))
        self.imageBank = image.subsurface((i*size[0], j*size[1], size[0], size[1]))


    def extractAnimationsFromImages(self):
        size = (24, 32)
        positions = ['Move_Up', 'Move_Right', 'Move_Down', 'Move_Left']   # Hardcoded since using templates
        self.animationBank = {}
        for i in range(4):   # Hardcoded 4.
            self.animationBank[positions[i]] = []
            for j in range(3):
                self.animationBank[positions[i]].append(self.imageBank.subsurface((j * size[0], i * size[1], size[0], size[1])))


    def initiateImage(self):
        self.image = self.animationBank['Move_Down'][0]   # Initiate with down-looking characters.


    def getCurrentImage(self):
        return self.image


    def animateImage(self, t):
        self.image = self.animationLoop[t % len(self.animationLoop)]
        return self.getCurrentImage()


    def loadAnimation(self, action):
        try:
            self.animationLoop = self.animationBank[action[0]]
        except:
            self.animationLoop = [self.image]


    def getStringDirection(self,targetPosition):
        currentPosition = self.character.position
        if currentPosition[1] > targetPosition[1]:
            return 'Up'
        elif currentPosition[1] < targetPosition[1]:
            return 'Down'
        elif currentPosition[0] > targetPosition[0]:
            return 'Left'
        elif currentPosition[0] < targetPosition[0]:
            return 'Right'
        else:
            return 'Up'


class Company(Entity):
    def __init__(self, position, name, siteSize, wealth, head, subEntities, companyType, subType):
        Entity.__init__(position, name)

        self.siteSize = siteSize
        self.wealth = wealth

        self.subEntities = subEntities
        self.head = head

        self.companyType = companyType
        self.subType = subType

