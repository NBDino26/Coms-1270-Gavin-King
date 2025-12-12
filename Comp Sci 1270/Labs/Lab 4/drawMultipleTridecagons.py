# Gavin King    Lab 4   10-2-25
# This code will draw many tridecagons
import turtle
import math


def tridecagonTurtle(s, x, y, t):
    # Source: https://en.wikipedia.org/wiki/Tridecagon

    for y in range(13):
       t.forward(s)
       t.right(27.692)
    

def multipleTridecagon(s, x, y, nr, sr, t):
     t.exitonclick
     t.penup()
     t.setpos(x, y)
     t.pendown()

     for i in range(nr):
       tridecagonTurtle(s, x, y, t)
       t.penup()
       t.forward(sr +(s/math.sin(math.pi/13)))
       t.pendown()
    

     

def Main():
    turt = turtle
    multipleTridecagon(int(input("Input a side length: ")), int(input("Input an X Coord: ")), int(input("Input a Y Coord: ")), int(input("Input number of tridecagons: ")), int(input("Input the space between tridecagons: ")), turt)
    

if __name__ == "__main__":
    Main()

turtle.exitonclick()
