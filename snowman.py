#create a snowman with a hat, a face, and arms, in turtle graphics
import turtle
import math
import random

#draw a circle of radius r at position (x,y)
def circle(x,y,r):
    turtle.penup()
    turtle.goto(x,y-r)
    turtle.pendown()
    turtle.circle(r)

#draw a rectangle of width w and height h at position (x,y)
def rectangle(x,y,w,h):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.setheading(0)
    turtle.forward(w)
    turtle.left(90)
    turtle.forward(h)
    turtle.left(90)
    turtle.forward(w)
    turtle.left(90)
    turtle.forward(h)

#draw a triangle of side length s at position (x,y)
def triangle(x,y,s):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.setheading(0)
    turtle.forward(s)
    turtle.left(120)
    turtle.forward(s)
    turtle.left(120)
    turtle.forward(s)

#draw a snowman with a hat, a face, and arms, at position (x,y)
def snowman(x,y):
    #draw the body
    circle(x,y,50)
    circle(x,y+100,40)
    circle(x,y+180,30)

    #draw the hat
    turtle.penup()
    turtle.goto(x-20,y+210)
    turtle.pendown()
    turtle.setheading(0)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(20)

    #draw the eyes
    turtle.penup()
    turtle.goto(x-10,y+170)
    turtle.pendown()
    turtle.dot(10)
    turtle.penup()
    turtle.goto(x+10,y+170)
    turtle.pendown()
    turtle.dot(10)

    #draw the nose
    turtle.penup()
    turtle.goto(x,y+160)
    turtle.pendown()
    turtle.setheading(0)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(10)

    #draw the mouth
    turtle.penup()
    turtle.goto(x-10,y+140)
    turtle.pendown()
    turtle.setheading(0)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(10)

    #draw the arms
    turtle.penup()
    turtle.goto(x-40,y+120)
    turtle.pendown()
    turtle.setheading(0)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(20)

    turtle.penup()
    turtle.goto(x+40,y+120)
    turtle.pendown()
    turtle.setheading(0)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(20)

    #keep the window open
    turtle.done()

    