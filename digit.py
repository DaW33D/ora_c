from turtle import Turtle
from turtle import Screen

class digit:
    turtle = Turtle()
    turtle.hideturtle()
    turtle.speed(0)
    screen = Screen()
    screen.setup(width=600, height=400)
    screen.bgcolor("black")

    def egyseg(self):
        self.turtle.fillcolor("#1aff1a")
        self.turtle.begin_fill()
        self.turtle.right(45)
        self.turtle.backward(20)
        self.turtle.left(45)
        self.turtle.backward(80)
        self.turtle.left(45)
        self.turtle.backward(20)
        self.turtle.right(90)
        self.turtle.forward(20)
        self.turtle.left(45)
        self.turtle.forward(80)
        self.turtle.left(45)
        self.turtle.forward(20)
        self.turtle.right(45)
        self.turtle.end_fill()

    def num8(self):
        self.egyseg()
        self.turtle.left(90)
        self.turtle.forward(108)
        self.egyseg()
        self.turtle.left(90)
        self.turtle.forward(108)
        self.egyseg()
        self.turtle.penup()
        self.turtle.backward(108)
        self.turtle.right(90)
        self.turtle.pendown()
        self.turtle.forward(108)
        self.egyseg()
        self.turtle.left(90)
        self.turtle.forward(108)
        self.egyseg()
        self.turtle.left(90)
        self.turtle.forward(108)
        self.egyseg()
        self.turtle.forward(108)
        self.egyseg()
        self.turtle.right(90)
        self.turtle.forward(150)

    def num1(self):
        self.turtle.left(90)
        self.egyseg()
        self.turtle.forward(108)
        self.egyseg()
        self.turtle.forward(250)

    def num2(self):
        self.turtle.right(90)
        self.turtle.forward(108)
        self.egyseg()
        self.turtle.right(90)
        self.turtle.forward(108)
        self.egyseg()
        self.turtle.right(90)
        self.turtle.forward(108)
        self.egyseg()
        self.turtle.left(90)
        self.turtle.forward(108)
        self.egyseg()
        self.turtle.left(90)
        self.turtle.forward(108)
        self.egyseg()






    def __init__(self):
        self.num8()
        self.num1()
        self.num2()

        self.screen.mainloop()



digit()