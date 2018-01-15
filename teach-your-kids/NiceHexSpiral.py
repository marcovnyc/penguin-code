# Create some fancy graphics

import turtle
colors = [ 'red', 'green', 'purple', 'blue',
           'white', 'yellow' ]

t=turtle.Pen()
turtle.bgcolor('black')
for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x/100+1)
    t.forward(x/2)
    t.left(59)
