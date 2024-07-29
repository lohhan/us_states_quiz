import turtle
import pandas as pd

screen = turtle.Screen()

screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
states = data.state.tolist()

correct_guesses = []
while len(correct_guesses) < 50:
   answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct", prompt="What's another state's name: ").title()

   # if answer_state == "Exit":
   #    missing_states = []
   #    for item in states:
   #       if item not in correct_guesses:
   #          missing_states.append(item)
   #    df = pd.DataFrame(missing_states)
   #    df.to_csv("missing_states.csv")
   #    break

   if answer_state == "Exit":
      missing_states = [item for item in states if item not in correct_guesses]
      df = pd.DataFrame(missing_states)
      df.to_csv("missing_states.csv")
      break

   if answer_state in states:
      if answer_state not in correct_guesses:
         correct_guesses.append(answer_state)
         state_data = data[data.state == answer_state]
         t = turtle.Turtle()
         t.hideturtle()
         t.penup()
         t.speed("fastest")
         t.goto(int(state_data.x), int(state_data.y))
         t.write(answer_state)