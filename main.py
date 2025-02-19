import sys
import pygame

pygame.init()

window = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Ninja Game')

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    pygame.display.update()
    clock.tick(60)
