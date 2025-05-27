from turtle import *

import colorsys

speed(0)
hideturtle()
bgcolor("black")
pensize(4)

hue = 0.0

for i in range(300):
    color = colorsys.hsv_to_rgb(hue,1,1)
    pencolor(color)
    fd(i)
    rt(30*2+1)
    circle(10)
    hue += 0.0005
    
done()
