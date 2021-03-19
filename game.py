from ball import Ball
from plat import Plat
from scoreboard import Scoreboard
from gamemsg import Message

import turtle
import time


class Gamescreen:
    def __init__(self, color_left, color_right, color_ball):
        # Iniciar a Tela

        self.screen = turtle.Screen()
        self.screen.bgcolor("black")
        self.screen.setup(width=800, height=600)
        self.screen.title("GhuPong")
        self.screen.tracer(0)

        # Inserir os widgets na tela

        self.r_plat = Plat((350, 0), color=color_right)
        self.l_plat = Plat((-350, 0), color=color_left)
        self.ball = Ball(color=color_ball)
        self.scoreboard = Scoreboard()

        # Traço no meio da tela

        trace = turtle.Turtle()
        trace.shape('square')
        trace.color('white')
        trace.shapesize(stretch_wid=30, stretch_len=0.2)
        trace.penup()

        # Guardando as cores

        self.cor_left, self.cor_right, self.cor_bola = color_left, color_right, color_ball

    def check_screen_collision(self):

        # Detecta colisão com a parede de cima
        if self.ball.ycor() > 290 or self.ball.ycor() < -290:
            self.ball.bounce_y()

        # Detecta se a plataforma R falha
        if self.ball.xcor() > 390:
            self.ball.reset_position()
            self.scoreboard.l_point()

        # Detecta se a plataforma L falha
        if self.ball.xcor() < -390:
            self.ball.reset_position()
            self.scoreboard.r_point()

    def check_plataform_collision(self):
        # Detecta a colisão com a plataforma
        if self.ball.distance(self.r_plat) < 73 and 340 > self.ball.xcor() >= 330 or \
                self.ball.distance(self.l_plat) < 73 and -340 < self.ball.xcor() <= -330:
            self.ball.bounce_x()


class GameBOT(Gamescreen):
    def __init__(self, color_left, color_right, color_ball):
        super().__init__(color_left, color_right, color_ball)

        self.screen.listen()
        self.screen.onkeypress(self.l_plat.go_up, "Up")
        self.screen.onkeypress(self.l_plat.go_down, "Down")

    def bot_mov(self, plat):
        if plat.ycor() != self.ball.ycor():
            plat.go_up() if plat.ycor() < self.ball.ycor() else plat.go_down()

    def run(self):
        # Run game

        d = 0  # d para o bot movimentar a peça dele

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
                self.ball.move()

                self.check_screen_collision()
                self.check_plataform_collision()

                if d >= 6:
                    self.bot_mov(self.r_plat)
                    d = 0

                d += 1

                if self.scoreboard.l_score == 5 or self.scoreboard.r_score == 5:
                    game_is_on = False
                    self.screen.clear()

                # FIM DA RENDERIZAÇÃO DO JOGO

                frames += 1
                delta -= 1

            if time.time() - timer >= 1:
                print('FPS:', frames)
                frames = 0
                timer += 1

        self.screen.bgcolor('black')
        Message(('O Computador' if self.scoreboard.r_score > self.scoreboard.l_score else 'Você') + ' venceu!!')
        time.sleep(3)

        self.screen.clear()

        return self.cor_left, self.cor_right, self.cor_bola


class Game2v2(Gamescreen):
    def __init__(self, color_left, color_right, color_ball):
        super().__init__(color_left, color_right, color_ball)

        self.screen.listen()
        self.screen.onkeypress(self.r_plat.go_up, "Up")
        self.screen.onkeypress(self.r_plat.go_down, "Down")
        self.screen.onkeypress(self.l_plat.go_up, "w")
        self.screen.onkeypress(self.l_plat.go_down, "s")

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
                self.ball.move()

                self.check_screen_collision()
                self.check_plataform_collision()

                if self.scoreboard.l_score == 5 or self.scoreboard.r_score == 5:
                    game_is_on = False
                    self.screen.clear()

                # FIM DA RENDERIZAÇÃO DO JOGO

                frames += 1
                delta -= 1

            if time.time() - timer >= 1:
                print('FPS:', frames)
                frames = 0
                timer += 1

        self.screen.bgcolor('black')
        Message(('P1' if self.scoreboard.r_score > self.scoreboard.l_score else 'P2') + ' venceu!!')
        time.sleep(3)

        self.screen.clear()

        return self.cor_left, self.cor_right, self.cor_bola


class GameINF(GameBOT):
    def __init__(self, color_left, color_right, color_ball):
        super().__init__(color_left, color_right, color_ball)

    def run(self):
        # Run game

        d = 0  # d para o bot movimentar a peça dele

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

                self.ball.move()

                self.check_screen_collision()
                self.check_plataform_collision()

                if d >= 6:
                    self.bot_mov(self.r_plat)
                    d = 0

                d += 1

                if self.scoreboard.r_score == 5:
                    game_is_on = False
                    self.screen.clear()

                # FIM DA RENDERIZAÇÃO DO JOGO

                frames += 1
                delta -= 1

            if time.time() - timer >= 1:
                print('FPS:', frames)
                frames = 0
                timer += 1

        self.screen.bgcolor('black')
        Message('Fim de jogo', pos=(0, 30))
        Message(f'Pontuação: {self.scoreboard.l_score}', pos=(0, -30))
        time.sleep(3)

        self.screen.clear()

        return self.cor_left, self.cor_right, self.cor_bola
