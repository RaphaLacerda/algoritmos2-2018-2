import pygame

class Game:

    def __init__(self):
        self.__running: False
        self.__window: None
        self.__game_objects = []

    def _draw(self):
        self.window.clear()
        for obj in self.__game_objects :
            self.window.draw(obj)
        self.window.update()
    
    def _update(self):
        for obj in self.__game_objects:
            obj.update(self)

    def run(self):
        self.__running = True
        while self.__running:
            for event in pygame.event.get():
                if event.type == pygame.quit:
                    self.__running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.__running = False
            self._update()
            self._draw()

    @property
    def window(self):
        return self.__window

    @window.setter
    def window(self, window):
        self.__window = window

    def add_object(self, obj):
        self.__game_objects.append(obj)
                