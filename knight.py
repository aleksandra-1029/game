import pygame.sprite


class Knight(pygame.sprite.Sprite):
    def __init__(self, group, ):
        super().__init__(group)

        self.frame_index = 0

        self.x, self.y = 2310, 350
        self.image = pygame.image.load('data/npc/sprites/1.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

