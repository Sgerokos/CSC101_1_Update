# Imports turtle module
import turtle

# The size of the board, along with the screen size and size of each square can be altered here
BOARD_SIZE = 8
SQUARE_SIZE = 60
SCREEN_SIZE = BOARD_SIZE * SQUARE_SIZE * 2


def draw_square(pen, size, color):
    """Draws a square with the given size and color"""
    pen.fillcolor(color)
    pen.begin_fill()
    for _ in range(4):
        pen.forward(size)
        pen.left(90)
    pen.end_fill()
    

def draw_board(pen, size, board_size):
    """Draws a checkerboard with the given size and number of squares"""
    for row in range(board_size):
        for col in range(board_size):
            # Set the position for the next square
            x = -size * board_size + size * col * 2
            y = -size * board_size + size * row * 2
            pen.up()
            pen.goto(x, y)
            pen.down()
            
            # Set the color for the square
            if (row + col) % 2 == 0:
                color = 'black'
            else:
                color = 'white'
            
            # Draw the square
            draw_square(pen, size, color)
    

if __name__ == '__main__':
    with turtle.Screen() as screen:
        # Create a turtle object
        pen = turtle.Turtle()
        pen.speed(0)
        
        # Set the screen size
        screen.setup(SCREEN_SIZE, SCREEN_SIZE)
        
        # Draw the checkerboard
        draw_board(pen, SQUARE_SIZE, BOARD_SIZE)
        
        # Hide the turtle
        pen.hideturtle()

        # Wait for the user to close the window
        screen.exitonclick()