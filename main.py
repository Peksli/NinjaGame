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
            'background': load_image('background.png'),
            'player': load_image('entities/player.png'),
            'grass':  load_images('tiles/grass'),
            'stone':  load_images('tiles/stone')
        }

        self.movement = [False, False]

        self.camera_pos = [0, 0]


    def run(self):
        while True:
            self.current_window.blit(self.resources['background'], (0, 0))

            self.camera_pos[0] += (self.player.player_rect().centerx - self.current_window.get_width()/2 -  self.camera_pos[0]) / 20
            self.camera_pos[1] += (self.player.player_rect().centery - self.current_window.get_height()/2 - self.camera_pos[1]) / 20
            print(self.camera_pos[0], self.camera_pos[1])

            self.tilemap.render(self.current_window, self.camera_pos)


            self.player.update(self.tilemap,self.current_window, (self.movement[1] - self.movement[0], 0))
            self.player.render(self.current_window, self.camera_pos)


            print(self.tilemap.physics_rects_around(self.player.pos))

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
