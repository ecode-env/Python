from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.penup()
paddle.shapesize(5, 1)
paddle.goto(350, 0)

def go_up():
    paddle.goto(paddle.xcor(), paddle.ycor() + 20)
def go_down():
    paddle.goto(paddle.xcor(), paddle.ycor() - 20)

screen.listen()
screen.onkey(go_up, 'Up')
screen.onkey(go_down, 'Down')

is_game_on = True
while is_game_on:
    screen.update()










screen.exitonclick()