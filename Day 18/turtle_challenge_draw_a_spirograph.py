import random
import turtle as t

eyob = t.Turtle()
t.colormode(255)


eyob.speed('fastest')

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

def draw_spirograph(size_of_gap):
    for _ in range( int(360 / size_of_gap) ):
        eyob.color(random_color())
        eyob.circle(100)
        eyob.setheading(eyob.heading() + size_of_gap)


draw_spirograph(10)

screen = t.Screen()
screen.exitonclick()