import pygame

pygame.init()

scr_width, scr_height = 600, 650
scr_width, scr_height = 600, 650

scr = pygame.display.set_mode((scr_width,scr_height))

pygame.display.set_caption('adding image and background image')

background_image = pygame.transform.scale(
    pygame.image.load('background.jpg').convert(),
    (scr_width,scr_height))



done = False

while not done:
    for event in pygame.event.get():
        if event.type ==pygame.quit:
            pygame.quit()

    scr.blit(background_image,(0,0))

    pygame.display.flip()

