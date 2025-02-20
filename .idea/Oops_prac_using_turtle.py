from turtle import *
t = Turtle()
def square(t,width,color):
    t.color('Maroon')
    t.width(15)
    t.begin_fill()
    for i in range(4):
        t.forward(150)
        t.left(90)

t.end_fill()
square(t,width,color)




