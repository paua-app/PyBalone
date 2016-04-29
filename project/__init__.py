import playingField
import window
import pygame
import gameLoop

window.init((800,600))
windowScreen = window.getWindow()
back = window.getBackground()
windowScreen.blit(back,(0,0))

# Dummy test for node stuff
node = playingField.Node(2, 3)
print(str(node.x) + " - " + str(node.y))

# Some listeners and callback functions:
# TODO: extract into own file/class
def onInput(key):
    #TODO implement with useful input
    print(str(key))

circ = pygame.Surface((30, 30), 0, 32)
pygame.draw.circle(circ, (0, 255, 0), (15, 15), 15)
circ.set_colorkey((0,0,0))
x = 100
def onRender(screen):
    #TODO implement with useful renderings
    screen.blit(circ, (x, 100))

def onUpdate(delta):
    #TODO implement with useful animation/update stuff
    global x
    x += 10

loop = gameLoop.gameLoop(windowScreen)
loop.setBackgroundImage(back)
loop.addKeyInputListener(lambda key : onInput(key))
loop.addRenderCallback(lambda screen : onRender(screen))
loop.addUpdateCallback(lambda delta : onUpdate(delta), 250)
loop.run()
