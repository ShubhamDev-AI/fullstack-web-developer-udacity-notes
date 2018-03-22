import turtle

DRAWING_SPEED = 200 * 6
DEFAULT_SHAPE = 'turtle'
DEFAULT_COLOR = 'blue'
DEFAULT_BG_COLOR = 'white'


def draw_square(some_turtle):
    for i in range(1, 5):
        some_turtle.forward(100)
        some_turtle.right(90)


def draw_rhombus(some_turtle):
    for i in range(1, 3):
        some_turtle.forward(100)
        some_turtle.right(45)
        some_turtle.forward(100)
        some_turtle.right(135)


def draw_line(some_turtle, length):
    some_turtle.forward(length)


def draw_round_shape(some_turtle, draw_thing):
    angle = 0
    while angle < 360:
        # Create a shape
        some_turtle.shape(DEFAULT_SHAPE)
        some_turtle.color('blue')
        some_turtle.speed(DRAWING_SPEED)

        # Draw square
        draw_thing(some_turtle)
        some_turtle.right(5)

        # Update angle
        angle += 5


def draw_flower():
    # Set up screen and line color
    screen = turtle.Screen()
    screen.bgcolor(DEFAULT_BG_COLOR)

    # Create instance of Turtle
    jerry = turtle.Turtle()

    # Draw flower's leaf and its body
    draw_round_shape(jerry, draw_rhombus)
    jerry.right(90)
    draw_line(jerry, 300)


if __name__ == '__main__':
    draw_flower()
    input()
    # TODO: Draw some fractals, write some initials
