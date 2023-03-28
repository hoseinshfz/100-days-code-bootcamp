import turtle
import pandas
from turtle import Screen
from states_game import StatesNameWriter

IMG_FILE_NAME = "blank_states_img.gif"
STATES_FILE_NAME = "50_states.csv"
NUMBER_OF_STATES = 50

data = pandas.read_csv(STATES_FILE_NAME)

screen = Screen()
screen.title('U.S. States Guess Game')
screen.addshape(IMG_FILE_NAME)
turtle.shape(IMG_FILE_NAME)

state_name = StatesNameWriter()
all_states_name = data['state'].to_list()
guessed_states = []
score = 0
while len(guessed_states) < NUMBER_OF_STATES:
    answer = screen.textinput(title=f"{score}/50 Guess the State", prompt="Enter a State's name: ").title()
    if answer == 'Exit':
        missing_states = [state for state in all_states_name if state not in guessed_states]
        df = pandas.DataFrame(missing_states)
        df.to_csv('states_to_learn.csv')
        break
    row = data[data['state'] == answer]
    if len(row) == 0:
        print("Wrong State Name, try again!")
    else:
        if answer not in guessed_states:
            pos = (int(row['x']), int(row['y']))
            state_name.write_state(state=answer, pos=pos)
            guessed_states.append(answer)
            score += 1
        else:
            print(f"You already have guessed {answer}.")
