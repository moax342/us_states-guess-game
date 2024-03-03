from turtle import Turtle

FONT = ("Arial", 10, "normal")


class State(Turtle):

    def __init__(self, state, position):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.state = state
        self.state_position = position

    def goto_position(self):
        self.goto(self.state_position)
        self.write(f"{self.state}",align="center",font=FONT)
