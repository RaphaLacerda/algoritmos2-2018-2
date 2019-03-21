"""Classe Window"""

import pygame

class Window:
    # Implementa objetos de janela usando PyGame
    def __init__(self, titulo):
        self.titulo = titulo
        self._width, self._height = self.size = (800, 600)
        # Inicializa objeto Window.

    def run(self):
        pygame.init()
        screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption(self.titulo)
        done = False
        is_blue = True
        x = 30
        y = 30
        clock = pygame.time.Clock()

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done == True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    is_blue = not is_blue               
            clock.tick(60)

            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_UP]: y -= 3
            if pressed[pygame.K_DOWN]: y += 3
            if pressed[pygame.K_LEFT]: x -= 3
            if pressed[pygame.K_RIGHT]: x += 3
            if pressed[pygame.K_ESCAPE]: pygame.QUIT
            if is_blue : color = (0, 128, 255)
            else: color = (255, 100, 0)
            screen.fill((0, 0, 0))
            pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))
            pygame.display.flip()

newWindow = Window("Oi, sou o PyGame")
newWindow.run()