import pygame.sprite


class Enemy(pygame.sprite.Sprite):
    def __init__(self, group,x, y):
        super().__init__(group)
        self.is_alive = False

        self.frame_index = 0

        self.x, self.y = x, y
        self.image = pygame.image.load('data/enemy/sprites/1.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

