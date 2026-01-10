import pygame

pygame.init()

display = pygame.display.set_mode((350,350))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.draw.rect(display, (150, 50, 250), pygame.Rect(30, 30, 60, 60))

    pygame.display.flip()