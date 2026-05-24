import turtle

screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()

colors = ["red","orange","yellow","green","cyan","blue","purple","pink"]

for i in range(100):
    t.pencolor(colors[i % len(colors)])
    t.forward(i * 3)
    t.right(59)

turtle.done()