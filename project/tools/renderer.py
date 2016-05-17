import pygame
import tools.onRenderListener

class BasicRenderer(tools.onRenderListener.OnRenderListener):
    __circ = pygame.Surface((0, 0), 0, 32) # a dummy surface to not have 'None'
    __xPosition = 0

    def __init__(self):
        self.__circ = pygame.Surface((30, 30), 0, 32)
        pygame.draw.circle(self.__circ, (0, 255, 0), (15, 15), 15)
        self.__circ.set_colorkey((0,0,0))
        self.__xPosition = 100.0

    def onRender(self, screen):
        #TODO create UI class for this
        for i in range(0, 1):
            screen.blit(self.__circ, (int(self.__xPosition), 100))

    def onUpdate(self, delta):
        #TODO implement with useful animation/update stuff
        self.__xPosition += delta / 10
        #log.info("callbacks.renderer.onUPdate delta-time", str(delta))
