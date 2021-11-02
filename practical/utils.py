import pygame
from pygame.math import Vector2
import random

WHITE = 255, 255, 255
BLACK = 0, 0, 0


class Organism(pygame.sprite.Sprite):
    vector_mag = 200

    def __init__(self):
        super(Organism, self).__init__()
        self.image = pygame.image.load("virus.png")
        self.rect = self.image.get_rect()
        self.target_pos = Vector2(0, 0)
        self.target_rect = self.rect
        self.velocity = Vector2(0, 0)

    def update(self, dt, display):
        if self.rect.colliderect(self.target_rect):
            self.target_pos.x = random.randint(0, 650)
            self.target_pos.y = random.randint(0, 650)

        self.velocity = Vector2(self.target_pos.x - self.rect.x, self.target_pos.y - self.rect.y)
        self.velocity = self.velocity.normalize() * self.vector_mag
        self.target_rect = pygame.draw.circle(display, WHITE, (self.target_pos.x, self.target_pos.y), 10)
        self.rect.x += self.velocity.x * dt
        self.rect.y += self.velocity.y * dt


class Enemy(Organism):
    def __init__(self, name):
        super(Enemy, self).__init__()
        self.image = pygame.image.load("enemy.png")
        self.rect = self.image.get_rect()
