import sys

import pygame
from mouse import Mouse
from knight import *
from enemy import *
from camera import *
from main_hero import *
from knight_dialoges import *


class Game:
    def __init__(self):
        pygame.init()

        icon = pygame.image.load('data/icon.png')
        pygame.display.set_icon(icon)
        size = self.x, self.y = 1100, 700
        self.screen = pygame.display.set_mode(size)
        self.screen.fill((0, 0, 0))
        pygame.display.set_caption('Игра')
        self.running = True
        self.clock = pygame.time.Clock()
        self.mouse = Mouse()
        self.pos = 0, 0
        self.map_group = pygame.sprite.Group()
        self.map = Map(self.map_group)
        self.level = load_level()
        self.knight_group = pygame.sprite.Group()
        self.npc = Knight(self.knight_group)
        self.enemy_group = pygame.sprite.Group()
        self.enemy = Enemy(self.enemy_group, 420, 420)
        self.enemy_group2 = pygame.sprite.Group()
        self.enemy2 = Enemy(self.enemy_group2, 630, 210)
        self.player_group = pygame.sprite.Group()
        self.player = Hero(self.player_group)
        self.camera = Camera(self.camera_func, 1100, 700)
        self.d_group = pygame.sprite.Group()
        self.d = Dialoges(self.d_group)

    def camera_func(self, camera, target_rect):
        l = -self.player.x + self.x // 2
        t = -self.player.y + self.y // 2
        l = min(0, l)
        l = max(-1700, l)
        t = min(0, t)
        t = max(-700, t)

        return pygame.Rect(l, t, 1100, 700)

    def run(self):
        d = False
        n = 0
        k = 0
        l = 1
        en = False
        m = False
        while self.running:
            self.screen.fill((0, 0, 0))
            while True:
                event = pygame.event.poll()
                if event.type == pygame.NOEVENT:
                    break
                elif event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEMOTION:
                    pos = event.pos
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        m = False
                        self.player.status = 'up_idle'
                    elif event.key == pygame.K_a:
                        m = False
                        self.player.status = 'left_idle'
                    elif event.key == pygame.K_s:
                        m = False
                        self.player.status = 'down_idle'
                    elif event.key == pygame.K_d:
                        m = False
                        self.player.status = 'right_idle'
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        m = True
                        s = 'up'
                    elif event.key == pygame.K_a:
                        m = True
                        s = 'left'
                    elif event.key == pygame.K_s:
                        m = True
                        s = 'down'
                    elif event.key == pygame.K_d:
                        m = True
                        s = 'right'
                    elif event.key == pygame.K_SPACE:
                        d = True
                        n += 1
            if d and 2240 < self.player.x < 2380 and 280 < self.player.y < 420:
                if l == 1:
                    if n <= 4:
                        self.d.image = self.d.dialoges[1][n - 1]
                    else:
                        n = 0
                        l += 1
                        d = False
                        en = True
                        self.enemy.is_alive = True
                        self.enemy2.is_alive = True

                elif l == 2 and not self.enemy.is_alive and not self.enemy2.is_alive:
                    if n <= 2:
                        self.d.image = self.d.dialoges[3][n - 1]
                    elif n == 3:
                        sys.exit()

            if m:
                self.enemy.is_alive, self.enemy2.is_alive = self.player.move(s, self.enemy.is_alive,
                                                                             self.enemy2.is_alive)

            self.camera.update(self.player)
            for e in self.map_group:
                self.screen.blit(e.image, self.camera.apply(e))
            for e in self.player_group:
                self.screen.blit(e.image, self.camera.apply(e))
            for e in self.knight_group:
                self.screen.blit(e.image, self.camera.apply(e))
            if en:
                if self.player.enemy1:
                    for e in self.enemy_group:
                        self.screen.blit(e.image, self.camera.apply(e))
                if self.player.enemy2:
                    for e in self.enemy_group2:
                        self.screen.blit(e.image, self.camera.apply(e))
            if d and 2240 < self.player.x < 2380 and 280 < self.player.y < 420:
                self.d_group.draw(self.screen)

            if k == 400:
                k = 0
                self.player.animate()

            self.clock.tick(50)
            k += 50

            pygame.display.flip()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    sys.excepthook = except_hook
    game = Game()
    game.run()
