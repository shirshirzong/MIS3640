import turtle
import math

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    
    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t, n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)

def circle(t, r):
    arc(t, r, angle = 360)

shir = turtle.Turtle()
shir.pen (pencolor = "black", pensize = "3")
shir.speed(0)
r = 100
r2 = r/2
r3 = r/6

arc (shir, r2 , angle = 180)
arc (shir, r , angle = 180)
shir.penup()
arc (shir, r2 , angle = 180)
shir.pendown()
arc (shir, r2 , angle = 180)

arc (shir, r, angle = 180)

shir.penup()
shir.fd(r3)
shir.lt(90)
shir.fd (r2)
shir.pendown()

circle (shir, r3)

shir.penup()
shir.fd(r)
shir.pendown()

circle (shir, r3)

turtle.mainloop()