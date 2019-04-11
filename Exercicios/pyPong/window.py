import pygame

class Window:

    def __init__(self, width, height):
        self.__width, self.__height = size = (width, height)
        self.__screen = pygame.display.set_mode(size)

    def set_title(self, title):
        pygame.display.set_caption(title)

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def size(self):
        return (self.__width, self.__height)

    def draw(self, object):
        object.draw(self.__screen)

    def clear(self, color=(0, 0, 0)):
        self.__screen.fill(color)

    def update(self):
        pygame.display.update()
