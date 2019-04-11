from game import Game
from window import Window

import pygame
pygame.init()

class PongGame(Game):

    def __init__(self):
        Game.__init__(self)
        self.window = Window(800, 600)
        self.window.set_title("Pong")
        self.clock = pygame.time.Clock()
        self.run()

if __name__ == "__main__":
    PongGame().run()
