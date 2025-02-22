import pygame


class PhysicsEntity:
    def __init__(self, game, entity_type, pos, size):
        self.game = game
        self.type = entity_type
        self.pos = list(pos) # converting tuple to list cz we wonna change pos
        self.size = size
        self.velocity = [0, 0]


    def player_rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])


    def update(self, tilemap, win, movement=(0, 0)): # will get info how much we wonna move right now
        frame_movement = (movement[0] + self.velocity[0], movement[1] + self.velocity[1])

        self.velocity[1] = min(4, self.velocity[1] + 0.1)

        self.pos[0] += frame_movement[0]
        entity_rect = self.player_rect()
        for rect in tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(rect):
                if frame_movement[0] > 0:
                    entity_rect.right = rect.left
                if frame_movement[0] < 0:
                    entity_rect.left = rect.right
                self.pos[0] = entity_rect.x
        pygame.draw.rect(win, (255, 0, 0), entity_rect, width=1)


        self.pos[1] += frame_movement[1]
        entity_rect = self.player_rect()
        for rect in tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(rect):
                if frame_movement[1] > 0:
                    entity_rect.bottom = rect.top
                if frame_movement[1] < 0:
                    entity_rect.top = rect.bottom
                self.pos[1] = entity_rect.y
        pygame.draw.rect(win, (255, 0, 0), entity_rect, width=1)


    def render(self, surf):
        surf.blit(self.game.resources['player'], self.pos)