#import colorgram
import random
import turtle
# rgb_color = []
#
# colors = colorgram.extract('image_converted.jpg', 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_color.append(new_color)

from turtle import Turtle, Screen
import random

# Set up the screen color mode
screen = Screen()
screen.colormode(255)

# Create the turtle object
eyob = Turtle()
eyob.speed("fastest")
eyob.penup()

# List of colors (RGB tuples)
color_list = [
    (222, 232, 226), (208, 161, 82), (54, 89, 131), (146, 91, 40), (140, 26, 48),
    (222, 206, 108), (132, 177, 203), (45, 55, 104), (158, 46, 83), (169, 160, 39),
    (128, 189, 143), (83, 20, 44), (38, 42, 67), (186, 93, 105), (187, 139, 171),
    (84, 122, 181), (59, 39, 31), (78, 153, 165), (88, 157, 91), (195, 79, 72),
    (161, 202, 220), (45, 74, 77), (80, 73, 44), (57, 131, 122), (217, 176, 188),
    (220, 182, 167), (166, 207, 165)
]

# Move the turtle to the starting position
eyob.setheading(250)
eyob.forward(300)
eyob.setheading(0)

# Number of dots
number_of_dots = 100

# Draw the dots
for dot_count in range(1, number_of_dots + 1):
    eyob.dot(20, random.choice(color_list))  # Draw a dot with a random color
    eyob.forward(50)  # Move forward for the next dot

    # Change row after every 10 dots
    if dot_count % 10 == 0:
        eyob.setheading(90)
        eyob.forward(50)
        eyob.setheading(180)
        eyob.forward(500)
        eyob.setheading(0)

# Exit the screen on click
screen.exitonclick()


