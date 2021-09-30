
import turtle
import math

WIDTH = 800
HEIGHT = 600

pointer = turtle.Turtle()
screen = turtle.getscreen()
screen.setup(WIDTH, HEIGHT, 0, 0)
screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
pointer.hideturtle()
screen.delay(delay=0)

# drawing x axes
# References:
# goto https://docs.python.org/3.3/library/turtle.html?highlight=turtley#turtle.goto
# penup https://docs.python.org/3.3/library/turtle.html?highlight=turtley#turtle.penup
# pendown https://docs.python.org/3.3/library/turtle.html?highlight=turtley#turtle.pendown
X_AXES_LEFT_X = 0
X_AXES_LEFT_Y = X_AXES_RIGHT_Y = HEIGHT / 2
X_AXES_RIGHT_X = WIDTH

pointer.penup()
pointer.goto(X_AXES_LEFT_X, X_AXES_LEFT_Y)
pointer.pendown()
pointer.goto(X_AXES_RIGHT_X, X_AXES_RIGHT_Y)
pointer.penup()

# drawing y axes
Y_AXES_TOP_X = Y_AXES_BOTTOM_X = WIDTH/2
Y_AXES_TOP_Y = HEIGHT
Y_AXES_BOTTOM_Y = 0

pointer.goto(Y_AXES_TOP_X, Y_AXES_TOP_Y)
pointer.pendown()
pointer.goto(Y_AXES_BOTTOM_X, Y_AXES_BOTTOM_Y)
pointer.penup()

# getting input and converting to required type
# References:
# string to int conversion https://stackoverflow.com/questions/379906/how-do-i-parse-a-string-to-a-float-or-int
XC = int(input("Enter the Xc (integer): "))
YC = int(input("Enter the Yc (integer): "))
RADIUS = float(input("Enter the radius (float): "))
X1 = int(input("Enter X1 (integer): "))
Y1 = int(input("Enter Y1 (integer): "))
X2 = int(input("Enter X2 (integer): "))
Y2 = int(input("Enter Y2 (integer): "))

# drawing red circle

pointer.color("red")
pointer.goto(XC, YC - RADIUS)
pointer.pendown()
pointer.circle(RADIUS)
pointer.penup()

# drawing blue line

pointer.color("blue")
pointer.goto(X1, Y1)
pointer.pendown()
pointer. goto(X2, Y2)
pointer.penup()

# 3 intermediate calculations to determine intersections
A = (X2 - X1) ** 2 + (Y2 - Y1) ** 2
B = 2*((X1 - XC) * (X2 - X1) + (Y1 - YC) * (Y2 - Y1))
C = (X1 - XC) ** 2 + (Y1 - YC) ** 2 - RADIUS ** 2

# looking at value under the root to find the number of intersections
# References:
# if statements http://anh.cs.luc.edu/handsonPythonTutorial/ifstatements.html
VALUE_UNDER_ROOT = (B**2 - 4*A*C)
if VALUE_UNDER_ROOT < 0:
    # writing 'No Intersect' if there are no intersections
    # Reference:
    # write() function https://docs.python.org/3.3/library/turtle.html?highlight=turtle#turtle.write
    pointer.goto(WIDTH/2, HEIGHT/2)
    pointer.color("green")
    pointer.write("No Intersect!", True, align="center")
if VALUE_UNDER_ROOT == 0:
    print("there is one intersection")
if VALUE_UNDER_ROOT > 0:
    print("there are two intersections")

print(A)
print(B)
print(C)




screen.exitonclick()
