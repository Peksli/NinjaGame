import pygame


class Tilemap:
    def __init__(self, game, tile_size=16):
        self.game = game
        self.tile_size = tile_size
        self.tilemap = dict()
        self.offgrid_tiles = dict()

        for i in range(11):
            self.tilemap[str(3 + i) + ";10"] = {'type': 'grass', 'image_id': 1, 'pos': (3 + i, 10)}
            self.tilemap['10;' + str(3 + i)] = {'type': 'stone', 'image_id': 1, 'pos': (10, 3 + i)}


    def tiles_around(self):
        pass


    def render(self, surf):
        for tile_loc in self.tilemap:
            current_tile = self.tilemap[tile_loc] # gettin concrete info(type, variant, pos) using str loc

            # blitting images from resources to surface
            surf.blit(self.game.resources[current_tile['type']][current_tile['image_id']],
                         (self.tile_size * current_tile['pos'][0], self.tile_size * current_tile['pos'][1]))

