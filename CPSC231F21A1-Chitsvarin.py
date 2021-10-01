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

# import libraries
import turtle
import math

# define constants
WIDTH = 800
HEIGHT = 600

# define global variable sum_of_intercepts
sum_of_intercepts = 0

# the function takes the alpha and line coordinates as arguments
# it tries to find an intercept
# and draws a green circle if there is an intercept
# References:
# function declaration with arguments https://www.w3schools.com/python/python_functions.asp
def draw_intercept(alpha, x1, y1, x2, y2):
    # this assures that an intersection does not occur outside of the end points of the line segment
    if  alpha >= 0 and alpha <= 1:
        # find intercept coordinates
        intercept_x = (1-alpha) * x1 + (alpha * x2)
        intercept_y = (1-alpha) * y1 + (alpha * y2)

        # draw intercept
        intercept_radius = 5
        pointer.goto(intercept_x, intercept_y-intercept_radius)
        pointer.color("green")
        pointer.pendown()
        pointer.circle(intercept_radius)
        pointer.penup()
        # access and increment global variable 'sum_of_intercepts' every time intersection is drawn
        # References:
        # access and modify global variables https://stackoverflow.com/questions/10588317/python-function-global-variables
        global sum_of_intercepts
        sum_of_intercepts = sum_of_intercepts + 1


# This function writes 'No Intersect' in the middle of the screen if there are no intersections
# Reference:
# write() function https://docs.python.org/3.3/library/turtle.html?highlight=turtle#turtle.write
def write_no_intersect():
    pointer.goto(WIDTH/2, HEIGHT/2)
    pointer.color("green")
    pointer.write("No Intersect!", True, align="center")


# This function takes user input for line coordinates and draws a blue line
def draw_blue_line(x1_string, y1_string, x2_string, y2_string):
    # remember sum of intercepts before drawing the line
    global sum_of_intercepts
    sum_of_intercepts_before = sum_of_intercepts

    # convert variables x1,y1,x2,y2 from string to integer
    x1 = int(x1_string)
    y1 = int(y1_string)
    x2 = int(x2_string)
    y2 = int(y2_string)

    # drawing blue line
    pointer.color("blue")
    pointer.goto(x1, y1)
    pointer.pendown()
    pointer. goto(x2, y2)
    pointer.penup()

    # check if user wants to draw a point or a line
    if x1 == x2 and y1 == y2:
        # single point case

        # find distance and difference
        distance = math.sqrt((XC - x1) ** 2 + (YC - y1) ** 2)
        difference = math.fabs(RADIUS - distance)

        # if difference between radius an distance is within 0.75 then there is an intersection and a green circle will be drawn around it
        if difference <= 0.75:
            intercept_radius = 5
            pointer.goto(x1, y1 - intercept_radius)
            pointer.color("green")
            pointer.pendown()
            pointer.circle(intercept_radius)
            pointer.penup()
            sum_of_intercepts = sum_of_intercepts + 1
    else:
        # line case (not a single point)

        # calculate a,b, and c used in quadratic formula
        a = (x2 - x1) ** 2 + (y2 - y1) ** 2
        b = 2*((x1 - XC) * (x2 - x1) + (y1 - YC) * (y2 - y1))
        c = (x1 - XC) ** 2 + (y1 - YC) ** 2 - RADIUS ** 2

        # looking at the value under the root to find the number of intersections
        # References:
        # if statements http://anh.cs.luc.edu/handsonPythonTutorial/ifstatements.html
        value_under_root = (b**2 - 4*a*c)

        # there are no intersections, write 'no intersect'
        if value_under_root < 0:
            write_no_intersect()

        # there is one intercept, draw it
        if value_under_root == 0:
            # finding the intercept and drawing a green circle around it
            alpha = (-b+math.sqrt(value_under_root))/(2*a)
            draw_intercept(alpha, x1, y1, x2, y2)

        # there are two intercepts, draw them
        if value_under_root > 0:
            # finding the two intercepts and drawing green circles around them
            alpha_positive_case = (-b + math.sqrt(value_under_root)) / (2 * a)
            draw_intercept(alpha_positive_case, x1, y1, x2, y2)
            alpha_negative_case = (-b - math.sqrt(value_under_root)) / (2 * a)
            draw_intercept(alpha_negative_case, x1, y1, x2, y2)
    # access global variable 'sum_of_intercepts' and print its value
    if sum_of_intercepts_before == sum_of_intercepts:
        write_no_intersect()
    print(sum_of_intercepts, "intersections have been found so far")

# this code is from assignment description
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

# getting input about circle and converting it to required types
# References:
# string to float conversion https://stackoverflow.com/questions/379906/how-do-i-parse-a-string-to-a-float-or-int
XC = int(input("Enter circle x coordinate: "))
YC = int(input("Enter circle y coordinate: "))
RADIUS = float(input("Enter radius of circle: "))

# drawing red circle
pointer.color("red")
pointer.goto(XC, YC - RADIUS)
pointer.pendown()
pointer.circle(RADIUS)
pointer.penup()

# asking user to input line coordinates
x1_string = input("Enter line start x coordinate: ")
y1_string = input("Enter line start y coordinate: ")
x2_string = input("Enter line end x coordinate: ")
y2_string = input("Enter line end y coordinate: ")

# use these coordinates to draw a blue line
draw_blue_line(x1_string, y1_string, x2_string, y2_string)

# asking for additional pairs of coordinates (bonus) and drawing a line
# References:
# while loop https://www.w3schools.com/python/python_while_loops.asp
# break from while loop https://realpython.com/python-while-loop/
while 1:
    # ask user to enter line coordinates
    # if user enters a blank coordinate the loop breaks
    x1_string = input("Enter line start x coordinate (additional input): ")
    if x1_string == "":
        break
    y1_string = input("Enter line start y coordinate (additional input): ")
    if y1_string == "":
        break
    x2_string = input("Enter line end x coordinate (additional input): ")
    if x2_string == "":
        break
    y2_string = input("Enter line end y coordinate (additional input): ")
    if y2_string == "":
        break
    draw_blue_line(x1_string, y1_string, x2_string, y2_string)

# exit on click
screen.exitonclick()
