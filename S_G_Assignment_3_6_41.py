import turtle
import random

# Define constants
NUM_DOTS = 10
CIRCLE_RADIUS = 50
SQUARE_WIDTH = 100
SQUARE_HEIGHT = 100

# Define functions

def distance(x1, y1, x2, y2):
    """Calculate the distance between two points."""
    try:
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    except TypeError:
        return float('inf')

def draw_circle_dot(x, y):
    """Draw a dot within the circle."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(3)
    turtle.end_fill()

def draw_circle(x, y, radius):
    """Draw a circle at the given position and radius."""
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.circle(radius)

def draw_square(x, y, width, height):
    """Draw a square at the given position and dimensions."""
    turtle.penup()
    turtle.goto(x + width / 2, y + height / 2)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)

def draw_dots_in_circle():
    """Draw the specified number of dots within the circle."""
    i = 0
    while i < NUM_DOTS:
        x = random.randint(0, 100)
        y = random.randint(-50, 50)
        if distance(x, y, 50, 0) <= CIRCLE_RADIUS:
            draw_circle_dot(x, y)
            i += 1

def draw_dots_in_square():
    """Draw the specified number of dots within the square."""
    for i in range(NUM_DOTS):
        x = random.randint(-125, -25)
        y = random.randint(-50, 50)
        draw_circle_dot(x, y)

def main():
    """Draw the shapes and dots."""
    draw_square(-75, 0, SQUARE_WIDTH, SQUARE_HEIGHT)
    draw_circle(50, 0, CIRCLE_RADIUS)
    draw_dots_in_circle()
    draw_dots_in_square()

if __name__ == '__main__':
    turtle.speed('fastest')
    try:
        main()
    except Exception as e:
        print(f'An error occurred: {e}')
    turtle.done()