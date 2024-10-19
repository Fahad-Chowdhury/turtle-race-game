from turtle import Turtle, Screen
import random


COLORS = ["red", "orange", "yellow", "blue", "purple"]
turtles = []


def create_tutles():
    """ Create turtles of different colors defined by COLORS. """
    x_coord = -230
    y_coord = -100
    for color in COLORS:
        turtle = Turtle(shape="turtle")
        turtle.color(color)
        turtle.penup()
        turtle.goto(x=x_coord, y=y_coord)
        turtles.append(turtle)
        y_coord += 50


def reached_finish_line(turtle):
    """ Retuns True if turtle reached the Finnish line, else False. """
    return turtle.xcor() > 230

def move_turtles():
    """ Move each turtle by a random steps (0 to 10), and returns the turtle,
    if it reached finish line, else False. """
    for turtle in turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(distance=random_distance)
        if reached_finish_line(turtle):
            return turtle.pencolor()
    return False


def race_turtles():
    """ Race turtles unless a turtle has reached the finish line. """
    winner = None
    while not winner:
        winner = move_turtles()
    return winner


def main():
    """ Main method for racing turtles. It sets the screen for the race, takes user bet,
    creates turtles, races turtles, checks if the user bet is correct and prints result.  """
    screen = Screen()
    screen.setup(width=500, height=400)
    msg = f"Which tuttle will win the race?\n({' or '.join(COLORS)})\nEnter a color: "
    user_bet = screen.textinput(title="Make your bet.", prompt=msg)

    create_tutles()
    winning_color = race_turtles()

    if winning_color == user_bet:
        print(f"You've won! The {winning_color} turtle is the winner!")
    else:
        print(f"You've Lost. The {winning_color} turtle is the winner!")

    screen.exitonclick()



if __name__ == "__main__":
    main()
