import pygame


class Dialoges(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)

        self.dialoges = {1: [], 2: [], 3: []}
        for i in range(4):
            self.dialoges[1].append(
                pygame.image.load(f'data/k_dialoges/1-{i + 1}.png').convert_alpha())
        self.dialoges[2].append(pygame.image.load('data/k_dialoges/2-1.png').convert_alpha())
        for i in range(2):
            self.dialoges[3].append(
                pygame.image.load(f'data/k_dialoges/3-{i + 1}.png').convert_alpha())
        self.image = self.dialoges[1][0]
        self.rect = self.image.get_rect(topleft=(0, 407))
