from turtle import Turtle
from random import uniform


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.x_move = 6
        self.y_move = 6

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1 * uniform(1, 1.2)

    def bounce_x(self):
        self.x_move *= -1 * uniform(1.1, 1.2)
        self.y_move *= 1.1 * uniform(1.1, 1.2)

    def reset_position(self):
        self.goto(0, 0)
        self.x_move *= -1
        self.x_move = 6
        self.y_move = 6




