import playingField
import window

window.init((800,600))
window = window.getWindow()
back = window.getBackground()
window.blit(back,(0,0))

node = playingField.Node(2, 3)
print(str(node.x) +" - " + str(node.y))

while True:
    pygame.display.update()
