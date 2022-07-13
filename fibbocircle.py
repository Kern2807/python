import turtle

colors = ["Green"]
a = turtle.Turtle()

for i in range(100):
    a.forward(20+i)
    a.left(30 - i/1.5)
    a.color(colors[0])

turtle.done()
