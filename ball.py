from turtle import Turtle
from random import uniform, randint


class Ball(Turtle):

    def __init__(self, color='white'):
        super().__init__()
        self.color(color)
        self.shape("square")
        self.penup()
        self.x_move = uniform(4, 6)
        self.y_move = uniform(4, 6)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1 * uniform(1, 1.05)

    def bounce_x(self):
        self.x_move *= -1 * uniform(1, 1.05)

    def reset_position(self):
        self.goto(0, 0)

        self.x_move = uniform(4, 6) if self.x_move < 0 else -uniform(4, 6)
        self.y_move = uniform(4, 6) if randint(1, 2) == 2 else -uniform(4, 6)

    def move_at_menu(self):
        self.move()

        # Detecta colisão com a parede de cima
        if self.ycor() > 290 or self.ycor() < -290:
            self.bounce_y()

        # Detecta se a plataforma R falha
        if self.xcor() > 390 or self.xcor() < -390:
            self.bounce_x()



