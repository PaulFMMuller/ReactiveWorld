import numpy as np

class World:
    def __init__(self, worldSize=(100,100), initMethod=0):
        self.worldSize = worldSize
        self.genWorld(initMethod)
        self.actionBuffer = []
        self.worldLimits = (self.worldSize[0] * 50, self.worldSize[1] * 50)
        self.formerCollisions = np.zeros((self.worldLimits[0], self.worldLimits[1]))

    def genWorld(self, initMethod):
        # generate new world. Method to be improved
        self.worldState = [['Grass']*self.worldSize[1]]*self.worldSize[0]

        # Add life
        self.characters = []

    def startUpdate(self):
        collisions = np.zeros((self.worldLimits[0], self.worldLimits[1]))
        for character in self.characters:
            # Future : Add decision-taking moment (Every 10 minutes ?)
            if character.sex == 'Ball':
                character.setAction(('Move_Down', None))
            else:
                character.setAction(('', None))
            newPosition = character.getFuturePosition(self.worldLimits)
            oldPosition = character.getPosition()
            if not self.determineIfBlock(collisions, newPosition, oldPosition):
                collisions[newPosition[0], newPosition[1]] = 1
            else:
                character.forbidAction()
                print('Forbidden !')
        self.formerCollisions = collisions


    def determineIfBlock(self, collisions, newPosition, oldPosition):
        if np.sum(collisions[newPosition[0]-12:newPosition[0]+12, newPosition[1]-16:newPosition[1]+16]) < 0.5:
            if np.sum(self.formerCollisions[newPosition[0]-12:newPosition[0]+12, newPosition[1]-16:newPosition[1]+16]) < 0.5:
                return False
            else:
                if newPosition == oldPosition:
                    return False
                else:
                    return True
        else:
            if newPosition == oldPosition:
                return False
        return True


    def endUpdate(self):
        for character in self.characters:
            # Future : Add decision-taking moment (Every 10 minutes ?)
            character.executeAction(self.worldLimits)


    def addCharacter(self,character):
        self.characters.append(character)

