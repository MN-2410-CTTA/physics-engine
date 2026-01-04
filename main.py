# Example file showing a basic pygame "game loop"
import pygame
from pygame.math import Vector2
import physics.body as body, physics.world as world, physics.collision as collision

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

world = world.World()
box1 = body.Body((600, 100), (80, 80), mass=2)
box2 = body.Body((300, 150), (40, 40), mass=20)
world.add_body(box1)
world.add_body(box2)

GROUND_Y = 620
running = True

while running:
    dt = clock.tick(165) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    world.step(dt)
    collision.resolve_ground_collision(box1, GROUND_Y)
    collision.resolve_ground_collision(box2, GROUND_Y)

    screen.fill("#87CEEB")
    pygame.draw.rect(screen, "#7CFC00", rect=[0, 620, 1280, 100])
    for body in world.bodies:
        pygame.draw.rect(screen, "black", body.rect)
    pygame.display.flip()

pygame.quit()
