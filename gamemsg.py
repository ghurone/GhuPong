from turtle import Turtle


class Message(Turtle):

    def __init__(self, msg, pos=(0, 0), tam=30, tipo='normal', cor='white', alin="center"):
        super().__init__()

        self.color(cor)
        self.penup()
        self.hideturtle()
        self.goto(pos)
        self.write(msg, align=alin, font=("Small Fonts", tam, tipo))
