import pygame
from map import *


class Camera:
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = pygame.Rect(0, 0, width, height)

    def update(self, player):
        self.player = player
        self.state = self.camera_func(self.state, player.rect)


    def apply(self, target):
        return target.rect.move(self.state.topleft)

