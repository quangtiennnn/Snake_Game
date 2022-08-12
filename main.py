import turtle as t
import snake
import food
import scoreboard
screen = t.Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Snake Game")
snake = snake.snake()
score_board = scoreboard.scoreboard()
screen.update()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")
food = food.food()
while snake.is_game_on():
    snake.move()
    screen.update()
    if(food.distance(snake.snake_head) <= 15):
        food.refresh()
        snake.increase_snake()
        score_board.increase_score()
    score_board.write_score()
screen.exitonclick()
