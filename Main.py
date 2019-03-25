import glob
from Engine import Engine
from Entities import *
from World import World
import time


pygame.display.init()

world = World((20,10))
engine = Engine(world)

for i in range(0,490,20):
    for j in range(0,490,20):
        world.addCharacter(Character((i,j), 'Character {},{}'.format(i,j),'None', portraitPath=('Data/Charset/ff6-18.png', i%4)))
#testCharacter = Character((200,200), "Joe Ballo", 'Ball', portraitPath=('Data/Charset/ff6-18.png', 0))
#testCharacter2 = Character((200,300), "Joe Ballobstacle", 'Ballobstacle', portraitPath=('Data/Charset/ff6-18.png', 1))

#world.addCharacter(testCharacter)
#world.addCharacter(testCharacter2)

engine.run(175)

time.sleep(1)
pygame.quit()