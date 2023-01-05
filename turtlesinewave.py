import math
import turtle

win = turtle.Screen()
win.bgcolor()

# coordinate setting
win.setworldcoordinates(0, -4, 2800, 4)
t = turtle.Turtle()

# Draw a vertical line
t.goto(0, 4)
t.goto(0, -4)
t.goto(0, 0)

# Draw a Horizontal line
t.goto(2800, 0)
t.penup()
t.goto(0, 0)
t.pendown()
t.pencolor("green")
t.pensize(2)

# Generate wave form
for x in range(2800):
	y = math.sin(math.radians(x))
	t.goto(x, y)
