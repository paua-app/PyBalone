import materials.playingField as playingField
import services.log as log
import tools.gameLoop as gameLoop
import tools.input as input
import tools.renderer as renderer
import tools.window as window

window = window.window((800,600))
window.setBackgroundColor((255,0,0,0)) # We can set the color afterwards

# Dummy test for node stuff
node = playingField.Node(2, 3)
log.info("__init__-nodeTest", str(node.x) + " - " + str(node.y))

loop = gameLoop.gameLoop(window.getSurface())
loop.setBackgroundImage(window.newBackgroundSurface())

loop.addRenderListener(renderer.BasicRenderer())
loop.addKeyInputListener(input.BasicInput())

loop.run()
