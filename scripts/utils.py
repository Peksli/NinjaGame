import pygame

DEFAULT_PATH = 'data/images/'

def load_image(path):
    img = pygame.image.load(DEFAULT_PATH + path).convert()
    img.set_colorkey((0, 0, 0))
    return img