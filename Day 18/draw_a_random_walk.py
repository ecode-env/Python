import random
import turtle as t

eyob = t.Turtle()
t.colormode(255)
# turtle_colors = [
#     "red", "blue", "green", "yellow", "purple", "orange",
#     "pink", "brown", "black", "white", "gray", "cyan",
#     "magenta", "lime", "turquoise", "gold", "navy", "coral",
#     "indigo", "violet", "salmon", "chocolate", "beige", "dark green"
# ]

direction = [0, 90, 180, 270]
eyob.pensize(15)
eyob.speed('fastest')

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

for _ in range(200):
    eyob.color(random_color())
    eyob.forward(30)
    eyob.setheading(random.choice(direction))
