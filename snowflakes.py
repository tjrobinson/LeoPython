import random
from turtle import *
shape("turtle")
speed(10)
pencolor("white")
pensize(6)
Screen().bgcolor("turquoise")
def vshape(size):
    right(25)
    forward(size)
    backward(size)
    left(50)
    forward(size)
    backward(size)
    right(25)
def snowflakearm(size):
    for x in range(0,4):
        forward(size)
        vshape(size)
    backward(size*4)
def snowflake(size):
    for x in range(0,6):
        snowflakearm(size)
        right(60)
for i in range(0,10):
    size = random.randint(5,30)
    x = random.randint(-400,400)
    y = random.randint(-400,400)
    penup()
    goto(x,y)
    pendown()
    snowflake(size)
hideturtle()
