import turtle
import math
# a square
# def square(t, length):
#     for i in range (4):
#         t.fd(length)
#         t.lt(90)

# jack = turtle.Turtle()

# square(jack,100)

# turtle.mainloop()

# a polygon

# def polygon(t, length,n):
#     for i in range (n):
#         t.fd(length)
#         t.lt(360/n)

# jack = turtle.Turtle()

# polygon(jack,100,6)

# turtle.mainloop()

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
    arc(t, r, 360)

jack = turtle.Turtle()

arc(jack,100,120)

turtle.mainloop()