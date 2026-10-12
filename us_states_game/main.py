import os
import turtle
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

screen = turtle.Screen()
screen.title("U.S. States Game")
image = os.path.join(BASE_DIR, "blank_states_img.gif")
screen.addshape(image)

turtle.shape(image)


def get_mouse_click_coor(x, y):
    print(x, y)


turtle.onscreenclick(get_mouse_click_coor)


Data = pd.read_csv(os.path.join(BASE_DIR, "50_states.csv"))
all_states = Data.state.to_list()
guessed_states = []


while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 states are gussed", prompt="whats another state name "
    ).title()

    if answer_state == 'Exit':
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = Data[Data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)

