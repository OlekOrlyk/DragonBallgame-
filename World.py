import pygame
from Bot import Bot
from  Hero import Hero

class World(pygame.Rect):
    def __init__(self, width, height):
        super(World, self).__init__(0, 0, width, height)
        self.clear()

    def add_actor(self, actor):
        self.actors.append(actor)

    def remove_actor(self, actor):
        self.actors.remove(actor)

    def update(self):
        bots = 0
        for actor in self.actors:
            actor.update()
            if type(actor).__name__ == 'Bot':
                bots += 1
        if bots < 20:
            self.add_actor(Bot(self))

    def draw(self, screen):
        for actor in self.actors:
            actor.draw(screen)

    def clear (self):
        self.actors = []
        self.health = 20
        self.points = 0 
        self.herosayjin = Hero(self)
        self.add_actor(self.herosayjin)
        for i in range(0, 20):
            self.add_actor(Bot(self))