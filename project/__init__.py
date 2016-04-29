import playingField
import window
import pygame
import gameLoop

window.init((800,600))
win = window.getWindow()
back = window.getBackground()
win.blit(back,(0,0))

node = playingField.Node(2, 3)
print(str(node.x) +" - " + str(node.y))

loop = gameLoop.gameLoop()
loop.run()
