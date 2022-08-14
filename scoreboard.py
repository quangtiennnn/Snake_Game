from turtle import Turtle
class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,260)
        self.point = 0
        with open("highscore.txt","r") as data:
            self.highscore = int(data.read())
    def write_score(self):
        self.clear()
        self.write(f"Score: {self.point}    High Score : {self.highscore}",align="center",font=('Arial', 15, 'normal'))
    def reset(self):
        if self.point > self.highscore:
            self.highscore = self.point
            with open("highscore.txt","w") as data:
                # contents = data.read()
                # print(contents)
                data.write(f"{self.highscore}")
        self.point = 0


    def increase_score(self):
        self.point += 1
