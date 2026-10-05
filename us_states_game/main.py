import turtle
import pandas as pd
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "us_states_game/blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)


def get_mouse_click_coor(x,y):
    print(x,y)
turtle.onscreenclick(get_mouse_click_coor)



Data = pd.read_csv("us_states_game/50_states.csv")
all_states = Data.state.to_list()


answer_state = screen.textinput(title="Guess the state" , prompt= "whats another state name ")
if answer_state is not None:
    answer_state = answer_state.title()
print(answer_state)

if answer_state in all_states:
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    state_data = Data[Data.state == answer_state]
    t.goto(state_data.x, state_data.y)
    t.write(state_data.state)



turtle.mainloop()