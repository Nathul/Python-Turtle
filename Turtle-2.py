from turtle import *
from colorsys import *

bgcolor('black')
tracer(20)
pensize(6)
h = 0.8
s=1

penup()
goto(0,0)
pendown()

for i in range(200):
    color(hsv_to_rgb(h,s,1))
    h += 0.005
    s=0.3+0.3*(i%2)
    forward(i)
    right(90)
    circle(i//5,80)
    left(90)
    circle(i//5,80)
    right(90)
    