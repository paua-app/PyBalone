import pygame
import game.log as log

circ = pygame.Surface((30, 30), 0, 32)
pygame.draw.circle(circ, (0, 255, 0), (15, 15), 15)
circ.set_colorkey((0,0,0))
x = 100.0

def onRender(screen):
    #TODO implement with useful renderings
    for i in range(0, 10000):
        screen.blit(circ, (int(x), 100))

def onUpdate(delta):
    #TODO implement with useful animation/update stuff
    global x
    x += delta/10
    log.info("delta-time", str(delta))
