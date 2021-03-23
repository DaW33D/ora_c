from turtle import Turtle


class Numbers:
    turtle = Turtle()
    turtle.hideturtle()
    turtle.speed(0)
    turtle.pensize(10)

    def goto(self, x, y, x2, y2):
        self.turtle.penup()
        self.turtle.goto(x, y)
        self.turtle.setheading(90)
        self.turtle.forward(x2)
        self.turtle.setheading(180)
        self.turtle.forward(y2)
        self.turtle.pendown()
        self.turtle.setheading(0)

    def number0(self, x, y, size):
        self.goto(x, y, 60, 10)

        self.turtle.setheading(270)
        for i in range(2):
            self.turtle.circle(-size / 2, 180)
            self.turtle.forward(size)

    def number1(self, x, y, size):
        self.goto(x, y, 10, 40)

        self.turtle.setheading(90)
        self.turtle.forward(size * 2)
        self.turtle.left(135)
        self.turtle.forward(size * 0.8)

    def number2(self, x, y, size):
        self.goto(x, y, 15, 10)

        self.turtle.setheading(180)
        self.turtle.forward(size)
        self.turtle.setheading(50)
        self.turtle.forward(size * 1.4)
        self.turtle.circle(size / 2, 220)

    def number3(self, x, y, size):
        self.goto(x, y, 60, 110)

        self.turtle.setheading(270)
        self.turtle.circle(size / 2, 270)
        self.turtle.setheading(0)
        self.turtle.circle(size / 2, 270)

    def number4(self, x, y, size):
        self.goto(x, y, 30, 40)

        self.turtle.setheading(90)
        self.turtle.forward(size * 1.6)
        self.turtle.setheading(240)
        self.turtle.forward(size * 1.3)
        self.turtle.setheading(0)
        self.turtle.forward(size * 0.85)

    def number5(self, x, y, size):
        self.goto(x, y, 75, 110)

        self.turtle.setheading(270)
        self.turtle.circle(size / 2, 325)
        self.turtle.goto(x, y + size * 0.285)
        self.turtle.setheading(90)
        self.turtle.forward(size * 0.9)
        self.turtle.setheading(0)
        self.turtle.forward(size)

    def number6(self, x, y, size):
        self.goto(x, y, 60, 10)

        self.turtle.setheading(270)
        for i in range(2):
            self.turtle.circle(-size / 2, 180)
            self.turtle.forward(size / 5)
        self.turtle.circle(-size / 2, 180)
        self.turtle.setheading(90)
        self.turtle.forward(size)
        self.turtle.circle(-size / 2, 180)

    def number7(self, x, y, size):
        self.goto(x, y, 10, 62.5)

        self.turtle.setheading(75)
        self.turtle.forward(size * 2)
        self.turtle.setheading(180)
        self.turtle.forward(size)

    def number8(self, x, y, size):
        self.goto(x, y, 120, 60)

        self.turtle.circle(size / -2, 360)
        self.turtle.circle(size * 0.4, 360)

    def number9(self, x, y, size):
        self.goto(x, y, 160, 110)

        self.turtle.setheading(90)
        for i in range(2):
            self.turtle.circle(size / -2, 180)
            self.turtle.forward(size / 5)
        self.turtle.circle(size / -2, 180)
        self.turtle.setheading(270)
        self.turtle.forward(size)
        self.turtle.circle(size / -2, 180)
