import turtle

turtle.Screen().bgcolor("cyan")

t = turtle.Turtle()

for i in range(3):
    t.forward(100)
    t.left(120)

t.penup()
t.goto(150, 0)
t.pendown()

for i in range(2):
    t.forward(100)
    t.left(90)
    t.forward(50)
    t.left(90)

t.penup()
t.goto(-150, 0)
t.pendown()

for i in range(6):
    t.forward(50)
    t.left(60)

turtle.done()