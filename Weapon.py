import pygame
import Actor


class Weapon(Actor.Actor):
    def __init__(self, world):
        super(Weapon, self).__init__(world)
        self.x = 0
        self.y = 0
        self.speed_x = 15
        self.speed_y = 0

    def load_image(self):
        self.set_image(pygame.image.load("resources/little hit.png").convert_alpha())

    def update(self):
        super(Weapon, self).update()
        if self.x > self.world.width:
            self.world.remove_actor(self)
