from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=500, height=400)
user_guess = screen.textinput(
    title="Bet on: ", prompt="Enter the color of the turtle to bet: ")

turtle_list = []
colours = ['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']
for i in colours:
    tur = Turtle(shape="turtle")
    tur.color(i)
    turtle_list.append(tur)

y = 90
for t in turtle_list:
    t.penup()
    t.goto(x=-230, y=y)
    y -= 30

gameOn = False

if user_guess:
    gameOn = True

while gameOn:
    for par in turtle_list:
        par.speed("fastest")
        par.forward(randint(0, 10))
        if par.xcor() > 230:
            win_col = par.pencolor()
            gameOn = False

if win_col == user_guess:
    print("You win")

else:
    print(f"You lose and the winner is {win_col}")


screen.exitonclick()
