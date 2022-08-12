from turtle import Turtle
class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.point = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,260)
    def write_score(self):
        self.clear()
        self.write(f"Score: {self.point}",align="center",font=('Arial', 15, 'normal'))
    def increase_score(self):
        self.point += 1
