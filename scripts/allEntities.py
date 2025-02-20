import pygame


class PhysicsEntity:
    def __init__(self, game, entity_type, pos, size):
        self.game = game
        self.type = entity_type
        self.pos = list(pos) # converting tuple to list cz we wonna change pos
        self.size = size
        self.velocity = [0, 0]


    def update(self, movement=(0, 0)): # will get info how much we wonna move right now
        frame_movement = (movement[0] + self.velocity[0], movement[1] + self.velocity[1])

        self.pos[0] += frame_movement[0]
        self.pos[1] += frame_movement[1]


    def render(self, surf):
        surf.blit(self.game.assets['player'], self.pos)