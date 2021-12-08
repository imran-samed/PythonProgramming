from turtle import Turtle, Screen
import time

is_race_on = True
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake game")
screen.bgcolor("black")
shape = "square"
color = "white"
start = 0

at_end = False
snakes = []
for i in range(0, 4):
    snake = Turtle(shape=shape)
    snake.goto(start, 0)
    start -= 20
    snake.color(color)
    snake.penup()
    snake.speed("slow")
    snakes.append(snake)

while not at_end:
    screen.update()
    time.sleep(0.1)
    for seg in range((len(snakes)-1), 0, -1):
        x = snakes[seg-1].xcor()
        y = snakes[seg-1].ycor()
        snakes[seg].goto(x, y)

    snakes[0].forward(10)

screen.exitonclick()
