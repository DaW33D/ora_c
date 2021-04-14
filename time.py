from turtle import Turtle
from turtle import Screen
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
    screen.setup(width=1920, height=1080)
    n = numbers.Numbers()
    d = digit.digit()

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
        h1 = int(h1)
        return h1

    def h2(self):
        now = datetime.now()
        h2 = str(now.strftime("%H")[1:2])
        h2 = int(h2)
        return h2

    def m1(self):
        now = datetime.now()
        m1 = str(now.strftime("%M")[0:1])
        m1 = int(m1)
        return m1

    def m2(self):
        now = datetime.now()
        m2 = str(now.strftime("%M")[1:2])
        m2 = int(m2)
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

    #numbers

    def selector(self, number, size, turtle, x, y):
        if number == 0:
            self.n.number0(size=size, turtle=turtle, x=x, y=y)
        if number == 1:
            self.n.number1(size=size, turtle=turtle, x=x, y=y)
        if number == 2:
            self.n.number2(size=size, turtle=turtle, x=x, y=y)
        if number == 3:
            self.n.number3(size=size, turtle=turtle, x=x, y=y)
        if number == 4:
            self.n.number4(size=size, turtle=turtle, x=x, y=y)
        if number == 5:
            self.n.number5(size=size, turtle=turtle, x=x, y=y)
        if number == 6:
            self.n.number6(size=size, turtle=turtle, x=x, y=y)
        if number == 7:
            self.n.number7(size=size, turtle=turtle, x=x, y=y)
        if number == 8:
            self.n.number8(size=size, turtle=turtle, x=x, y=y)
        if number == 9:
            self.n.number9(size=size, turtle=turtle, x=x, y=y)

    def digitSelector(self, number, size, turtle):
        if number == 0:
            self.d.num0(size=size, turtle=turtle)
        if number == 1:
            self.d.num1(size=size, turtle=turtle)
        if number == 2:
            self.d.num2(size=size, turtle=turtle)
        if number == 3:
            self.d.num3(size=size, turtle=turtle)
        if number == 4:
            self.d.num4(size=size, turtle=turtle)
        if number == 5:
            self.d.num5(size=size, turtle=turtle)
        if number == 6:
            self.d.num6(size=size, turtle=turtle)
        if number == 7:
            self.d.num7(size=size, turtle=turtle)
        if number == 8:
            self.d.num8(size=size, turtle=turtle)
        if number == 9:
            self.d.num9(size=size, turtle=turtle)



    #base event + idozito

    oldh1 = 10
    oldh2 = 10
    oldm1 = 10
    oldm2 = 10

    def baseEvent(self):
        m2 = self.m2()
        if m2 != self.oldm2:
            self.minute2(ido=m2)
            print('minute2 changed')
            self.oldm2 = m2
        m1 = self.m1()
        if m1 != self.oldm1:
            self.minute1(ido=m1)
            print('minute1 changed')
            self.oldm1 = m1
        h1 = self.h1()
        if h1 != self.oldh1:
            self.hour1(ido=h1)
            print('hour1 changed')
            self.oldh1 = h1
        h2 = self.h2()
        if h2 != self.oldh2:
            self.hour2(ido=h2)
            print('hour2 changed')
            self.oldh2 = h2

    def idozito(self):
        self.baseEvent()
        time.sleep(0.5)
        self.idozito()

    #writing

    def hour1(self, ido):
        self.t1.clear()
        self.selector(number=ido, size=100, turtle=self.t1, x=-145, y=-100)

    def hour2(self, ido):
        self.t2.clear()
        self.selector(number=ido, size=100, turtle=self.t2, x=-25, y=-100)

    def minute1(self, ido):
        self.t3.clear()
        self.selector(number=ido, size=100, turtle=self.t3, x=145, y=-100)

    def minute2(self, ido):
        self.t4.goto(x=265, y=-100)
        self.t4.clear()
        """self.selector(number=ido, size=100, turtle=self.t4, x=265, y=-100)"""
        self.digitSelector(number=9, size=100, turtle=self.t4)

    #init

    def __init__(self):
        """self.fullkeret()"""
        self.idozito()


Time()