import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("My first game screen")

sun = pygame.image.load("C:\\Users\\benny\\Desktop\\PythonCourse\\lesson1\\sun-blasts-a-m66-flare.jpg")
sun = pygame.transform.scale(sun, (500, 500))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.blit(sun, (0, 0))
    pygame.display.update()

