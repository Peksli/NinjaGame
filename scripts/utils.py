import pygame
import os

DEFAULT_PATH = 'data/images/'

def load_image(path):
    img = pygame.image.load(DEFAULT_PATH + path).convert()
    img.set_colorkey((0, 0, 0))

    return img


def load_images(path):
    list_images = []
    for spec_image_path in os.listdir(DEFAULT_PATH + path):
        list_images.append(load_image(path + '/' + spec_image_path))

    return list_images

