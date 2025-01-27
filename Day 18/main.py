import random
from turtle import Turtle, Screen


eyob_the_turtle = Turtle()
# eyob_the_turtle.shape("turtle")
# eyob_the_turtle.color('red')


# dash line

# for _ in range(15):
#     eyob_the_turtle.forward(10)
#     eyob_the_turtle.pendown()
#     eyob_the_turtle.forward(10)
#     eyob_the_turtle.penup()


# eyob_the_turtle.right(90)
# eyob_the_turtle.forward(100)
# eyob_the_turtle.right(90)
# eyob_the_turtle.forward(100)
# eyob_the_turtle.right(90)
# eyob_the_turtle.forward(100)
# eyob_the_turtle.right(90)
# eyob_the_turtle.forward(100)

# eyob_the_turtle.forward(80)
# eyob_the_turtle.right(72)

# angel = 3
# rotate = True
# while rotate:
#     if 360 / angel == 0:
#         rotate = False
#     for _ in range(angel):
#         eyob_the_turtle.right(360 / angel)
#         eyob_the_turtle.forward(100)
#     angel = angel + 1
#     print(angel)

# Array of colors for Python turtle
turtle_colors = [
    "red", "blue", "green", "yellow", "purple", "orange",
    "pink", "brown", "black", "white", "gray", "cyan",
    "magenta", "lime", "turquoise", "gold", "navy", "coral",
    "indigo", "violet", "salmon", "chocolate", "beige", "dark green"
]




def draw_shape(num_sides):
    angele = 360 / num_sides
    for _ in range(num_sides):
        eyob_the_turtle.forward(100)
        eyob_the_turtle.right(angele)

for shape_side_n in range(3, 11):
    eyob_the_turtle.color(random.choice(turtle_colors))
    draw_shape(shape_side_n)

screen = Screen()

screen.exitonclick()