from gamemsg import Message
from ball import Ball
from game import GameBOT, Game2v2, GameINF

import turtle
import time


class MenuWindow:

    def __init__(self, color_left='white', color_right='white', cor_bolinha='white'):
        # Iniciar a Tela

        self.screen = turtle.Screen()
        self.screen.bgcolor("black")
        self.screen.setup(width=800, height=600)
        self.screen.title("GhuPong")
        self.screen.tracer(0)
        self.screen.listen()

        # Título

        self.title = Message('GhuPong', pos=(0, 125), tam=60, tipo="bold")

        # Botões

        msgs = ['Jogar 1P vs COM', 'Jogar 1P vs 2P', 'Jogar INFINITO',  'Configurações']
        self.buttons = []

        for i in range(len(msgs)):
            self.buttons.append(Message(msgs[i], pos=(-100, -(50 * (i+1))), tam=20, cor='white', alin='left'))

        self.current = 0
        self.ball = Ball()

        # Ponteiro

        self.ponteiro = turtle.Turtle()
        self.ponteiro.shape('triangle')
        self.ponteiro.color('orange')
        self.ponteiro.shapesize(stretch_wid=1, stretch_len=1)
        self.ponteiro.penup()
        self.ponteiro.goto((-125, -35))

        # Binds

        self.screen.listen()
        self.screen.onkey(self.ponteiro_down, 'Down')
        self.screen.onkey(self.ponteiro_up, 'Up')
        self.screen.onkey(self.select_game_mode, 'Return')

        # CORES PLATAFORMAS

        self.c_right = color_right
        self.c_left = color_left
        self.c_ball = cor_bolinha

        self.run()

    def ponteiro_down(self):
        self.current += 1 if self.current < len(self.buttons) - 1 else -self.current

        self.ponteiro.goto((-125, -(50 * self.current + 35)))

    def ponteiro_up(self):
        self.current -= 1 if self.current != 0 else -(len(self.buttons) - 1)

        self.ponteiro.goto((-125, -(50 * self.current + 35)))

    def select_game_mode(self):
        self.screen.clear()

        if self.current == 0:
            tela = GameBOT(self.c_left, self.c_right, self.c_ball)
        elif self.current == 1:
            tela = Game2v2(self.c_left, self.c_right, self.c_ball)
        elif self.current == 2:
            tela = GameINF(self.c_left, self.c_right, self.c_ball)
        else:
            tela = ConfigWindow(self)

        cores = tela.run()

        MenuWindow(cores[0], cores[1], cores[2])

    def run(self):
        # Sistema de FPS

        last_time = time.time()
        tick_rate = 60
        ns = 1 / tick_rate
        delta = 0
        frames = 0
        timer = time.time()

        game_is_on = True
        while game_is_on:
            now = time.time()
            delta += (now - last_time) / ns
            last_time = now

            if delta >= 1:

                # Renderização do jogo

                self.screen.update()
                self.ball.move_at_menu()

                # Fim da renderização

                frames += 1
                delta -= 1

            if time.time() - timer >= 1:
                print('FPS:', frames)
                frames = 0
                timer += 1


class ConfigWindow:

    def __init__(self, menu):

        # Iniciar a Tela

        self.screen = turtle.Screen()
        self.screen.bgcolor("black")
        self.screen.setup(width=800, height=600)
        self.screen.title("GhuPong")
        self.screen.tracer(0)
        self.screen.listen()

        # Título

        self.titulo = Message('Configurações', pos=(-250, 250), tam=25, tipo="bold")

        # Botões

        msgs = ['Cor da plat 1P', 'Cor da plat 2P (COM)', 'Cor da bolinha', 'Voltar']
        self.buttons = []

        for i in range(len(msgs)):
            self.buttons.append(Message(msgs[i], pos=(-300, (150-50*i)), tam=20, cor='white', alin='left'))

        # Quadrados com as cores

        self.q_left = turtle.Turtle()
        self.q_left.shape('square')
        self.q_left.color(menu.c_left)
        self.q_left.shapesize(stretch_wid=1, stretch_len=1)
        self.q_left.penup()
        self.q_left.goto((20, 165))

        self.q_right = turtle.Turtle()
        self.q_right.shape('square')
        self.q_right.color(menu.c_right)
        self.q_right.shapesize(stretch_wid=1, stretch_len=1)
        self.q_right.penup()
        self.q_right.goto((20, 115))

        self.q_bola = turtle.Turtle()
        self.q_bola.shape('square')
        self.q_bola.color(menu.c_ball)
        self.q_bola.shapesize(stretch_wid=1, stretch_len=1)
        self.q_bola.penup()
        self.q_bola.goto((20, 65))

        # Ponteiro

        self.ponteiro = turtle.Turtle()
        self.ponteiro.shape('triangle')
        self.ponteiro.color('orange')
        self.ponteiro.shapesize(stretch_wid=1, stretch_len=1)
        self.ponteiro.penup()
        self.ponteiro.goto((-325, 170))

        self.current = 0

        # Lista de cores

        self.list_cores = ['white', 'blue', 'magenta', 'orange', 'red', 'green', 'yellow']
        self.cor_left = self.list_cores.index(menu.c_left)
        self.cor_right = self.list_cores.index(menu.c_right)
        self.cor_bola = self.list_cores.index(menu.c_ball)

        # Binds

        self.screen_on = True

        self.screen.listen()
        self.screen.onkey(self.ponteiro_down, 'Down')
        self.screen.onkey(self.ponteiro_up, 'Up')
        self.screen.onkey(self.select_option, 'Return')

    def ponteiro_down(self):
        self.current += 1 if self.current < len(self.buttons) - 1 else -self.current

        self.ponteiro.goto((-325, (-50 * self.current + 170)))

    def ponteiro_up(self):
        if self.current == 0:
            self.current = len(self.buttons) - 1
        else:
            self.current -= 1

        self.ponteiro.goto((-325, (-50 * self.current + 170)))

    def select_option(self):
        if self.current == len(self.buttons) - 1:
            self.screen_on = False

        elif self.current == 0:
            try:
                self.cor_left += 1
                self.q_left.color(self.list_cores[self.cor_left])
            except IndexError:
                self.cor_left = 0
                self.q_left.color(self.list_cores[0])

        elif self.current == 1:
            try:
                self.cor_right += 1
                self.q_right.color(self.list_cores[self.cor_right])
            except IndexError:
                self.cor_right = 0
                self.q_right.color(self.list_cores[0])

        elif self.current == 2:
            try:
                self.cor_bola += 1
                self.q_bola.color(self.list_cores[self.cor_bola])
            except IndexError:
                self.cor_bola = 0
                self.q_bola.color(self.list_cores[0])

    def run(self):
        last_time = time.time()
        tick_rate = 60
        ns = 1 / tick_rate
        delta = 0
        frames = 0
        timer = time.time()

        while self.screen_on:
            now = time.time()
            delta += (now - last_time) / ns
            last_time = now

            if delta >= 1:
                # Renderização do jogo

                self.screen.update()

                # Fim da renderização

                frames += 1
                delta -= 1

            if time.time() - timer >= 1:
                # print('FPS:', frames)
                frames = 0
                timer += 1

        self.screen.clear()

        return self.list_cores[self.cor_left], self.list_cores[self.cor_right], self.list_cores[self.cor_bola]
