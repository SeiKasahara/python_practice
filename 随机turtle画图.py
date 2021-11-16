import turtle
import random as r

t = turtle.Turtle()

def control():
    if r.random() > 0.9:
        return True
    return False

while control():
    if r.random() > 0.5:
        t.forward(10)
        t.left(90)
        continue
    else:
        t.forward(10)
        t.right(90)
    break