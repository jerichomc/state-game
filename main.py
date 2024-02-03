import turtle
import pandas

correct = 0
screen = turtle.Screen()
screen.title("Guess the state")
image = "blank_states_img.gif" #using picture path and setting it as the image variable
screen.addshape(image)  #adding new shape to be used in turtle
turtle.shape(image)


# def get_mouse_click_coor(x, y): #is a function to get a coordinate on every click
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor) #listens for mouse click and calls the function
# turtle.mainloop() #keeps screen open

game_is_on = True
correct_states = []
data = pandas.read_csv("50_states.csv")
state_list = data["state"].to_list() #puts all the states into a list
state_to_dict = data.to_dict()



while len(correct_states) < 50:
    answer_state = screen.textinput(title=f"Correct states: {correct}/50", prompt="Name a state").title() #asks the user for an input
    if answer_state == "Exit":
        missing_states = [state for state in state_list if state not in correct_states]
        # for state in state_list:
        #     if state not in correct_states:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in state_list:
        if answer_state not in correct_states:
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            guessed_state = data[data.state == answer_state]
            #t.goto(guessed_state.x, guessed_state.y)
            correct_x = int(guessed_state.x)
            correct_y = int(guessed_state.y) #uneeded but another way to do previous line
            t.goto(correct_x, correct_y)
            t.write(answer_state)
            correct_states.append(answer_state)
            correct += 1











screen.exitonclick()