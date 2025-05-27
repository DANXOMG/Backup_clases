from turtle import *

from colorsys import hsv_to_rgb


speed(0)
hideturtle()
bgcolor("black")
pensize(4)

hue = 0.0

for i in range(300):
    color = hsv_to_rgb(hue,1.0,1.0)
    pencolor(color)
    fd(i)
    rt(30*2+1)
    circle(10)
    hue += 0.005

done()