import glob
from Engine import Engine
from Entities import *
from World import World
import time

world = World((20,10))
engine = Engine(world)

engine.run(5)

time.sleep(5)
pygame.quit()