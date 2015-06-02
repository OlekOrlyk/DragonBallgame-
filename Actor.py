import pygame


class Actor(pygame.Rect):
    def __init__(self, world):
        self.world = world
        self.x = 0
        self.y = 0
        self.speed_x = 0
        self.speed_y = 0
        self.load_image()

    def load_image(self):
        pass

    def move(self, x, y):
        self.speed_x += x
        self.speed_y += y

    def is_hit(self, actors):
        for actor in actors:
            if actor != self and self.colliderect(actor):
                return actor
        return False

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        actor = self.is_hit(self.world.actors)
        if actor != False:
            self.hit(actor)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def set_image(self, image):
        self.w = image.get_width()
        self.h = image.get_height()
        self.image = image

    def hit(self, actor):
        pass
