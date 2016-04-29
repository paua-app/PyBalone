import pygame
import sys
import datetime

class gameLoop:

    keyInputFunction = lambda x : None
    renderFunction = lambda x : None
    updateFunction = lambda x : None
    lastUpdate = datetime.datetime.now()
    screen = None
    background = pygame.Surface((0,0),0,32)

    def __init__(self, screen):
        self.screen = screen

    def addKeyInputListener(self, listener):
        self.keyInputFunction = listener

    def addRenderCallback(self, callbackFunction):
        self.renderFunction = callbackFunction

    def addUpdateCallback(self, updateFunction):
        self.updateFunction = updateFunction

    def setBackgroundImage(self, background):
        self.background = background

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self.keyInputFunction(event.key)

            self.screen.blit(self.background, (0,0))
            self.renderFunction(self.screen)

            currentTime = datetime.datetime.now()
            deltaTime = datetime.datetime.now() - self.lastUpdate
            self.updateFunction(deltaTime.total_seconds() * 1000)
            self.lastUpdate = currentTime

            pygame.display.update()
