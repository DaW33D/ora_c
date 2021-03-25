from turtle import Turtle
from turtle import Screen
import numbers
from datetime import datetime
import time


class Time:
    # screen and turtle
    turtle = Turtle()
    turtle.hideturtle()
    turtle.speed(0)
    screen = Screen()
    screen.setup(width=600, height=400)
    screen.bgcolor("black")

    # other turtles

    t1 = turtle
    t1.hideturtle()
    t1.speed(0)
    t1.fillcolor('white')

    t2 = turtle
    t2.hideturtle()
    t2.speed(0)
    t2.fillcolor('white')

    t3 = turtle
    t3.hideturtle()
    t3.speed(0)
    t3.fillcolor('white')

    t4 = turtle
    t4.hideturtle()
    t4.speed(0)
    t4.fillcolor('white')

    def keret(self, x, width):
        self.turtle.penup()
        self.turtle.setheading(90)
        self.turtle.goto(x, -100)
        self.turtle.pendown()
        for i in range(2):
            self.turtle.forward(220)
            self.turtle.left(90)
            self.turtle.forward(width)
            self.turtle.left(90)

    def fullkeret(self):
        self.keret(-145, width=120)
        self.keret(-25, width=120)
        self.keret(25, width=50)
        self.keret(145, width=120)
        self.keret(265, width=120)

    def hour1(self):
        self.t1.goto(-145,  -110)

    def hour2(self):
        self.t2.goto(-25, -110)

    def minute1(self):
        self.t3.goto(145, -110)

    def minute2(self):
        self.t4.goto(256, -110)

    def __init__(self):
        n = numbers.Numbers()
        self.fullkeret()
        self.hour1()
        n.number2(-25, -100, 100)
        self.screen.mainloop()


    def __init__(self):
        n = numbers.Numbers()
        self.fullkeret()
        self.hour2()
        n.number1(-25, -100, 100)
        self.screen.mainloop()


Time()