import pygame
import Actor
from Weapon import Weapon


class Hero(Actor.Actor):
    def __init__(self, world):
        super(Hero, self).__init__(world)
        self.fire_now = 0

    def load_image(self):
        self.set_image(pygame.image.load("resources/actor.png").convert_alpha())
        self.image_stop = self.image
        self.image_move = pygame.image.load("resources/actor move.png").convert_alpha()
        self.image_jump = pygame.image.load("resources/actor jump.png").convert_alpha()
        self.image_back = pygame.image.load("resources/actor move backwards.png").convert_alpha()
        self.image_fire = pygame.image.load("resources/herofire.png").convert_alpha()

        self.image_down = self.image_jump
        self.image_up = self.image_jump
        self.image_left = self.image_back
        self.image_right = self.image_move
        self.image_left_down = self.image_back
        self.image_left_up = self.image_back
        self.image_right_down = self.image_jump
        self.image_right_up = self.image_move

    def update(self):
        super(Hero, self).update()
        if not self.world.contains(self):
            self.x -= self.speed_x
            self.y -= self.speed_y

        if self.fire_now == 1:
            bullet = Weapon(self.world)
            bullet.x = self.x + 15
            bullet.y = self.y + 18
            self.world.add_actor(bullet)
        if self.fire_now:
            self.fire_now -= 1
            self.image = self.image_fire
            return
        if self.speed_x == 0 and self.speed_y == 0:
            self.set_image(self.image_stop)
        if self.speed_x > 0 and self.speed_y == 0:
            self.set_image(self.image_right)
        if self.speed_x < 0 and self.speed_y == 0:
            self.set_image(self.image_left)
        if self.speed_x == 0 and self.speed_y > 0:
            self.set_image(self.image_down)
        if self.speed_x == 0 and self.speed_y < 0:
            self.set_image(self.image_up)
        if self.speed_x > 0 and self.speed_y < 0:
            self.set_image(self.image_right_up)
        if self.speed_x > 0 and self.speed_y > 0:
            self.set_image(self.image_right_down)
        if self.speed_x < 0 and self.speed_y > 0:
            self.set_image(self.image_left_down)
        if self.speed_x < 0 and self.speed_y < 0:
            self.set_image(self.image_left_up)

    def fire(self):

        if self.fire_now:
            return
        self.fire_now = 5
