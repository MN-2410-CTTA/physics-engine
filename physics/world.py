import pygame
from pygame.math import Vector2

class World:
    def __init__(self, gravity=(0, 1000)):
        self.gravity = Vector2(gravity)
        self.bodies = []

    def add_body(self, body):
        self.bodies.append(body)

    def step(self, dt):
        for body in self.bodies:
            body.apply_force(self.gravity * body.mass)
            body.integrate(dt)
