from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
from wall import Wall

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()
screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

on = True
while on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -296 or snake.head.ycor() > 296 or snake.head.ycor() < -296:
        on = False
        scoreboard.game_over()
    # Detect collision With Tail
    for seg in snake.segment[1:]:
        if snake.head.distance(seg) < 10:
            on = False
            scoreboard.game_over()


screen.exitonclick()
