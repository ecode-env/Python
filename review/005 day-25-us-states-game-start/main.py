import turtle
import pandas as pd

screen = turtle.Screen()
writer = turtle.Turtle()
screen.title('U.S States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)


data = pd.read_csv('50_states.csv')
data_list = data.state.to_list()


left_question = len(data_list)
guessed_state = []

if len(guessed_state) < 50:
    answer = screen.textinput(title=f'{len(guessed_state)}/{len(data_list)} Correct', prompt='What\'s another state\'s name?').title()
    if answer ==
    print(data)

screen.exitonclick()