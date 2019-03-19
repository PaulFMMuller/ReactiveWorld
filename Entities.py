import pygame
from pygame.locals import *


class Entity:
    def __init__(self, position, name):
        self.position = position
        self.name = name

        self.currentTask = None
        self.taskList = []


class Character(Entity):
    def __init__(self, position, name, sex, family, portraitName):
        Entity.__init__(position, name)
        self.sex = sex
        self.family = family
        self.currentAction = None

        self.graphics = CharacterGraphics(portraitName)


    def setAction(self, action):
        self.currentAction = action
        self.graphics.loadAnimation(action, self.position)


    # World will have to deal with collision.
    def executeAction(self):
        if self.action[0] == 'Move':
            self.position = self.action[1]


    def animateImage(self, count):
        self.graphics.update(count)
        return self.getImage()


    def getImage(self):
        return self.graphics.image


    def getCurrentPosition(self, count, maxCount):
        if self.currentAction[0] == 'Move':
            staticPos  = self.position
            targetPos  = self.currentAction[1]
            currentPos = (targetPos-staticPos) * (count+1) / (maxCount+1) + staticPos
        else:
            currentPos = self.position
        return currentPos


class CharacterGraphics:
    def __init__(self, portraitName):
        self.portraitName = portraitName
        self.image = pygame.Surface((50, 50))

        # Character representation
        pygame.draw.circle(self.image, pygame.Color('Blue'), 50 / 2)
        self.animationLoop = [self.image]




class Company(Entity):
    def __init__(self, position, name, siteSize, wealth, head, subEntities, companyType, subType):
        Entity.__init__(position, name)

        self.siteSize = siteSize
        self.wealth = wealth

        self.subEntities = subEntities
        self.head = head

        self.companyType = companyType
        self.subType = subType

