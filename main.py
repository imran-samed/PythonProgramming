import turtle
from turtle import Turtle, Screen
import random

is_race_on = True
screen = Screen()
screen.setup(width=500, height=500)
user_bet = screen.textinput("Let's bet", "Which color turtle will win ?")

colors = ["red", "green", "yellow", "blue", "purple", "green"]
all_turtle = []

init_point = - 175
for c in range(0, len(colors)):
    t = Turtle(shape="turtle")
    t.penup()
    t.color(colors[c])
    init_point = init_point + 50
    t.goto(-230, init_point)
    all_turtle.append(t)

if user_bet:
    is_race_on = True

while is_race_on:
    for t in all_turtle:
        if t.xcor() > 230:
            is_race_on = False
            if t.pencolor() == user_bet:
                print(f"You've won. The wining turtle color is {t.pencolor()}")
            else:
                print(f"You've lost. The wining turtle color is {t.pencolor()}")

        move_by = random.randint(0, 10)
        t.forward(move_by)

screen.exitonclick()
