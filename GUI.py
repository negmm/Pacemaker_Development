import time
import PySimpleGUI as sg
from PacemakerUser import PacemakerUser

#font = 'Arial',, background_color='white', , margins=(200, 200)
#Layout for first part
sg.theme('Teal Mono')
layout = [[sg.Text('Welcome to the Pace Maker', font=("Times New Roman",30))],
          [sg.Text('Please Login below', font=("Helvetica",15))],
          [sg.Text('Username ', font=("Helvetica",15)), sg.Input(font=("Helvetica",15,),key='-User-')],
          [sg.Text('Password ', font=("Helvetica",15)), sg.Input(font=("Helvetica",15), key='-Pass-')],
          [sg.Button('New User? Register here ', font=("Helvetica",15))],
          [sg.Button("Login", font=("Helvetica",12))]]
#size argument is x(length of a line),y(number of lines) size of the text box, e.g. size=(20,3)

#Signup layout
layout1 = [[sg.Text('Please Register below', font=("Helvetica",15))],
          [sg.Text('Username ', font=("Helvetica",15)), sg.Input(font=("Helvetica",15))],
          [sg.Text('Password ', font=("Helvetica",15)), sg.Input(font=("Helvetica",15))],
          [sg.Text('Re-enter Password ', font=("Helvetica",15)), sg.Input(font=("Helvetica",15))],
          [sg.Button("Sign Up", font=("Helvetica",12))]]

#Layout for incorrect input
layout2 = [[sg.Text('Welcome to the Pace Maker', font=("Times New Roman",30))],
          [sg.Text('Please Login below', font=("Helvetica",15))],
          [sg.Text('Incorrect Username or Password', text_color='red', font=("Helvetica",15))],
          [sg.Text('Username ', font=("Helvetica",15)), sg.Input(font=("Helvetica",15))],
          [sg.Text('Password ', font=("Helvetica",15)), sg.Input(font=("Helvetica",15))],
          [sg.Button("Login", font=("Helvetica",12))]]

window = sg.Window('Pace Maker', layout)


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    print(values)
    print(values['-User-'])
    print(values['-Pass-'])
    user_input = values['-User-']
    pass_input = values['-Pass-']

    
    #compare these values to the users registered
        #If true: move to ... not sure...
        #false: incorrect input layout2
    #sign up
        #total users < 10
            #Enter username
                #If username already taken, new layout, username taken
            #Enter password twice
                #If they match --> go to login layout
                #else --> new layout they dont match
        #total users > 10
            #new layout, max number of users reached, please login using an existing account

window.close()



