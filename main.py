import pandas
import turtle
from states_data import State

screen=turtle.Screen()
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.setup(width=725,height=491)

score =0

states_data=pandas.read_csv("50_states.csv")
states = states_data["state"].tolist()
game_is_on=True
while game_is_on:

    answer_state = screen.textinput(f"{score}/50 Guess a state", "Which state do you want to choose?")
    for state in states:
        if state == answer_state.title():
            state_index = states.index(state)
            pos_x = states_data.x[state_index]
            pos_y = states_data.y[state_index]
            State(state,(pos_x,pos_y)).goto_position()
            score +=1
        elif answer_state=="":
            game_is_on=False

screen.exitonclick()
