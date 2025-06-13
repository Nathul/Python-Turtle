import turtle as t 
import colorsys 

t.bgcolor("black")
t.tracer(10)
t.pensize(1)

h = 0.5
i = 0

while True:
    c = colorsys.hsv_to_rgb(h,1,1)  # wrap hue to [0,1]
    h += 0.008
    t.fillcolor(c)
    t.begin_fill()

    t.fd(i)
    t.lt(100)

    for j in range(2):
        t.fd(i * j)
        t.rt(109)

    t.end_fill()
    i += 1
