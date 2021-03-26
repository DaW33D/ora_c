from turtle import Turtle


class Numbers:

    def goto(self, x, y, x2, y2, turtle):
        turtle.penup()
        turtle.goto(x, y)
        turtle.setheading(90)
        turtle.forward(x2)
        turtle.setheading(180)
        turtle.forward(y2)
        turtle.pendown()
        turtle.setheading(0)

    def number0(self, x, y, size, turtle):
        self.goto(x, y, x2=60, y2=10, turtle=turtle)

        turtle.setheading(270)
        for i in range(2):
            turtle.circle(-size / 2, 180)
            turtle.forward(size)

    def number1(self, x, y, size, turtle):
        self.goto(x, y, x2=10, y2=40, turtle=turtle)

        turtle.setheading(90)
        turtle.forward(size * 2)
        turtle.left(135)
        turtle.forward(size * 0.8)

    def number2(self, x, y, size, turtle):
        self.goto(x, y, x2=15, y2=10, turtle=turtle)

        turtle.setheading(180)
        turtle.forward(size)
        turtle.setheading(50)
        turtle.forward(size * 1.4)
        turtle.circle(size / 2, 220)

    def number3(self, x, y, size, turtle):
        self.goto(x, y, x2=60, y2=110, turtle=turtle)

        turtle.setheading(270)
        turtle.circle(size / 2, 270)
        turtle.setheading(0)
        turtle.circle(size / 2, 270)

    def number4(self, x, y, size, turtle):
        self.goto(x, y, x2=30, y2=40, turtle=turtle)

        turtle.setheading(90)
        turtle.forward(size * 1.6)
        turtle.setheading(240)
        turtle.forward(size * 1.3)
        turtle.setheading(0)
        turtle.forward(size * 0.85)

    def number5(self, x, y, size, turtle):
        """self.goto(x, y, x2=75, y2=110, turtle=turtle)"""

        turtle.setheading(270)
        turtle.circle(size / 2, 180)
        turtle.circle(size / 1.9, 150)
        turtle.setheading(90)
        turtle.forward(size * 0.9)
        turtle.setheading(0)
        turtle.forward(size)

    def number6(self, x, y, size, turtle):
        self.goto(x, y, x2=60, y2=10, turtle=turtle)

        turtle.setheading(270)
        for i in range(2):
            turtle.circle(-size / 2, 180)
            turtle.forward(size / 5)
        turtle.circle(-size / 2, 180)
        turtle.setheading(90)
        turtle.forward(size)
        turtle.circle(-size / 2, 180)

    def number7(self, x, y, size, turtle):
        self.goto(x, y, x2=10, y2=62.5, turtle=turtle)

        turtle.setheading(75)
        turtle.forward(size * 2)
        turtle.setheading(180)
        turtle.forward(size)

    def number8(self, x, y, size, turtle):
        self.goto(x, y, x2=120, y2=60, turtle=turtle)

        turtle.circle(size / -2, 360)
        turtle.circle(size * 0.4, 360)

    def number9(self, x, y, size, turtle):
        self.goto(x, y, x2=160, y2=110, turtle=turtle)

        turtle.setheading(90)
        for i in range(2):
            turtle.circle(size / -2, 180)
            turtle.forward(size / 5)
        turtle.circle(size / -2, 180)
        turtle.setheading(270)
        turtle.forward(size)
        turtle.circle(size / -2, 180)

