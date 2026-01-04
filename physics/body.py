import pygame
from pygame.math import Vector2

class Body:
    def __init__(self, position, size, mass=1):
        self.position = Vector2(position)
        self.previous_position = Vector2(position)
        self.acceleration = Vector2(0, 0)
        self.mass = mass
        self.size = size
        self.rect = pygame.Rect(self.position.x, self.position.y, size[0], size[1])

    def apply_force(self, force):
        self.acceleration += force / self.mass

    def integrate(self, dt):
        displacement = self.position - self.previous_position
        next_position = self.position + displacement + self.acceleration * dt * dt

        self.previous_position = self.position
        self.position = next_position

        self.rect.topleft = self.position
        self.acceleration = Vector2(0, 0)

    def velocity(self, dt):
        return (self.position - self.previous_position) / dt