from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QWidget, QApplication, QTextBrowser, QPushButton
import sys
from random import randint


class BattleWindow(QWidget):
    def __init__(self, p_hp=20):
        self.player_hp = p_hp
        self.enemy_hp = 10
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(400, 100, 500, 750)
        self.setWindowTitle('Битва')
        self.setWindowIcon(QIcon('data/icon.png'))
        self.setStyleSheet('background-color : #87817b')

        self.text = QTextBrowser(self)
        self.text.move(10, 10)
        self.text.resize(480, 450)
        self.text.setStyleSheet('background-color : #66615d; color : #ccc6c0')
        self.text.setFont(QFont('Monospace', 10))

        self.attack = QPushButton('Атаковать', self)
        self.attack.move(150, 480)
        self.attack.resize(200, 50)
        self.attack.clicked.connect(self.attack_enemy)
        self.attack.setStyleSheet('background-color : #66615d; color : #ccc6c0')
        self.attack.setFont(QFont('Monospace', 12))

        self.run = QPushButton('Убежать', self)
        self.run.move(150, 620)
        self.run.resize(200, 50)
        self.run.setStyleSheet('background-color : #66615d; color : #ccc6c0')
        self.run.setFont(QFont('Monospace', 12))
        self.run.clicked.connect(self.run_f)

    def run_f(self):
        self.close()

    def attack_enemy(self):
        if self.enemy_hp > 0 and self.player_hp > 0:
            n = randint(2, 5)
            self.enemy_hp -= n
            if self.enemy_hp < 0:
                self.enemy_hp = 0
            if self.enemy_hp == 10 - n:
                self.text.setText(f'Вы нанесли врагу {n} урона! '
                                  f'У него осталось {self.enemy_hp} здоровья!')
            else:
                self.text.setText(
                    self.text.toPlainText() + f'\nВы нанесли врагу {n} урона! '
                                              f'У него осталось {self.enemy_hp} здоровья!')
            if self.enemy_hp > 0:
                n = randint(1, 5)
                self.player_hp -= n
                if self.player_hp < 0:
                    self.player_hp = 0
                self.text.setText(
                    self.text.toPlainText() + f'\nВраг нанёс вам {n} урона! У вас '
                                              f'осталось {self.player_hp} здоровья!')
                if self.player_hp == 0:
                    self.text.setText(
                        self.text.toPlainText() + f'\nИгра окончена!')
            else:
                self.text.setText(
                    self.text.toPlainText() + f'\nВы победили! Нажмите кнопку атаки или закройте '
                                              f'окно')
        else:
            self.close()
