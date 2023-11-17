from turtle import Turtle


class Wall(Turtle):
    def __init__(self):
        super().__init__()

        self.speed(0)
        self.penup()
        self.goto(-280,280)
        self.pendown()
        self.color("white")
        self.shape("square")
        self.goto(280,280)
        self.goto(280,-280)
        self.goto(-280,-280)
        self.goto(-280,280)