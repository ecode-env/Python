from turtle import Turtle, Screen

# Create the turtle and screen objects
eyob = Turtle()
screen = Screen()

# Function to move the turtle forward
def move_forward():
    eyob.forward(10)

# Function to move the turtle backward
def move_backward():
    eyob.backward(10)

# Function to turn the turtle left
def move_left():
    eyob.left(10)

# Function to turn the turtle right
def move_right():
    eyob.right(10)

# Function to clear the screen and reset the turtle position
def clear():
    eyob.clear()
    eyob.penup()
    eyob.home()
    eyob.pendown()

# Listen for keypress events
screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(move_left, "a")
screen.onkey(move_right, "d")
screen.onkey(clear, "c")

# Keep the screen open until clicked
screen.exitonclick()
