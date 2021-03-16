from plat import Plat
from ball import Ball
from scoreboard import Scoreboard
from gamemsg import Message

import turtle
import time


def check_screen_collision():

    # Detecta colisão com a parede de cima
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    # Detecta se a plataforma R falha
    if ball.xcor() > 390:
        ball.reset_position()
        scoreboard.l_point()

    # Detecta se a plataforma L falha
    if ball.xcor() < -390:
        ball.reset_position()
        scoreboard.r_point()


def check_plataform_collision():
    # Detecta a colisão com a plataforma
    if ball.distance(r_plat) < 72.8 and 340 > ball.xcor() >= 330 or \
         ball.distance(l_plat) < 72.8 and - 340 < ball.xcor() <= -330:
        ball.bounce_x()


def bot_mov(plat):
    if plat.ycor() != ball.ycor():
        plat.go_up() if plat.ycor() < ball.ycor() else plat.go_down()


if __name__ == '__main__':

    # Iniciar a Tela

    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.setup(width=800, height=600)
    screen.title("GhuPong")
    screen.tracer(0)

    # Inserir os widgets na tela

    r_plat = Plat((350, 0))
    l_plat = Plat((-350, 0))
    ball = Ball()
    scoreboard = Scoreboard()

    # Traço no meio da tela

    trace = turtle.Turtle()
    trace.shape('square')
    trace.color('white')
    trace.shapesize(stretch_wid=30, stretch_len=0.2)
    trace.penup()

    # Bind das teclas

    screen.listen()
    screen.onkeypress(l_plat.go_up, "Up")
    screen.onkeypress(l_plat.go_down, "Down")

    # Run game

    d = 0  # d para o bot movimentar a peça dele

    # Sistema de FPS

    last_time = time.time()
    amountTicks = 60
    ns = 1 / amountTicks
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

            screen.update()
            ball.move()

            check_screen_collision()
            check_plataform_collision()

            if d >= 0.6:
                bot_mov(r_plat)
                d = 0

            if scoreboard.l_score == 5 or scoreboard.r_score == 5:
                game_is_on = False
                screen.clear()
                screen.bgcolor('black')
                msg = ('O Computador' if scoreboard.r_score > scoreboard.l_score else 'Você') + ' venceu!!'
                Message(msg)

            d += 0.1

            # FIM DA RENDERIZAÇÃO DO JOGO

            frames += 1
            delta -= 1

        if time.time() - timer >= 1:
            print('FPS:', frames)
            frames = 0
            timer += 1

    screen.exitonclick()
