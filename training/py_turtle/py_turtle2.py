# Program to train Turtle library.

import turtle

pen = turtle.Turtle()
pen.speed(7)                    # Sets the real time drawing (0 = no delay, 1 = slow, 10 = fast).
pen.hideturtle()                # Hides the cursor of turtle.
pen.color("green")

for i in range(0, 100, 10):
    pen.forward(i)
    pen.left(90)

turtle.done()