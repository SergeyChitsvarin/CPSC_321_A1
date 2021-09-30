
import turtle

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
X_C = int(input("Enter the Xc (integer): "))
Y_C = int(input("Enter the Yc (integer): "))
RADIUS = float(input("Enter the radius (float): "))
X_1 = int(input("Enter X1 (integer): "))
Y_1 = int(input("Enter Y1 (integer): "))
X_2 = int(input("Enter X2 (integer): "))
Y_2 = int(input("Enter Y2 (integer): "))

# drawing red circle

pointer.color("red")
pointer.goto(X_C, Y_C-RADIUS)
pointer.pendown()
pointer.circle(RADIUS)
pointer.penup()

# drawing blue line





screen.exitonclick()














