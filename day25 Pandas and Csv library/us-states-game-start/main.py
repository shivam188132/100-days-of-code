import turtle
import pandas

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("U.S state guessing game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/ 50 States_correct",
                                    prompt="What's another state name").title()

    if answer_state == "Exit":
        missing_state = [state for state in all_states if state not in guessed_state]
        print(missing_state)
        # for state in all_states:
        #     if state not in guessed_state:
        #         missing_state.append(state)
        # new_data = pandas.DataFrame(missing_state)
        # new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_state.append(answer_state)
        timmy = turtle.Turtle()
        timmy.hideturtle()
        timmy.penup()
        state_data = data[data.state == answer_state]
        timmy.goto(int(state_data.x), int(state_data.y))
        timmy.write(answer_state)
