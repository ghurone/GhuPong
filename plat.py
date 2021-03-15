from turtle import Turtle


class Plat(Turtle):
    
    def __init__(self, position, color='white'):
        super().__init__()

        self.shape('square')
        self.color(color)
        self.shapesize(stretch_wid=6, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        if self.ycor() < 240:
            new_y = self.ycor() + 30
            self.goto(self.xcor(), new_y)

    def go_down(self):
        if self.ycor() > -240:
            new_y = self.ycor() - 30
            self.goto(self.xcor(), new_y)
