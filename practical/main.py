import pygame
import random

from practical.utils import Organism, Enemy, BLACK

pygame.init()
pygame.display.set_caption("Organisms")


display = pygame.display.set_mode([650, 650])
nexit = True


px, py = 325, 325
radius = 10

player = Organism()
enemy = Enemy("enemy1")
enemy2 = Enemy("enemy2")

neutrals = pygame.sprite.Group()
neutrals.add(player)

enemies = pygame.sprite.Group()
enemies.add(enemy)
enemies.add(enemy2)

clock = pygame.time.Clock()

while nexit:
    dt = clock.tick(30) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            nexit = False

    display.fill(BLACK)
    player.update(dt, display)
    neutrals.draw(display)
    enemies.update(dt, display)
    enemies.draw(display)

    pygame.display.flip()

pygame.quit()
