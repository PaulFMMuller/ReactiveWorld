import glob
from Engine import Engine
from Entities import *
from World import World
import time


pygame.display.init()

world = World((20,10))
engine = Engine(world)

testCharacter = Character((10,100), "Joe Ballo", 'Ball', portraitPath=('Data/Charset/ff6-18.png', 0))
testCharacter2 = Character((10,200), "Joe Ballobstacle", 'Ballobstacle', portraitPath=('Data/Charset/ff6-18.png', 1))

world.addCharacter(testCharacter)
world.addCharacter(testCharacter2)

engine.run(175)

time.sleep(1)
pygame.quit()