# Ping Pong game.

import turtle
import time

game_speed = 0.008
score_a = 0
score_b = 0

# Screen setting.
win = turtle.Screen()
win.title("PingPong")
win.bgcolor("gray")
win.setup(width=1000, height=800)
win.tracer(0)                        # Turns off automatic screen updates

# Top guardrail.
t_guardrail = turtle.Turtle()
t_guardrail.speed(0)
t_guardrail.shape("square")
t_guardrail.color("green")
t_guardrail.shapesize(stretch_wid=1,stretch_len=50)
t_guardrail.penup()
t_guardrail.goto(0, 310)

# Bot guardrail.
b_guardrail = turtle.Turtle()
b_guardrail.speed(0)
b_guardrail.shape("square")
b_guardrail.color("green")
b_guardrail.shapesize(stretch_wid=1,stretch_len=50)
b_guardrail.penup()
b_guardrail.goto(0, -310)

# Paddle A.
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("blue")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B.
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("purple")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball.
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

# Score pen Player A.
score_pen_a = turtle.Turtle()
score_pen_a.speed(0)
score_pen_a.shape("square")
score_pen_a.color("blue")
score_pen_a.penup()
score_pen_a.hideturtle()
score_pen_a.goto(-250, 320)
score_pen_a.write(" Player A: 0", align="center", font=("Courier", 24, "normal"))

# Score pen Player B.
score_pen_b = turtle.Turtle()
score_pen_b.speed(0)
score_pen_b.shape("square")
score_pen_b.color("purple")
score_pen_b.penup()
score_pen_b.hideturtle()
score_pen_b.goto(250, 320)
score_pen_b.write("Player B: 0 ", align="center", font=("Courier", 24, "normal"))

# Functions for paddle movement.
def paddle_a_up():
    y = paddle_a.ycor()
    y += 30
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 30
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 30
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 30
    paddle_b.sety(y)

# Keyboard bindings.
win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")

# Main game loop.
while True:
    win.update()
    
    # Move the ball.
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Top and bottom border checking.
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # Left and right border checking.
    if ball.xcor() > 350:
        score_a += 1
        score_pen_a.clear()
        score_pen_a.write("Player B: {}".format(score_a), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1
    elif ball.xcor() < -350:
        score_b += 1
        score_pen_b.clear()
        score_pen_b.write("Player A: {}".format(score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    # Paddle and ball collisions.
    if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.dx *= -1 
    elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.dx *= -1
    
    time.sleep(game_speed)