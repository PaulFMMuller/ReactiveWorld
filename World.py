class World:
    def __init__(self, worldSize=(100,100), initMethod=0):
        self.worldSize = worldSize
        self.genWorld(initMethod)
        self.actionBuffer = []


    def genWorld(self, initMethod):
        # generate new world. Method to be improved
        self.worldState = [['Grass']*self.worldSize[1]]*self.worldSize[0]

        # Add life
        self.characters = []


    def startUpdate(self):
        for character in self.characters:
            # Future : Add decision-taking moment (Every 10 minutes ?)
            character.setAction(('Move',((character.position[0]+10) % (self.worldSize[0]*50),(character.position[1]+10) % (self.worldSize[1]*50))))

    def endUpdate(self):
        for character in self.characters:
            # Future : Add decision-taking moment (Every 10 minutes ?)
            character.executeAction()


    def addCharacter(self,character):
        self.characters.append(character)

