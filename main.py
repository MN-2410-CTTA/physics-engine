# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

gravity = 1000 # change gravity
velocity_y = -100 #change starting velocity
box = [590, 0, 100, 50] # change pos y, pos x, size x, and size y

while running:
    # math
    dt = clock.tick(165) / 1000 # tick(x) is the framerate

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if box[1] <= (620-box[3]): 
        velocity_y += gravity * dt
    else:
        velocity_y = 0

    box[1] += velocity_y * dt

    # renderer
    # renders sky first, then ground, and then the object
    screen.fill("#87CEEB")
    pygame.draw.rect(screen, color="black", rect=(0, 620, 1280, 100))
    pygame.draw.rect(screen, color="black", rect=box)

    pygame.display.flip()

pygame.quit()