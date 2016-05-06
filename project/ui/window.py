import game.log as log
import pygame

class window:

    __windowSize = (200,100)
    __backgroundColor = (0,0,0,0)
    __surface = None

    def __init__(self, size):
        """
        Initializes all variables and calls all init function needed to start the game.

        Arguments:
        size -- The size of the window.
        """
        self.__windowSize = size

        if self.__surface == None:
            self.__surface = pygame.display.set_mode(self.__windowSize, 0, 32)
            pygame.display.set_caption("PyBalone - v.0.0.1_prealpha.infdev")
        else:
            self.__surface.size = self.__windowSize

    def getSurface(self):
        return self.__surface

    def newBackgroundSurface(self):
        """
        Creates a new surface filled with the current background color and as big as the current window size is.
        """
        background = pygame.Surface(self.__windowSize)
        background.fill(self.__backgroundColor)
        return background

    def setBackgroundColor(self, color):
        """
        Sets the new background color and directly applies it to the surface.

        Arguments:
        color -- The new color of the window.
        """
        self.__backgroundColor = color
        if self.__surface == None:
            self.__surface.blit(getBackgroundSurface(),(0,0))
        else:
            log.error("window-SetBackgroundColor", "The surface is of type None, so some init methods were not called.")
