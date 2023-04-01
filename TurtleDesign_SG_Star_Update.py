# Import turtle module
import turtle

# Define function to draw letter S
def draw_s():
    turtle.pensize(5)
    turtle.color("blue")
    turtle.backward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)

# Define function to draw letter G
def draw_g():
    turtle.pensize(10)
    turtle.color("red")
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(15)
    turtle.left(90)
    turtle.left(90)
    turtle.forward(30)

# Define function to draw star
def draw_star():
    turtle.pensize(8)
    turtle.color("grey")
    turtle.forward(100)
    turtle.right(144)
    turtle.forward(100)
    turtle.forward(100)
    turtle.right(144)
    turtle.forward(100)
    turtle.forward(100)
    turtle.right(144)
    turtle.forward(100)
    turtle.forward(100)
    turtle.right(144)
    turtle.forward(100)
    turtle.forward(100)
    turtle.right(144)
    turtle.forward(100)
    turtle.forward(100)
    turtle.right(144)
    turtle.forward(100)

# Set up turtle window
turtle.showturtle()
turtle.bgcolor("black")

# Draw the letters and star
draw_s()
turtle.penup()
turtle.goto(100, -50)
turtle.pendown()
draw_g()
turtle.penup()
turtle.goto(100, 50)
turtle.pendown()
turtle.left(20)
draw_star()

# Keep turtle window open until it is clicked
turtle.done()