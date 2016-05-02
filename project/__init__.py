import playingField
import window
import pygame
import gameLoop
import log

window = window.window((800,600))
window.setBackgroundColor((255,0,0,0)) # We can set the color afterwards

# Dummy test for node stuff
node = playingField.Node(2, 3)
log.info("__init__-nodeTest", str(node.x) + " - " + str(node.y))

# Some listeners and callback functions:
# TODO: extract into own file/class
def onInput(key):
    #TODO implement with useful input
    print(str(key))

circ = pygame.Surface((30, 30), 0, 32)
pygame.draw.circle(circ, (0, 255, 0), (15, 15), 15)
circ.set_colorkey((0,0,0))
x = 100.0
def onRender(screen):
    #TODO implement with useful renderings
    screen.blit(circ, (int(x), 100))

def onUpdate(delta):
    #TODO implement with useful animation/update stuff
    global x
    x += delta/10

loop = gameLoop.gameLoop(window.getSurface())
loop.setBackgroundImage(window.newBackgroundSurface())
loop.addKeyInputListener(lambda key : onInput(key))
loop.addRenderCallback(lambda screen : onRender(screen))
loop.addUpdateCallback(lambda delta : onUpdate(delta))
loop.run()
