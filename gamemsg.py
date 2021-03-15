from turtle import Turtle


class Message(Turtle):

    def __init__(self, msg):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()

        self.write(msg, align="center", font=("Small Fonts", 30, "normal"))
