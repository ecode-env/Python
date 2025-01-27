from turtle import Turtle, Screen

eyob = Turtle()
screen = Screen()

def move_turtle():
    eyob.fd(100)

screen.listen()
screen.onkey(key='space', fun=move_turtle)

screen.exitonclick()