# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

a = 1000
u = -500
box = [639, 620, 100, 100]

while running:
    dt = clock.tick(165) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.draw.rect(screen, color="black", rect=box)
    pos = box[1]
    box[1] += 0.5 * (u + u + (a * dt)) * dt
    u =  (box[1] - pos) / dt

    

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("#87CEEB")

    

    # flip() the display to put your work on screen
    

    

    pygame.display.flip()
pygame.quit()