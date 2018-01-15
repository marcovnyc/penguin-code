import turtle

painter = turtle.Turtle()

painter.color('blue')

for i in range(50):
    painter.forward(50)
    painter.left(123) # Let's go counter clockwise

painter.color('red')
for i in range(50):
    painter.forward(100)
    painter.left(123)

turtle.done()
