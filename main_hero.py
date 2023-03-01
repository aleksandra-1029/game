import pygame.sprite
from battle import *
from knight_dialoges import *


class Hero(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)

        self.import_assets()
        self.status = 'down_idle'
        self.frame_index = 0

        self.x, self.y = 140, 70
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.enemy1 = self.enemy2 = False

    def import_assets(self):
        self.animations = {'up': [], 'down': [], 'left': [], 'right': [], 'up_idle': [],
                           'down_idle': [], 'left_idle': [], 'right_idle': []}
        for animation in self.animations.keys():
            path = 'data/movement/' + animation
            self.animations[animation] = self.import_folder(path)

    def animate(self):
        self.frame_index += 1
        self.frame_index %= 2
        self.image = self.animations[self.status][self.frame_index]

    def move(self, side, enemy1, enemy2):

        lvl = open('data/map.txt').read().splitlines()
        self.status = side
        if side == 'up':
            cell1 = self.get_cell(self.x, self.y - 3)
            if lvl[cell1[1]][cell1[0]] == '.':
                self.y -= 3
        elif side == 'down':
            cell1 = self.get_cell(self.x, self.y + 73)
            if lvl[cell1[1]][cell1[0]] == '.':
                self.y += 3
        elif side == 'left':
            cell1 = self.get_cell(self.x - 3, self.y)
            if lvl[cell1[1]][cell1[0]] == '.':
                self.x -= 3
        elif side == 'right':
            cell1 = self.get_cell(self.x + 73, self.y)
            if lvl[cell1[1]][cell1[0]] == '.':
                self.x += 3
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.enemy1 = enemy1
        self.enemy2 = enemy2
        self.enemy_window()
        self.npc()
        return self.enemy1, self.enemy2

    def enemy_window(self):
        if 370 < self.x < 470 and 360 <= self.y <= 490 and self.enemy1:
            app = QApplication(sys.argv)
            ex = BattleWindow()
            ex.show()
            app.exec()
            if ex.enemy_hp == 0:
                self.enemy1 = False
        if 580 < self.x < 680 and 150 <= self.y <= 280 and self.enemy2:
            app = QApplication(sys.argv)
            ex = BattleWindow()
            ex.show()
            app.exec()
            if ex.enemy_hp == 0:
                self.enemy2 = False

    def npc(self):
        if 2260 <= self.x <= 2360 and 280 <= self.y <= 420 and self.enemy1:
            pass

    def get_cell(self, x, y):
        return x // 70, y // 70

    def import_folder(self, path):
        surface_list = list()
        im1 = pygame.image.load(f'{path}/1.png').convert_alpha()
        im2 = pygame.image.load(f'{path}/2.png').convert_alpha()
        surface_list.append(im1)
        surface_list.append(im2)
        return surface_list
