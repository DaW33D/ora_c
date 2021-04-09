from turtle import Turtle
from turtle import Screen
"""from j_clock import *"""
import digit
import numbers
import digit
from datetime import datetime
import time


class Time:
    # screen and turtle
    turtle = Turtle()
    turtle.hideturtle()
    turtle.speed(10)
    screen = Screen()
    screen.setup(width=600, height=400)
    n = numbers.Numbers()
    d = digit.digit()
    """clk = Clock(screen)"""

    # other turtles

    t1 = Turtle()
    t1.hideturtle()
    t1.speed(0)
    t1.fillcolor('white')

    t2 = Turtle()
    t2.hideturtle()
    t2.speed(0)
    t2.fillcolor('white')

    t3 = Turtle()
    t3.hideturtle()
    t3.speed(0)
    t3.fillcolor('white')

    t4 = Turtle()
    t4.hideturtle()
    t4.speed(0)
    t4.fillcolor('white')

    #now

    def h1(self):
        now = datetime.now()
        h1 = str(now.strftime("%H")[0:1])
        return h1

    def h2(self):
        now = datetime.now()
        h2 = str(now.strftime("%H")[1:2])
        return h2

    def m1(self):
        now = datetime.now()
        m1 = str(now.strftime("%M")[0:1])
        return m1

    def m2(self):
        now = datetime.now()
        m2 = str(now.strftime("%M")[1:2])
        return m2

    #keret

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

    #base event + idozito

    oldh1 = 10
    oldh2 = 10
    oldm1 = 10
    oldm2 = 10

    def baseEvent(self):
        m2 = self.m2()
        if m2 != self.oldm2:
            self.minute2(time=m2)
            self.oldm2 = m2


    def idozito(self):
        self.baseEvent()
        time.sleep(1)
        self.idozito()

    #writing

    def hour1(self):
        self.t1.goto(-145,  -110)

    def hour2(self):
        self.t2.goto(-25, -110)

    def minute1(self):
        self.t3.goto(145, -110)

    def minute2(self, time):
        self.n.number1(size=100, x=256, y=-110, turtle=self.t4)



    """def refreshsecond(self):
        print(self.clk.sec())"""

    def __init__(self):
        self.idozito()






Time()