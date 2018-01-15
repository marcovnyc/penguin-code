#Insertion Sort Algorithm - www.101computing.net/insertion-sort-algorithm/

import turtle

from random import shuffle

from time import sleep



myPen = turtle.Turtle()

myPen.tracer(0)

myPen.speed(0)

myPen.color("#000000")

myPen.hideturtle()



topLeft_x=-180

topLeft_y=160

intDim=30

gap = 40



def text(message,x,y,size):

    FONT = ('Arial', size, 'normal')

    X=myPen.xcor()

    Y=myPen.ycor()

    myPen.penup()

    myPen.goto(x,y)

    myPen.color("#000000")

    myPen.write(message,align="left",font=FONT)

    myPen.goto(X,Y)   

    myPen.pendown()



#A procedure to draw the grid on screen using Python Turtle

def drawList(list,numberOfIterations):

  global topLeft_x,topLeft_y,intDim

  myPen.penup()

  myPen.goto(topLeft_x,topLeft_y)

  myPen.pendown()



  for i in range(0,len(list)):

    #myPen.goto(topLeft_x+i*intDim,topLeft_y-intDim)

    if i<numberOfIterations:

      myPen.fillcolor("#FF00FF")

    else:

      myPen.fillcolor("#FFFFFF")

      

    myPen.begin_fill()

    for side in range(0,4):

      myPen.forward(intDim)

      myPen.left(90)

    myPen.end_fill()

      

    myPen.forward(intDim)

    text(list[i],topLeft_x+i*intDim+8,topLeft_y+5,20)



def highlightValue(list,position,color):

  global topLeft_x,topLeft_y,intDim,gap 

  myPen.penup()

  myPen.goto(topLeft_x+position*intDim,topLeft_y+gap)

  myPen.pendown()  

  myPen.fillcolor(color)

  myPen.begin_fill()

  for side in range(0,4):

    myPen.forward(intDim)

    myPen.left(90)

  myPen.forward(intDim)

  myPen.end_fill()

  myPen.end_fill()

  

  text(list[position],topLeft_x+position*intDim+8,topLeft_y+5+gap,20)    

  myPen.getscreen().update()        

  sleep(0.2)



#A function to sort a list using an insertion Sort Algorithm

def insertionSort(list):

  global topLeft_y,intDim,gap

  drawList(list,1)

  topLeft_y = topLeft_y - gap  

  myPen.getscreen().update()        

  sleep(1)

  numberOfIterations = 1



  for i in range(1, len(list)):

    highlightValue(list,i,"#FFAAFF")

    highlightValue(list,i,"#FFFFFF")

    j = i-1

    key = list[i]

    while (list[j] > key) and (j >= 0):

      highlightValue(list,j,"#CCCCCC")

      list[j+1] = list[j]

      highlightValue(list,j,"#FF00FF")

      j -= 1

    list[j+1] = key

    numberOfIterations += 1    

    drawList(list,numberOfIterations)

    topLeft_y = topLeft_y - gap

    myPen.getscreen().update()        

    sleep(0.5)

  text("Insertion Sort Complete", topLeft_x,topLeft_y+10,20)

  myPen.getscreen().update()



  

list = [1,2,3,4,5,6,7,8,9]

shuffle(list)

insertionSort(list)
