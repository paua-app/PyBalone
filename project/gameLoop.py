import pygame
import sys

class gameLoop:

    keyInputFunction = lambda x : None
    renderFunction = lambda x : None

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self.keyInputFunction()
            self.renderFunction()
            pygame.display.update()
