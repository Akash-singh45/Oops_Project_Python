from turtle import *

def star(t,width,color,size):
    t.color(color)
    t.width(width)
    t.begin_fill()
    for i in range(5):
        t.forward(size)
        t.left(144)
    t.end_fill()


def circle(t,color,radius):
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

t =Turtle()
ask =input('enter the shape: ')
while ask != 'done':
    if ask == 'star':
        width = int(input("enter the width: "))
        col = input("enter the color: ")
        size = int(input("enter the size: "))
        star(t,width,col,size)
    elif ask == 'circle':
        rad = int(input("enter the radius: "))
        col = input("enter the color: ")
        circle(t,col,rad)

    else:
        print("No valid shape entered: ")
    ask = input("enter the shape: ")
done()















