import pygame
import ui.window as window
import game.playingField as playingField
import game.gameLoop as gameLoop
import game.log as log
import callbacks.input
import callbacks.renderer
import sys

print(sys.path)

window = window.window((800,600))
window.setBackgroundColor((255,0,0,0)) # We can set the color afterwards

# Dummy test for node stuff
node = playingField.Node(2, 3)
log.info("__init__-nodeTest", str(node.x) + " - " + str(node.y))

loop = gameLoop.gameLoop(window.getSurface())
loop.setBackgroundImage(window.newBackgroundSurface())
loop.addKeyInputListener(lambda key : callbacks.input.onInput(key))
loop.addRenderCallback(lambda screen : callbacks.renderer.onRender(screen))
loop.addUpdateCallback(lambda delta : callbacks.renderer.onUpdate(delta))
loop.run()
