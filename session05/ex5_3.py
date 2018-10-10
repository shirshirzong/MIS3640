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
shir.pen (pencolor = "black", pensize = "1")
shir.speed(0)
r = 100
r2 = r/2
r3 = (r/2)/math.sqrt(3)

circle(shir,r)

shir.penup()
arc(shir, r, 30)
shir.pendown()
shir.lt (90)

shir.fd(r*2)
shir.rt(120)
shir.fd(r)
shir.rt(120)
shir.fd(r*2)
shir.lt(120)
shir.fd(r)

# another 8 shape triangle
shir.penup()
shir.lt(30)
arc(shir,r,90)
shir.lt(90)
shir.pendown()

shir.fd(r*2)
shir.rt(120) 
shir.fd(r)
shir.rt(120)
shir.fd(r*2)
shir.lt(120)
shir.fd(r)

# first circle
shir.bk(r2)
circle(shir,r3)

# second circle
shir.penup()
shir.goto(0, r+ r/2*math.sqrt(3))
shir.lt(90)
shir.pendown()
circle(shir,r3)

# third circle
shir.penup()
shir.goto(-r/2*math.sqrt(3),r)
shir.lt(90)
shir.pendown()
circle(shir,r3)

# fourth circle
shir.penup()
shir.goto(0,(r-r/2*math.sqrt(3)))
shir.lt(90)
shir.pendown()
circle(shir,r3)

turtle.mainloop()