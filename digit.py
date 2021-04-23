from turtle import Turtle
from turtle import Screen

class digit:
    turtle = Turtle()
    turtle.speed(0)
    screen = Screen()
    screen.setup(width=600, height=400)


    def egyseg(self, size, turtle):
        turtle.fillcolor("#1aff1a")
        turtle.begin_fill()
        turtle.right(45)
        turtle.backward(size / 5)
        turtle.left(45)
        turtle.backward(size / 100 * 80)
        turtle.left(45)
        turtle.backward(size / 5)
        turtle.right(90)
        turtle.forward(size / 5)
        turtle.left(45)
        turtle.forward(size / 100 * 80)
        turtle.left(45)
        turtle.forward(size / 5)
        turtle.right(45)
        turtle.end_fill()

    def goto(self, x, y, x2, y2, turtle):
        turtle.penup()
        turtle.goto(x, y)
        turtle.setheading(90)
        turtle.forward(x2)
        turtle.setheading(180)
        turtle.forward(y2)
        turtle.pendown()
        turtle.setheading(0)

    def num0(self, size, turtle, x, y):
        self.goto(x=x, y=y, x2=size / 4, y2=size * 1.30, turtle=turtle)

        turtle.setheading(180)
        self.egyseg(size=size, turtle=turtle)
        turtle.right(90)
        for i in range(2):
            turtle.forward(size / 100 * 108)
            self.egyseg(size=size, turtle=turtle)
        turtle.right(90)
        turtle.forward(size / 100 * 108)
        self.egyseg(size=size, turtle=turtle)
        turtle.right(90)
        for i in range(2):
            turtle.forward(size / 100 * 108)
            self.egyseg(size=size, turtle=turtle)

    def num1(self, size, turtle, y, x):
        self.goto(x=x, y=y, x2=size / 100 * 131.25, y2=size / 100 * 21.25, turtle=turtle)

        turtle.setheading(90)
        self.egyseg(size=size, turtle=turtle)
        turtle.forward(size / 100 * 108)
        self.egyseg(size=size, turtle=turtle)

    def num2(self, size, turtle, x, y):
        self.goto(x=x, y=y, x2=size / 4, y2=size / 100 * 21.25, turtle=turtle)

        turtle.setheading(180)
        turtle.forward(size / 100 * 108)
        self.egyseg(size=size, turtle=turtle)
        turtle.right(90)
        turtle.forward(size / 100 * 108)
        self.egyseg(size=size, turtle=turtle)
        turtle.right(90)
        turtle.forward(size / 100 * 108)
        self.egyseg(size=size, turtle=turtle)
        turtle.left(90)
        turtle.forward(size / 100 * 108)
        self.egyseg(size=size, turtle=turtle)
        turtle.left(90)
        turtle.forward(size / 100 * 108)
        self.egyseg(size=size, turtle=turtle)

    def num3(self, size, turtle, x, y):
        self.goto(x=x, y=y, x2=size / 100 * 241.25, y2=size / 100 * 21.25, turtle=turtle)

        turtle.setheading(0)
        self.egyseg(size=size, turtle=turtle)
        turtle.right(90)
        turtle.forward(size / 100 * 108)
        self.egyseg(size=size, turtle=turtle)
        turtle.left(90)
        self.egyseg(size=size, turtle=turtle)
        turtle.right(360)
        turtle.right(270)
        self.egyseg(size=size, turtle=turtle)
        turtle.right(180)
        turtle.penup()
        turtle.forward(size / 100 * 108)
        turtle.pendown()
        turtle.right(270)
        self.egyseg(size=size, turtle=turtle)

    def num4(self, size, turtle, x, y):
        self.goto(x=x, y=y, x2=size / 100 * 131.25, y2=size / 100 * 21.25, turtle=turtle)

        turtle.setheading(0)
        self.egyseg(size=size, turtle=turtle)
        turtle.left(90)
        turtle.forward(size / 100 * 108)
        self.egyseg(size=size, turtle=turtle)
        turtle.penup()
        turtle.right(180)
        turtle.forward(size / 100 * 216)
        turtle.pendown()
        self.egyseg(size=size, turtle=turtle)
        turtle.penup()
        turtle.right(180)
        turtle.forward(size / 100 * 108)
        turtle.left(90)
        turtle.forward(size / 100 * 108)
        turtle.right(90)
        turtle.forward(size / 100 * 108)
        turtle.pendown()
        self.egyseg(size=size, turtle=turtle)

    def num5(self, size, turtle, x, y):
        self.goto(x=x, y=y, x2=size / 100 * 241.25, y2=size / 100 * 128.75, turtle=turtle)

        turtle.setheading(90)
        self.egyseg(size=size, turtle=turtle)
        turtle.right(90)
        turtle.forward(size / 100 * 108)
        self.egyseg(size=size, turtle=turtle)
        turtle.penup()
        turtle.right(180)
        turtle.forward(size / 100 * 108)
        turtle.left(90)
        turtle.forward(size / 100 * 108)
        turtle.pendown()
        turtle.left(90)
        turtle.forward(size / 100 * 108)
        self.egyseg(size=size, turtle=turtle)
        turtle.right(90)
        turtle.forward(size / 100 * 108)
        self.egyseg(size=size, turtle=turtle)
        turtle.right(90)
        turtle.forward(size / 100 * 108)
        self.egyseg(size=size, turtle=turtle)

    def num6(self, size, turtle, x, y):
        self.goto(x=x, y=y, x2=size / 100 * 241.25, y2=size / 100 * 128.75, turtle=turtle)

        turtle.setheading(90)
        self.egyseg(size=size, turtle=turtle)
        turtle.right(90)
        turtle.forward(size / 100 * 108)
        self.egyseg(size=size, turtle=turtle)
        turtle.penup()
        turtle.right(180)
        turtle.forward(size / 100 * 108)
        turtle.left(90)
        turtle.forward(size / 100 * 108)
        turtle.pendown()
        turtle.left(90)
        turtle.forward(size / 100 * 108)
        self.egyseg(size=size, turtle=turtle)
        for i in range(3):
            turtle.right(90)
            turtle.forward(size / 100 * 108)
            self.egyseg(size=size, turtle=turtle)

    def num7(self, size, turtle, x, y):
        self.goto(x=x, y=y, x2=size / 100 * 241.25, y2=size / 100 * 21.25, turtle=turtle)

        turtle.setheading(0)
        self.egyseg(size=size, turtle=turtle)
        turtle.right(90)
        for i in range(2):
            turtle.forward(size / 100 * 108)
            self.egyseg(size=size, turtle=turtle)

    def num8(self, size, turtle, x, y):
        self.goto(x=x, y=y, x2=size / 4, y2=size / 100 * 21.25, turtle=turtle)

        self.egyseg(size=size, turtle=turtle)
        turtle.left(90)
        turtle.forward(size / 100 * 108)
        self.egyseg(size=size, turtle=turtle)
        turtle.left(90)
        turtle.forward(size / 100 * 108)
        self.egyseg(size=size, turtle=turtle)
        turtle.penup()
        turtle.backward(size / 100 * 108)
        turtle.right(90)
        turtle.pendown()
        turtle.forward(size / 100 * 108)
        self.egyseg(size=size, turtle=turtle)
        turtle.left(90)
        turtle.forward(size / 100 * 108)
        self.egyseg(size=size, turtle=turtle)
        turtle.left(90)
        turtle.forward(size / 100 * 108)
        self.egyseg(size=size, turtle=turtle)
        turtle.forward(size / 100 * 108)
        self.egyseg(size=size, turtle=turtle)



    def num9(self, size, turtle, x, y):
        self.goto(x=x, y=y, x2=size / 100 * 241.25, y2=size / 100 * 128.75, turtle=turtle)

        turtle.setheading(180)
        self.egyseg(size=size, turtle=turtle)
        for i in range(3):
            turtle.left(90)
            turtle.forward(size / 100 * 108)
            self.egyseg(size=size, turtle=turtle)
        turtle.right(180)
        turtle.penup()
        turtle.forward(size / 100 * 216)
        turtle.pendown()
        self.egyseg(size=size, turtle=turtle)
        turtle.right(90)
        turtle.forward(size / 100 * 108)
        self.egyseg(size=size, turtle=turtle)

    def pont(self, turtle, x, y):
        self.goto(turtle=turtle, x=x, y=y, x2=60, y2=25)

        turtle.pencolor("#1aff1a")
        turtle.setheading(90)
        turtle.dot(size=20)
        turtle.penup()
        turtle.forward(80)
        turtle.pendown()
        turtle.dot(size=20)



        """turtle.penup
        turtle.left(90)
        turtle.forward(20)
        turtle.right(180)
        turtle.pendown()
        self.egyseg(size=size,turtle=turtle)
        turtle.penup()
        turtle.forward(40)
        turtle.right(180)
        turtle.pendown()
        self.egyseg(size=size,turtle=turtle)"""








