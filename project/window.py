import pygame

WINDOW_SIZE = (200,100)

def init(size):
    WINDOW_SIZE = size
    pygame.init()

def getWindow():
    screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
    screen.set_caption("PyBalone - v.0.0.1_prealpha.infdev")

    return screen

def getBackground():
    background = pygame.Surface(WINDOW_SIZE)
    background.fill((255,0,0,0))
    return backgrund
