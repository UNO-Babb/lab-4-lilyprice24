#TurtleGraphics.py
#Name:Lily Price
#Date:
#Assignment:Lab 4

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawPolygon(myTurtle, sides):
    for i in range(sides):
        myTurtle.forward(100)
        myTurtle.right(360 / sides)

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)

def fillCorner(myTurtle, corner):
    drawSquare(myTurtle, 100) 
    
    if corner == 2:
        myTurtle.forward(50)
    
    if corner == 3:
        myTurtle.right(90)
        myTurtle.forward(50)
        myTurtle.left(90)

    if corner == 4:
        myTurtle.right(90)
        myTurtle.forward(50)
        myTurtle.left(90)
        myTurtle.forward(50)

        
    myTurtle.begin_fill()
    drawSquare(myTurtle, 50)
    myTurtle.end_fill()


def squaresInSquares(myTurtle, num):
    size = 10
    for i in range(num):
        drawSquare(myTurtle, size)
        size = size + 20
        myTurtle.penup()
        myTurtle.right(180)
        myTurtle.forward(10)
        myTurtle.right(90)
        myTurtle.forward(10)
        myTurtle.right(90)
        myTurtle.pendown()




def main():
    myTurtle = turtle.Turtle()
    #drawPolygon(myTurtle, 5) #draws a pentagon
    # drawPolygon(myTurtle, 8) #draws an octogon

    #fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    #fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.

    squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    # squaresInSquares(myTurtle, 3) #draws 3 concentric squares

main()
