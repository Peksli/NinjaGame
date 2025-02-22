import sys
import pygame

from scripts.utils import load_image
from scripts.utils import load_images
from scripts.allEntities import PhysicsEntity
from scripts.tilemap import Tilemap


class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption('Ninja Game')
        self.window = pygame.display.set_mode((640, 480))
        self.current_window = pygame.Surface((320, 240))

        self.clock = pygame.time.Clock()

        self.player = PhysicsEntity(self, 'player', (80, 50), (8, 16))
        self.tilemap = Tilemap(self, tile_size=16)

        self.resources = {
            'player': load_image('entities/player.png'),
            'grass':  load_images('tiles/grass'),
            'stone':  load_images('tiles/stone')
        }

        self.movement = [False, False]


    def run(self):
        while True:
            self.current_window.fill((14, 219, 248))
            self.tilemap.render(self.current_window)

            self.player.update((self.movement[1] - self.movement[0], 0))
            print(self.tilemap.tiles_around(self.player.pos))
            self.player.render(self.current_window)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = True
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = True

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False

            self.window.blit(pygame.transform.scale(self.current_window, self.window.get_size()), (0, 0))
            pygame.display.update()
            self.clock.tick(60)


Game().run()
