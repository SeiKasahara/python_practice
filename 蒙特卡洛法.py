#your code here
# recommend myturtle.tracer(12,25) for faster animation
import turtle
import math
import random as r

a = turtle.Turtle()

a.color('blue')

def pink():
    color = (1,r.random(),1)
    return color

def circle():
    '''circle drawing'''
    a.penup()
    a.goto(50,0)
    a.pendown()
    a.circle(50)
    a.begin_fill()
    a.fillcolor(pink())
    a.end_fill()

b = turtle.Turtle()

b.color('red')

def square():
    '''square drawing'''
    for i in range(4):
        b.forward(100)
        b.left(90)
        b.begin_fill()
        b.fillcolor(pink())
        b.end_fill()

c = turtle.Turtle()

def blue():
    c.begin_fill()
    c.fillcolor('blue')
    c.end_fill()
    c.penup()


def red():
    c.begin_fill()
    c.fillcolor('red')
    c.end_fill()
    c.penup()


def Montecarlo(n):
    '''Points Generate'''
    points = []
    count = 0
    for i in range(n):
        raw = r.random()*100
        colomn = r.random()*100
        xy = (raw,colomn)
        points.append(xy)
        #print(xy)
        for x,y in points:
            distance = math.sqrt((x-50)**2+(y-50)**2)
        if distance <= 50: #in circle
            blue()
            c.goto(x,y)
            c.stamp()
            c.goto(x,y)
            c.up()
            count += 1
        else: #out of circle
            red()
            c.goto(x,y)
            c.stamp()
            c.goto(x,y)
            c.up()
    PI = count*4/n
    return PI

if __name__ == '__main__':
    wn = turtle.Screen()
    wn.tracer(12,25)
    wn.setworldcoordinates(0,0,100,100)
    circle()
    square()
    print("Pi approximate to:" + str(Montecarlo(2000))) 