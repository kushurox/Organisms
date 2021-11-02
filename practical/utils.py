import math
import pygame
import random

WHITE = 255, 255, 255
BLACK = 0, 0, 0


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __mul__(self, other: int):
        return Vector(self.x * other, self.y * other)

    def __truediv__(self, other):
        return Vector(self.x / other, self.y / other)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def magnitude(self):
        return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2))

    def normalize(self):
        mag = self.magnitude()
        return self / mag


class Organism(pygame.sprite.Sprite):
    vector_mag = 200

    def __init__(self):
        super(Organism, self).__init__()
        self.image = pygame.image.load("virus.png")
        self.rect = self.image.get_rect()
        self.target_pos = Vector(0, 0)
        self.target_rect = self.rect
        self.velocity = Vector(0, 0)

    def update(self, dt, display):
        if self.rect.colliderect(self.target_rect):
            self.target_pos.x = random.randint(0, 650)
            self.target_pos.y = random.randint(0, 650)

        self.velocity = Vector(self.target_pos.x - self.rect.x, self.target_pos.y - self.rect.y)
        self.velocity = self.velocity.normalize() * self.vector_mag
        self.target_rect = pygame.draw.circle(display, WHITE, (self.target_pos.x, self.target_pos.y), 10)
        self.rect.x += self.velocity.x * dt
        self.rect.y += self.velocity.y * dt


class Enemy(Organism):
    def __init__(self, name):
        super(Enemy, self).__init__()
        self.image = pygame.image.load("enemy.png")
        self.rect = self.image.get_rect()