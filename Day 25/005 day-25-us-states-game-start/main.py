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





while len(guessed_state) < 50:
    answer = screen.textinput(title=f'{len(guessed_state)}/{len(data_list)} Correct', prompt='What\'s another state\'s name?').title()
    if answer == 'Exit':
        missing_states = [state for state in data_list if state not in guessed_state]
        new_state = pd.DataFrame(missing_states)
        new_state.to_csv('state_to_learn.csv')
        break
    if answer in data_list:
        guessed_state.append(answer)
        writer.penup()
        writer.hideturtle()
        pos = data[data.state == answer]
        writer.goto(pos.x.item(), pos.y.item())
        writer.write(answer)
def result_gn():
    pass