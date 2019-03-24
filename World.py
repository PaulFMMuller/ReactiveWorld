import numpy as np

class World:
    def __init__(self, worldSize=(100,100), initMethod=0):
        self.worldSize = worldSize
        self.genWorld(initMethod)
        self.actionBuffer = []
        self.worldLimits = (self.worldSize[0] * 50, self.worldSize[1] * 50)
        self.initializeCollisions()


    def genWorld(self, initMethod):
        # generate new world. Method to be improved
        self.worldState = [['Grass']*self.worldSize[1]]*self.worldSize[0]

        # Add life
        self.characters = []


    def initializeCollisions(self):
        self.collisions = np.zeros((self.worldLimits[0],self.worldLimits[1]))


    def startUpdate(self):
        self.initializeCollisions()
        for character in self.characters:
            # Future : Add decision-taking moment (Every 10 minutes ?)
            if character.sex == 'Ball':
                character.setAction(('Move_Down', None))
            else:
                character.setAction(('', None))
            newPosition = character.getFuturePosition(self.worldLimits)
            self.collisions[newPosition[0]][newPosition[1]] += 1
        self.forbidActions()


    def forbidActions(self):
        for character in self.characters:
            newPosition = character.getFuturePosition(self.worldLimits)
            oldPosition = character.getPosition()
            #if np.sum(self.collisions[newPosition[0]-12:newPosition[0]+12][newPosition[1]-10:newPosition[1]+10]) > 1.5:
            if np.sum(self.collisions[newPosition[0]][newPosition[1]]) > 1.5:
                if not (newPosition == oldPosition):
                    character.forbidAction()


    def determineIfBlock(self, collisions, newPosition, oldPosition):
        if np.sum(collisions[newPosition[0]-12:newPosition[0]+12, newPosition[1]-10:newPosition[1]+10]) < 0.5:
            return False
        else:
            if newPosition == oldPosition:
                return False
            else:
                return True
        return True


    def endUpdate(self):
        for character in self.characters:
            # Future : Add decision-taking moment (Every 10 minutes ?)
            character.executeAction(self.worldLimits)
        self.sortCharacters()

    def addCharacter(self,character):
        self.characters.append(character)


    def sortCharacters(self):
        self.characters = sorted(self.characters, key=(lambda x: x.position[1]))