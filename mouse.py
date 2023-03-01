import pygame


class Mouse(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('data/arrow.png')

    def arrow(self, pos, screen):
        if pygame.mouse.get_focused():
            self.update(pos, screen)

    def update(self, pos, screen):
        self.rect = self.image.get_rect(center=pos)


