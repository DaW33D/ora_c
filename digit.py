from turtle import Turtle
from turtle import Screen

class digit:
    turtle = Turtle()
    turtle.speed(0)
    screen = Screen()
    screen.setup(width=600, height=400)
    screen.bgcolor("black")

    def egyseg(self, size):
        self.turtle.fillcolor("#1aff1a")
        self.turtle.begin_fill()
        self.turtle.right(45)
        self.turtle.backward(size / 5)
        self.turtle.left(45)
        self.turtle.backward(size / 100 * 80)
        self.turtle.left(45)
        self.turtle.backward(size / 5)
        self.turtle.right(90)
        self.turtle.forward(size / 5)
        self.turtle.left(45)
        self.turtle.forward(size / 100 * 80)
        self.turtle.left(45)
        self.turtle.forward(size / 5)
        self.turtle.right(45)
        self.turtle.end_fill()

    def num8(self, size):
        self.egyseg(size=size)
        self.turtle.left(90)
        self.turtle.forward(size / 100 * 108)
        self.egyseg(size=size)
        self.turtle.left(90)
        self.turtle.forward(size / 100 * 108)
        self.egyseg(size=size)
        self.turtle.penup()
        self.turtle.backward(size / 100 * 108)
        self.turtle.right(90)
        self.turtle.pendown()
        self.turtle.forward(size / 100 * 108)
        self.egyseg(size=size)
        self.turtle.left(90)
        self.turtle.forward(size / 100 * 108)
        self.egyseg(size=size)
        self.turtle.left(90)
        self.turtle.forward(size / 100 * 108)
        self.egyseg(size=size)
        self.turtle.forward(size / 100 * 108)
        self.egyseg(size=size)
        self.turtle.right(90)
        self.turtle.forward(size / 100 * 108)

    def num1(self, size):
        self.turtle.left(90)
        self.egyseg(size=size)
        self.turtle.forward(size / 100 * 108)
        self.egyseg(size=size)
        self.turtle.forward(size / 100 * 108)

    def num2(self, size):
        self.turtle.right(90)
        self.turtle.forward(-180)
        self.turtle.forward(size / 100 * 108)
        self.egyseg(size=size)
        self.turtle.right(90)
        self.turtle.forward(size / 100 * 108)
        self.egyseg(size=size)
        self.turtle.right(90)
        self.turtle.forward(size / 100 * 108)
        self.egyseg(size=size)
        self.turtle.left(90)
        self.turtle.forward(size / 100 * 108)
        self.egyseg(size=size)
        self.turtle.left(90)
        self.turtle.forward(size / 100 * 108)
        self.egyseg(size=size)

    def num3(self, size):
        self.turtle.penup()
        self.turtle.right(180)
        self.turtle.forward(450)
        self.turtle.pendown()
        self.egyseg(size=size)
        self.turtle.right(90)
        self.turtle.forward(size / 100 * 108)
        self.egyseg(size=size)
        self.turtle.left(90)
        self.egyseg(size=size)
        self.turtle.right(360)
        self.turtle.right(270)
        self.egyseg(size=size)
        self.turtle.right(180)
        self.turtle.penup()
        self.turtle.forward(size / 100 * 108)
        self.turtle.pendown()
        self.turtle.right(270)
        self.egyseg(size=size)

    def num4(self, size):
        self.turtle.penup()
        self.turtle.right(360)
        self.turtle.forward(350)
        self.turtle.pendown()
        self.egyseg(size=size)
        self.turtle.left(90)
        self.turtle.forward(size / 100 * 108)
        self.egyseg(size=size)
        self.turtle.penup()
        self.turtle.right(180)
        self.turtle.forward(size / 100 * 216)
        self.turtle.pendown()
        self.egyseg(size=size)
        self.turtle.penup()
        self.turtle.right(180)
        self.turtle.forward(size / 100 * 108)
        self.turtle.left(90)
        self.turtle.forward(size / 100 * 108)
        self.turtle.right(90)
        self.turtle.forward(size / 100 * 108)
        self.turtle.pendown()
        self.egyseg(size=size)

    def num5(self, size):
        self.turtle.penup()
        self.turtle.forward(350)
        self.turtle.pendown()
        self.egyseg(size=size)
        self.turtle.right(90)
        self.turtle.forward(size / 100 * 108)
        self.egyseg(size=size)
        self.turtle.penup()
        self.turtle.right(180)
        self.turtle.forward(size / 100 * 108)
        self.turtle.left(90)
        self.turtle.forward(size / 100 * 108)
        self.turtle.pendown()
        self.turtle.left(90)
        self.turtle.forward(size / 100 * 108)
        self.egyseg(size=size)
        self.turtle.right(90)
        self.turtle.forward(size / 100 * 108)
        self.egyseg(size=size)
        self.turtle.right(90)
        self.turtle.forward(size / 100 * 108)
        self.egyseg(size=size)

    def num6(self, size):
        self.turtle.penup()
        self.turtle.right(180)
        self.turtle.forward(250)
        self.turtle.left(90)
        self.turtle.pendown()
        self.egyseg(size=size)
        self.turtle.right(90)
        self.turtle.forward(size / 100 * 108)
        self.egyseg(size=size)
        self.turtle.penup()
        self.turtle.right(180)
        self.turtle.forward(size / 100 * 108)
        self.turtle.left(90)
        self.turtle.forward(size / 100 * 108)
        self.turtle.pendown()
        self.turtle.left(90)
        self.turtle.forward(size / 100 * 108)
        self.egyseg(size=size)
        for i in range(3):
            self.turtle.right(90)
            self.turtle.forward(size / 100 * 108)
            self.egyseg(size=size)

    def num7(self, size):
        self.turtle.penup()
        self.turtle.forward(270)
        self.turtle.right(90)
        self.turtle.pendown()
        self.egyseg(size=size)
        self.turtle.right(90)
        for i in range(2):
            self.turtle.forward(size / 100 * 108)
            self.egyseg(size=size)

    def num9(self, size):
        self.turtle.penup()
        self.turtle.right(90)
        self.turtle.forward(1250)
        self.turtle.pendown()
        self.egyseg(size=size)
        for i in range(3):
            self.turtle.left(90)
            self.turtle.forward(size / 100 * 108)
            self.egyseg(size=size)
        self.turtle.right(180)
        self.turtle.penup()
        self.turtle.forward(size / 100 * 216)
        self.turtle.pendown()
        self.egyseg(size=size)
        self.turtle.right(90)
        self.turtle.forward(size / 100 * 108)
        self.egyseg(size=size)

    def num0(self, size):
        self.turtle.penup()
        self.turtle.right(90)
        self.turtle.forward(-120)
        self.turtle.pendown()
        self.turtle.right(90)
        self.egyseg(size=size)
        self.turtle.right(90)
        for i in range(2):
            self.turtle.forward(size / 100 * 108)
            self.egyseg(size=size)
        self.turtle.right(90)
        self.turtle.forward(size / 100 * 108)
        self.egyseg(size=size)
        self.turtle.right(90)
        for i in range(2):
            self.turtle.forward(size / 100 * 108)
            self.egyseg(size=size)





    """def __init__(self):
        self.num8()
        self.num1()
        self.num2()
        self.num3()
        self.num4()
        self.num5()
        self.num6()
        self.num7()
        self.num9()
        self.num0()

        self.screen.mainloop()"""



digit()