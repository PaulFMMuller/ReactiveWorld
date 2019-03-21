class World:
    def __init__(self, worldSize=(100,100), initMethod=0):
        self.worldSize = worldSize
        self.genWorld(initMethod)
        self.actionBuffer = []
        self.worldLimits = (self.worldSize[0] * 50, self.worldSize[1] * 50)
        self.collisions = [[[]]*(self.worldLimits[0]//10)]*(self.worldLimits[1]//10)


    def genWorld(self, initMethod):
        # generate new world. Method to be improved
        self.worldState = [['Grass']*self.worldSize[1]]*self.worldSize[0]

        # Add life
        self.characters = []


    def startUpdate(self):
        self.collisions = [[[]]*(self.worldLimits[0])]*(self.worldLimits[1])
        for character in self.characters:
            # Future : Add decision-taking moment (Every 10 minutes ?)
            #if character.sex == 'Ball':
            character.setAction(('Move_Down', None))
            #else:
            #    character.setAction(('',None))
            newPosition = character.getFuturePosition(self.worldLimits)
            if len(self.collisions[newPosition[0]][newPosition[1]]) == 0:
                self.collisions[newPosition[0]][newPosition[1]] = character
            else:
                character.forbidAction()


    def endUpdate(self):
        for character in self.characters:
            # Future : Add decision-taking moment (Every 10 minutes ?)
            character.executeAction(self.worldLimits)


    def addCharacter(self,character):
        self.characters.append(character)

