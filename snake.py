import turtle as t
import time
STARTING_POSITION = [0, -20, -40]
STEP_LEN = 20
class snake():
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.snake_head =  self.snake_body[0]
    def create_snake(self):
        """CREATING SNAKE"""
        for location in STARTING_POSITION:
            new_snake_body = t.Turtle()
            new_snake_body.penup()
            new_snake_body.shape("square")
            new_snake_body.color("white")
            new_snake_body.goto(location,0)
            self.snake_body.append(new_snake_body)
    def move(self):
            for i in range(len(self.snake_body)-1, 0, -1):
                new_xcor = self.snake_body[i - 1].xcor()
                new_ycor = self.snake_body[i - 1].ycor()
                self.snake_body[i].goto(new_xcor, new_ycor)
            self.snake_head.forward(STEP_LEN)
            time.sleep(0.1)
    def up(self):
        if (self.snake_head.heading() == 270):
            pass
        else:
            self.snake_head.setheading(90)
    def down(self):
        if (self.snake_head.heading() == 90):
            pass
        else:
            self.snake_head.setheading(270)
    def right(self):
        if (self.snake_head.heading() == 180):
            pass
        else:
            self.snake_head.setheading(0)
    def left(self):
        if (self.snake_head.heading() == 0):
            pass
        else:
            self.snake_head.setheading(180)
    def is_game_on(self):
        game_over = t.Turtle()
        game_over.color("white")
        game_over.hideturtle()
        if self.snake_head.xcor() > 260 or self.snake_head.xcor() < -260 or self.snake_head.ycor() > 260 or self.snake_head.ycor() < -260:
            # game_over.write("Game Over!!", align="center", font=('Arial', 15, 'normal'))
            return False
        for i in range(len(self.snake_body) - 1, 0, -1):
            if self.snake_head.distance(self.snake_body[i]) <= 15:
                # game_over.write("Game Over!!", align="center", font=('Arial', 15, 'normal'))
                return False
        return True
    def increase_snake(self):
        new_snake_body = t.Turtle()
        new_snake_body.penup()
        new_snake_body.shape("square")
        new_snake_body.color("white")
        """ADD X, Y"""
        add_x = 0
        add_y = 0
        if self.snake_head.heading == 90:
            add_x = -STEP_LEN
        else:
            add_x = STEP_LEN
        if self.snake_head.heading == 0:
            add_y = -STEP_LEN
        else:
            add_y = STEP_LEN
        new_xcor = self.snake_body[len(self.snake_body)-1].xcor() + add_x
        new_ycor = self.snake_body[len(self.snake_body)-1].ycor() + add_y
        new_snake_body.goto(new_xcor,new_ycor)
        self.snake_body.append(new_snake_body)
    def reset(self):
        for i in self.snake_body:
            i.goto(1000,1000)
        self.snake_body.clear()
        self.create_snake()
        self.snake_head = self.snake_body[0]