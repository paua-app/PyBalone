import pygame
import sys
import datetime

class gameLoop:

    __keyListener = []
    __renderListener = []
    __lastUpdate = datetime.datetime.now()
    __screen = None
    __background = pygame.Surface((0,0),0,32)

    def __init__(self, __screen):
        self.__screen = __screen

    def addKeyInputListener(self, listener):
        self.__keyListener.append(listener)

    def addRenderListener(self, listener):
        self.__renderListener.append(listener)

    def setBackgroundImage(self, __background):
        self.__background = __background

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    # notify all listeners:
                    for listener in self.__keyListener:
                        listener.onInput(event.key)

            currentTime = datetime.datetime.now()
            deltaTime = datetime.datetime.now() - self.__lastUpdate
            self.__lastUpdate = currentTime

            # notify all listeners for updates
            for listener in self.__renderListener:
                listener.onUpdate(deltaTime.total_seconds() * 1000)

            # notify all listeners for render
            self.__screen.blit(self.__background, (0,0))
            for listener in self.__renderListener:
                listener.onRender(self.__screen)

            pygame.display.update()
