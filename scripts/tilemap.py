import pygame


COEFFICIENTS_TILES_AROUND = [(0, 0), (1, 0), (0, 1), (1, 1), (-1, 0), (0, -1), (-1, 1), (1, -1), (-1, -1)]
PHYSICS_ENABLED_TILES = {'grass', 'stone'}


class Tilemap:
    def __init__(self, game, tile_size=16):
        self.game = game
        self.tile_size = tile_size
        self.tilemap = dict()
        self.offgrid_tiles = dict()

        for i in range(11):
            self.tilemap[str(3 + i) + ";10"] = {'type': 'grass', 'image_id': 1, 'pos': (3 + i, 10)}
            self.tilemap['10;' + str(3 + i)] = {'type': 'stone', 'image_id': 1, 'pos': (10, 3 + i)}


    def tiles_around(self, pos):
        tiles = []
        player_tile_loc = (int(pos[0] // self.tile_size), int(pos[1] // self.tile_size))
        for offset in COEFFICIENTS_TILES_AROUND:
            tile_offset_loc = str(player_tile_loc[0] + offset[0]) + ';' + str(player_tile_loc[1] + offset[1])
            if tile_offset_loc in self.tilemap:
                tiles.append(self.tilemap[tile_offset_loc])

        return tiles


    def physics_rects_around(self, pos):
        rects = []
        for tile in self.tiles_around(pos):
            if tile['type'] in PHYSICS_ENABLED_TILES:
                rects.append(pygame.Rect(
                    tile['pos'][0] * self.tile_size,
                    tile['pos'][1] * self.tile_size,
                    self.tile_size,
                    self.tile_size
                ))

        return rects


    def render(self, surf, camera_at=(0, 0)):
        for tile_loc in self.tilemap:
            current_tile = self.tilemap[tile_loc] # gettin concrete info(type, variant, pos) using str loc

            # blitting images from resources to surface
            surf.blit(self.game.resources[current_tile['type']][current_tile['image_id']],
                         (self.tile_size * current_tile['pos'][0] - camera_at[0], self.tile_size * current_tile['pos'][1] - camera_at[1]))