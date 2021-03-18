from gamemsg import Message
from ball import Ball
from Windows.game import GameBOT, Game2v2, GameINF

import turtle
import time


class MenuWindow:

    def __init__(self):
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

        msgs = ['Jogar 1P vs COM', 'Jogar 1P vs 2P', 'Jogar INFINITO']
        self.buttons = []

        for i in range(len(msgs)):
            self.buttons.append(Message(msgs[i], pos=(0, -(50 * (i+1))), tam=20, cor='white'))

        self.current = 0

        # Ponteiro

        self.ponteiro = turtle.Turtle()
        self.ponteiro.shape('triangle')
        self.ponteiro.color('orange')
        self.ponteiro.shapesize(stretch_wid=1, stretch_len=1)
        self.ponteiro.penup()
        self.ponteiro.goto((-150, -35))

        # Binds

        self.screen.listen()
        self.screen.onkey(self.ponteiro_down, 'Down')
        self.screen.onkey(self.ponteiro_up, 'Up')
        self.screen.onkey(self.select_game_mode, 'Return')

        self.run()

    def ponteiro_down(self):
        self.current += 1 if self.current < len(self.buttons) - 1 else -self.current

        self.ponteiro.goto((-150, -(50 * self.current + 35)))

    def ponteiro_up(self):
        if self.current == 0:
            self.current = len(self.buttons) - 1
        else:
            self.current -= 1

        self.ponteiro.goto((-150, -(50 * self.current + 35)))

    def select_game_mode(self):
        self.screen.clear()

        if self.current == 0:
            game = GameBOT()
        elif self.current == 1:
            game = Game2v2()
        else:
            game = GameINF()

        game.run_game()
        MenuWindow()

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

                # Fim da renderização

                frames += 1
                delta -= 1

            if time.time() - timer >= 1:
                #print('FPS:', frames)
                frames = 0
                timer += 1