# CPSC 231, Sergey Chitsvarin, tutorial 2, 30154758,09/30/2021
#
# 1) To run my program in the terminal
# open terminal and open the folder containing this file
# run this command in the terminal: python .\CPSC231F21A1-Chitsvarin.py
# 2) to run my program in PyCharm
# open file in PyCharm and do right-click within the file then click run
#
# this program asks the user for input and uses this input to draw a circle and a line,
# if circle and line intersect the program shows the intersection point(s)
# if they do not intercept the program says 'no intercepts!'

import turtle
import math

WIDTH = 800
HEIGHT = 600

# the function takes the alpha as an argument
# it uses alpha to find intercept
# and draws a green circle around the intercept
# References:
# function declaration with arguments https://www.w3schools.com/python/python_functions.asp
def draw_intercept(alpha):
    # this assures that an intersection does not occur outside of the end points of the line segment
    if  alpha >= 0 and alpha <= 1:
        intercept_x = (1-alpha)*X1+(alpha*X2)
        intercept_y = (1-alpha)*Y1+(alpha*Y2)
        intercept_radius = 5
        pointer.goto(intercept_x, intercept_y-intercept_radius)
        pointer.color("green")
        pointer.pendown()
        pointer.circle(intercept_radius)
        pointer.penup()

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
XC = int(input("Enter circle x coordinate: "))
YC = int(input("Enter circle y coordinate: "))
RADIUS = float(input("Enter radius of circle: "))

# drawing red circle
pointer.color("red")
pointer.goto(XC, YC - RADIUS)
pointer.pendown()
pointer.circle(RADIUS)
pointer.penup()

X1 = int(input("Enter line start x coordinate: "))
Y1 = int(input("Enter line start y coordinate: "))
X2 = int(input("Enter line end x coordinate: "))
Y2 = int(input("Enter line end y coordinate: "))

# drawing blue line
pointer.color("blue")
pointer.goto(X1, Y1)
pointer.pendown()
pointer. goto(X2, Y2)
pointer.penup()

# check if user draws a point or a line
if X1 == X2 and Y1 == Y2:
    # single point case
    # if the distance is equal to the radius then there is an intersection and a green circle will be drawn around it
    distance = math.sqrt((XC-X1)**2 + (YC-Y1)**2)
    difference = math.fabs(RADIUS - distance)
    if difference <= 0.75:
        intercept_radius = 5
        pointer.goto(X1,Y1-intercept_radius)
        pointer.color("green")
        pointer.pendown()
        pointer.circle(intercept_radius)
        pointer.penup()

else:
    # line case (not a single point)
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
        # finding the intercept and drawing a green circle around it
        alpha = (-B+math.sqrt(VALUE_UNDER_ROOT))/(2*A)
        draw_intercept(alpha)
    if VALUE_UNDER_ROOT > 0:
        # finding the two intercepts and drawing green circles around them
        alpha_positive_case = (-B + math.sqrt(VALUE_UNDER_ROOT)) / (2 * A)
        draw_intercept(alpha_positive_case)
        alpha_negative_case = (-B - math.sqrt(VALUE_UNDER_ROOT)) / (2 * A)
        draw_intercept(alpha_negative_case)

screen.exitonclick()
