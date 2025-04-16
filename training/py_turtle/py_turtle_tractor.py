# Program to draw tractor.

import turtle

pen = turtle.Turtle()       # Creates instance of Turtle class.
pen.hideturtle()
pen.circle(100)             # Draws the big wheel.

pen.penup()                 # Lifts the pen, so it does not draw while moving the pen.
pen.goto(0, 50)           # Moves the turtle to different possition withoout drawing.

pen.pendown()               # Puts the pen down, so it can start to draw with movement.
pen.circle(50)

pen.penup()
pen.goto(-80, 40)

pen.pendown()
pen.goto(-150, 40)

pen.penup()
pen.goto(-190, 0)

pen.pendown()
pen.circle(40)              # Small wheel.

pen.penup()
pen.goto(-190, 20)

pen.pendown()
pen.circle(20)

pen.penup()
pen.goto(-190, 80)

pen.pendown()
pen.left(90)
pen.forward(50)
pen.right(90)
pen.forward(70)
pen.left(90)                # Exhaust.
pen.forward(60)
pen.right(90)
pen.forward(10)
pen.right(90)
pen.forward(60)
pen.right(90)
pen.forward(10)
pen.backward(25)
pen.right(90)               # Cabin
pen.forward(70)
pen.right(90)
pen.forward(130)
pen.left(90)
pen.forward(70)
pen.left(90)
pen.forward(130)
pen.right(90)
pen.backward(100)
pen.forward(110)
pen.right(90)
pen.forward(160)
pen.right(90)
pen.forward(105)

turtle.done()