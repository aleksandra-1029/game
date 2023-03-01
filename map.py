import pygame
from main_hero import *


def load_level():
    filename = "data/map.txt"
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    return level_map


tile_width = tile_height = 70


class Map(pygame.sprite.Sprite):

    def __init__(self, group):
        super().__init__(group)
        self.image = pygame.image.load('data/map.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=(0, 0))