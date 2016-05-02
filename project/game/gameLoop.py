import pygame
import sys
import datetime

class gameLoop:

    __keyInputFunction = lambda x : None
    __renderFunction = lambda x : None
    __updateFunction = lambda x : None
    __lastUpdate = datetime.datetime.now()
    __screen = None
    __background = pygame.Surface((0,0),0,32)

    def __init__(self, __screen):
        self.__screen = __screen

    def addKeyInputListener(self, listener):
        self.__keyInputFunction = listener

    def addRenderCallback(self, callbackFunction):
        self.__renderFunction = callbackFunction

    def addUpdateCallback(self, __updateFunction):
        self.__updateFunction = __updateFunction

    def setBackgroundImage(self, __background):
        self.__background = __background

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self.__keyInputFunction(event.key)

            self.__screen.blit(self.__background, (0,0))
            self.__renderFunction(self.__screen)

            currentTime = datetime.datetime.now()
            deltaTime = datetime.datetime.now() - self.__lastUpdate
            self.__updateFunction(deltaTime.total_seconds() * 1000)
            self.__lastUpdate = currentTime

            pygame.display.update()
