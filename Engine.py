import pygame
from pygame.locals import *
import time
import glob
import re


class Engine:
    def __init__(self, world, animationTime=0.03, maxAnimationLength=3):
        self.world = world
        self.screen = None
        self.animationTime = animationTime
        self.maxAnimationLength = maxAnimationLength

        self.loadTerrain()


    def loadTerrain(self):
        self.terrains = {}
        terrainPaths = glob.glob('Data/Terrain/*.png')
        for terrainPath in terrainPaths:
            try:
                terrain = pygame.image.load(terrainPath).convert()
            except:
                terrain = pygame.image.load(terrainPath)
            imageName = re.findall('[a-zA-Z0-9_-]+', terrainPath)[-2]
            self.terrains[imageName] = terrain


    def run(self, maxSteps=None):
        if self.screen is None:
            self.screen = pygame.display.set_mode((self.world.worldSize[0]*50,self.world.worldSize[1]*50))

        if maxSteps is None:
            maxSteps = -1
        steps = 0
        while steps < maxSteps:
            steps += 1
            self.showEnvironment()
            self.showCharacters()
            pygame.display.flip()
            self.world.startUpdate()
            self.animateCharacters()
            self.world.endUpdate()


    def showEnvironment(self):
        for i in range(self.world.worldSize[0]):
            for j in range(self.world.worldSize[1]):
                self.screen.blit(self.terrains[self.world.worldState[i][j]], (50*i, 50*j))


    def showCharacters(self):
        for character in self.world.characters:
            self.screen.blit(character.getCurrentImage(), character.getCurrentPosition(0, self.maxAnimationLength))


    def animateCharacters(self):
        timePerAnimation = self.animationTime / self.maxAnimationLength
        for t in range(self.maxAnimationLength):
            startTime = time.time()

            self.showEnvironment()
            for character in self.world.characters:
                self.screen.blit(character.animateImage(t), character.getCurrentPosition(t, self.maxAnimationLength))

            # Stabilizing FPS
            pygame.display.flip()
            duration = time.time() - startTime
            if duration < timePerAnimation:
                time.sleep(timePerAnimation-duration)

