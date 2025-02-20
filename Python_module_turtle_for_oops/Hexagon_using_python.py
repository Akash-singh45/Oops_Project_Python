from turtle import *

pen = Turtle()

colors = ["red","blue","lime green","purple","orange","maroon"]

def hexagon(pen,color,width):
    pen.width(50)
    for i in range(6):
        pen.color(colors[i])
        pen.forward(200)
        pen.left(60)
hexagon(pen,color,width)

