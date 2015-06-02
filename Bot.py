import pygame
import Actor
from random import randint
from Explosion import Explosion


class Bot(Actor.Actor):
    def __init__(self, world):

        super(Bot, self).__init__(world)
        while True:
            self.x = randint(world.width, world.width + 1000)
            self.y = randint(0, world.height - self.height - 10)
            if not self.is_hit(world.actors):
                break

        self.speed_x = -2
        self.speed_y = 0

        self.next_turn = 3

    def load_image(self):
        self.set_image(pygame.image.load("resources/robot1.png").convert_alpha())

    def update(self):
        super(Bot, self).update()
        self.next_turn -= 1
        super(Bot, self).update()
        if self.x < -self.width:
            self.world.remove_actor(self)
            self.world.health -= 1
        if self.next_turn == 0:
            self.turn_bot()
            self.next_turn = randint(0, 30)
        if self.y + self.height > self.world.height or self.y < 0:
            self.y -= self.speed_y
            self.speed_y = -self.speed_y

    def turn_bot(self):
        self.speed_y = randint(-5, 5)

    def hit(self, actor):
        if type(actor).__name__ != 'Hero':
            self.x -= self.speed_x
            self.y -= self.speed_y
            self.speed_y = -self.speed_y
        if type(actor).__name__ == 'Weapon':
            self.world.remove_actor(actor)
            self.world.remove_actor(self)
            explosion = Explosion(self.world)
            explosion.x = self.x
            explosion.y = self.y
            self.world.add_actor(explosion)

