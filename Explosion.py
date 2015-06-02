import pygame
import Actor

images = []
def load(images):
    if images:
        return images;

    images.append(pygame.image.load("resources/expl1.png").convert_alpha())
    images.append(pygame.image.load("resources/expl2.png").convert_alpha())
    images.append(pygame.image.load("resources/expl3.png").convert_alpha())
    images.append(pygame.image.load("resources/expl4.png").convert_alpha())
    images.append(pygame.image.load("resources/expl5.png").convert_alpha())
    images.append(pygame.image.load("resources/expl6.png").convert_alpha())
    return images;

class Explosion(Actor.Actor):
    def __init__(self, world):
        self.images = []
        self.step = 0
        super(Explosion, self).__init__(world)

    def load_image(self):
        self.images=load(images)
        self.set_image(self.images[0])

    def update(self):
        self.set_image(self.images[self.step])
        self.step += 1
        if self.step == 6:
            self.world.remove_actor(self)
            self.world.points += 100

