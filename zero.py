import pygame
import random


from World import World

BLACK = (0, 0, 0)
pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont("monospace", 30)
pygame.display.set_caption('Hero Sayjin')
size = pygame.display.list_modes()[0]
screen = pygame.display.set_mode(size,pygame.FULLSCREEN)
image_background = pygame.transform.scale(pygame.image.load("resources/image.jpg").convert_alpha(),size)
image_over = pygame.image.load("resources/gameover.png").convert_alpha()
world = World(size[0], size[1])


clock = pygame.time.Clock()
done = False
while not done:

    if world.health <= 0:
        for event in pygame.event.get():
            if  event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                done = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                world.clear()

        screen.fill(BLACK)
        screen.blit(image_over,
                    ((world.width - image_over.get_width()) / 2, (world.height - image_over.get_height()) / 2))

    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    world.herosayjin.move(-10, 0)
                if event.key == pygame.K_RIGHT:
                    world.herosayjin.move(10, 0)
                if event.key == pygame.K_UP:
                    world.herosayjin.move(0, -10)
                if event.key == pygame.K_DOWN:
                    world.herosayjin.move(0, 10)
                if event.key == pygame.K_SPACE:
                    world.herosayjin.fire()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    world.herosayjin.move(10, 0)
                if event.key == pygame.K_RIGHT:
                    world.herosayjin.move(-10, 0)
                if event.key == pygame.K_UP:
                    world.herosayjin.move(0, 10)
                if event.key == pygame.K_DOWN:
                    world.herosayjin.move(0, -10)

        screen.blit(image_background, (0, 0))
        label = myfont.render("Life:" + str(world.health), 1, (0, 0, 0))
        screen.blit(label, (world.width - label.get_width(), 0))
        label = myfont.render("Points:" + str(world.points), 1, (0, 0, 0))
        screen.blit(label, (0, 0))

        world.update()
        world.draw(screen)

    pygame.display.flip()
    clock.tick(20)

pygame.quit()
