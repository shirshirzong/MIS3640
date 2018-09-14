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
shir.speed(0)

circle(shir, r = 100)
shir.lt(angle = 60)

for i in range(3):
    arc(shir, r= 100, angle= 120)
    shir.lt(angle = 120)


shir.rt(angle = 60)
shir.penup()
arc(shir, r= 100, angle = 60)
shir.pendown()
shir.lt(angle = 60)

for i in range(3):
    arc(shir, r = 100, angle = 120)
    shir.lt(angle = 120)

turtle.mainloop()