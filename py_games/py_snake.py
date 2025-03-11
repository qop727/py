# Snake game.

import turtle
import time
import random

game_speed = 0.05
score = 0
highest_score = 0
segments = []                   # Snake body segments list

# Set up the screen
win = turtle.Screen()
win.title("Snake")
win.bgcolor("black")
win.setup(width=620, height=620)
win.tracer(0)                    # Turns off automatic screen updates

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# Score pen
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.shape("square")
score_pen.color("white")
score_pen.penup()
score_pen.hideturtle()
score_pen.goto(0, 250)
score_pen.write("Score: 0    Record: 0", align="center", font=("Courier", 12, "normal"))

# Functions to change direction
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

# Function to move the snake
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Keyboard bindings
win.listen()
win.onkeypress(go_up, "Up")
win.onkeypress(go_down, "Down")
win.onkeypress(go_left, "Left")
win.onkeypress(go_right, "Right")

# Main game loop
while True:
    win.update()
    
    # Check for collision with the border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        
        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        
        score = 0
        score_pen.clear()
        score_pen.write("Score: {}    Record: {}".format(score, highest_score), align="center", font=("Courier", 12, "normal"))
    
    # Check for collision with the food
    if head.distance(food) < 20:
        # Move the food to a random position
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)
        
        # Add a new segment to the snake body
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)
        
        score += 10
        if score > highest_score:
            highest_score = score
        score_pen.clear()
        score_pen.write("Score: {}    Record: {}".format(score, highest_score), align="center", font=("Courier", 12, "normal"))
    
    # Move the end segments first in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)
    
    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    
    move()
    
    # Check for collision with the snake body
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            score = 0
            score_pen.clear()
            score_pen.write("Score: {}    Record: {}".format(score, highest_score), align="center", font=("Courier", 12, "normal"))
    
    time.sleep(game_speed)