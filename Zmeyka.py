import pygame
import sys
from zmaeyma_main import Ui_Zmeyka
from random import randrange
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox, QDesktopWidget




class MainHub(QMainWindow, Ui_Zmeyka):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.RES = 500
        self.SIZE = 30
        self.pushButton_4.clicked.connect(self.bigmap)
        self.pushButton_3.clicked.connect(self.medium_map)
        self.pushButton.clicked.connect(self.little_map)
        self.pushButton_2.clicked.connect(self.game)


    def bigmap(self):
        self.RES = 900
        print(self.RES)

    def medium_map(self):
        self.RES = 700
        print(self.RES)

    def little_map(self):
        self.RES = 500
        print(self.RES)



    def close_game(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
                MainHub.show()


    def game(self):

        x, y = randrange(self.SIZE, self.RES - self.SIZE, self.SIZE), randrange(self.SIZE, self.RES - self.SIZE,
                                                                                self.SIZE)
        apple = randrange(self.SIZE, self.RES - self.SIZE, self.SIZE), randrange(self.SIZE, self.RES - self.SIZE,
                                                                                 self.SIZE)
        length = 1
        snake = [(x, y)]
        dx, dy = 0, 0
        fps = 60
        dirs = {'W': True, 'S': True, 'A': True, 'D': True, }
        score = 0
        speed_count, snake_speed = 0, 10

        pygame.init()
        surface = pygame.display.set_mode([self.RES, self.RES])
        clock = pygame.time.Clock()
        font_score = pygame.font.SysFont('Arial', 26, bold=True)
        font_end = pygame.font.SysFont('Arial', 66, bold=True)
        img = pygame.image.load('Fon_dla_zmeyki.png').convert()

        while True:
            surface.blit(img, (0, 0))

            [pygame.draw.rect(surface, pygame.Color('green'), (i, j, self.SIZE - 1, self.SIZE - 1)) for i, j in snake]
            pygame.draw.rect(surface, pygame.Color('orange'), (*apple, self.SIZE, self.SIZE))

            render_score = font_score.render(f'Очки: {score}', 1, pygame.Color('orange'))
            surface.blit(render_score, (5, 5))

            speed_count += 1

            if not speed_count % snake_speed:
                x += dx * self.SIZE
                y += dy * self.SIZE
                snake.append((x, y))
                snake = snake[-length:]

            if snake[-1] == apple:
                apple = randrange(self.SIZE, self.RES - self.SIZE, self.SIZE), randrange(self.SIZE, self.RES - self.SIZE, self.SIZE)
                length += 1
                score += 1
                snake_speed -= 1
                snake_speed = max(snake_speed, 4)

            # смерть тут

            if x < 0 or x > self.RES - self.SIZE or y < 0 or y > self.RES - self.SIZE or len(snake) != len(set(snake)):
                while True:
                    render_end = font_end.render('Игра Окончена', 1, pygame.Color('red'))
                    surface.blit(render_end, (self.RES // 2 - 200, self.RES // 3))
                    pygame.display.flip()
                    self.close_game()



            pygame.display.flip()
            clock.tick(fps)
            self.close_game()
            #MainHub.close()
            key = pygame.key.get_pressed()
            if key[pygame.K_w]:
                if dirs['W']:
                    dx, dy = 0, -1
                    dirs = {'W': True, 'S': False, 'A': True, 'D': True, }
            elif key[pygame.K_s]:
                if dirs['S']:
                    dx, dy = 0, 1
                    dirs = {'W': False, 'S': True, 'A': True, 'D': True, }
            elif key[pygame.K_a]:
                if dirs['A']:
                    dx, dy = -1, 0
                    dirs = {'W': True, 'S': True, 'A': True, 'D': False, }
            elif key[pygame.K_d]:
                if dirs['D']:
                    dx, dy = 1, 0
                    dirs = {'W': True, 'S': True, 'A': False, 'D': True, }

        # добавить базу данных и запись в неё

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainHub()
    ex.show()
    sys.exit(app.exec_())
