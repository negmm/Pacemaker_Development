#%% Import Libraries
import time
import PySimpleGUI as sg
from PacemakerUser import verify, register

#%% Login Screen Layout

#font = 'Arial',, background_color='white', , margins=(200, 200)

sg.theme('Teal Mono')
loginLayout = [[sg.Text('Welcome to the Pace Maker', font=("Times New Roman",30))],
          [sg.Text('Please Login below', font=("Helvetica",15))],
          [sg.Text('Username ', font=("Helvetica",15)), sg.Input(font=("Helvetica",15,),key='-User-')],
          [sg.Text('Password ', font=("Helvetica",15)), sg.Input(font=("Helvetica",15), key='-Pass-', password_char="*")],
          [sg.Button('New User? Register here ', font=("Helvetica",15))],
          [sg.Button("Login", font=("Helvetica",12))]]

#%% Signup Layout

signupLayout = [[sg.Button("Back to Login")],
                [sg.Text('Please Register below', font=("Helvetica",15))],
                [sg.Text('Username ', font=("Helvetica",15)), sg.Input(font=("Helvetica",15), key="-newUser-")],
                [sg.Text('Password ', font=("Helvetica",15)), sg.Input(font=("Helvetica",15), key="-newPass-",password_char="*")],
                [sg.Text('Re-enter Password ', font=("Helvetica",15)), sg.Input(font=("Helvetica",15), key="-verifyPass-",password_char="*")],
                [sg.Button("Sign Up", font=("Helvetica",12))]]

#%% Pacing modes Layout 
#Button Layouts, for simplicity I used a dictionary and unpacked it for each button element instead of defining the parameters for individual buttons
modeButLay = {'size':(7,2), 'font':('Franklin Gothic Book', 24), 'button_color':("Black","#FFC0CB"), 'border_width':2}
selectLayout = [[sg.Button("Logout")],
           [sg.Text('Select Pacing Mode', font=("Franklin Gothic Book",30))],
           [sg.Button("AOO",**modeButLay), sg.Button("VOO",**modeButLay)],
           [sg.Button("AAI",**modeButLay), sg.Button("VVI",**modeButLay)]]


#%% Parameters Layout
#Parameter names list
paramNameList = ['Lower Rate Limit       ', 'Upper Rate Limit       ','Maximum Sensor Rate    ','Fixed AV Delay         ','Dynamic AV Delay       ',
                'Sensed AV Delay Offset ','Atrial Amplitude       ','Ventricular Amplitude  ','Atrial Pulse Width     ','Ventricular Pulse Width',
                'Atrial Sensitivity     ','Ventricular Sensitivity','    VRP                ','    ARP                ','    PVARP              ',
                'PVARP Extension        ','  Hysteresis           ',' Rate Smoothing        ','ATR Duration           ','ATR Fallback Mode      ',
                'ATR Fallback Time      ','Activity Threshold     ','Reaction Time          ','Response Factor        ','Recovery Time          ']

#Layouts for parameter layout elements
paramButLay = {'font':('Franklin Gothic Book', 14), 'button_color':("Black","#FFC0CB"), 'border_width':2}       
paramTextLay = {'font':('Franklin Gothic Book', 14), 'visible':False, 'justification':'centre', 'size':(30,1)}
paramInputLay = {'font':('Franklin Gothic Book', 14), 'visible':False, 'justification':'left', 'size':(20,1)}   

modeLayout = [[sg.Button("Go Back")],
          [sg.Text('', font=("Franklin Gothic Book",30), key = "-ParTitle-")],
           [sg.Text('Parameter Input Out of Range', text_color='red', font=("Helvetica",15), visible=False,key="-FalseParIN-")],
          *[[sg.pin(sg.Text(str(paramNameList[i]), key=f'-Par{i}-', **paramTextLay)),
             sg.pin(sg.Input(key=f'-ParIN{i}-',**paramInputLay))]
            for i in range(len(paramNameList))],
           [sg.Button("Set Parameters",**paramButLay)]]

#%% Functions to update pacing mode layout

#Determines which pacing paramters will be active based on the pacing mode
def pacingModePar(paceMode):
    if(paceMode == 'AOO'):
        return [0,1,6,8]
    elif(paceMode == 'VOO'):
        return [0,1,7,9]
    elif(paceMode == 'AAI'):
        return [0,1,6,8,10,13,14,16,17]
    elif(paceMode == 'VVI'):
        return [0,1,7,9,11,12,16,17]

#Updates the visibility of the parameters
def updateVisibility():
    paramVisb = pacingModePar(pacingMode)
    for i in paramVisb:
        visbList[i] = True

#Changes the visibility of certain paremters
def changeVisibility(visbiList):
    for keyVal in visbiList:
        window[f'-Par{keyVal}-'].Update(visible=True)
        window[f'-ParIN{keyVal}-'].Update(visible=True)

#Resets the visibility of all parameter except LR and UP Limit
def resetVisibility():
    for keyVal in range(0,len(paramNameList)):
        window[f'-Par{keyVal}-'].Update(visible=False)
        window[f'-ParIN{keyVal}-'].Update(visible=False)

#Shows incorrect input text when Parameter input is out of range(will have more functionailty once we implement param values)
def paramOFR():
    window['-FalseParIN-'].Update(visible=True)

#General Function for changing a text element based on key
def updateText(key, parm):
   window[key].Update(f"{str(parm)}")

#Clear the data in the corresponding key's input text box
def clrTextInput(key):
    for i in key:
        window[i].Update("")

#Clear all data in all boxes in previously selected pacing mode
def clrAllTextInput(pacingMode):
    onTerms = pacingModePar(pacingMode)
    lst = []
    for i in onTerms:
        lst.append(f'-ParIN{i}-')
    clrTextInput(lst)
        
#Clear Error Messages
def clearErrors():
    window['_text1_'].update(visible = False)
    window['_text2_'].update(visible = False)
    window['_text3_'].update(visible = False)
    window['_text4_'].update(visible = False)
    
#%% Display/Run app 
loginKeys = ["-User-", "-Pass-"]
signupKeys = ['-newUser-', '-newPass-', '-verifyPass-']
layout = [[sg.Column(loginLayout, visible = True, key='-COL1-'),
           sg.Column(signupLayout, visible=False, key='-COL2-'),
           sg.Column(selectLayout, visible = False, key='-COL3-'), 
           sg.Column(modeLayout, visible=False, key='-COL4-'),
           sg.Text("Incorrect Password or Username", visible = False, key = "_text1_"),
           sg.Text("Maximum number of users already registered.", visible = False, key = "_text2_"),
           sg.Text("Passwords do not match.", visible = False, key = "_text3_"),
           sg.Text("Username already in use.", visible = False, key = "_text4_")]]

window = sg.Window('Pace Maker', layout)
layout =1
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    
    ## Go to register screen
    if (event == 'New User? Register here '):
        clearErrors()
        window[f'-COL{layout}-'].update(visible = False)
        layout = 2
        clrTextInput(loginKeys)
        window[f'-COL{layout}-'].update(visible = True)
    
    ## Verify Login
    if (event == 'Login'):
        clearErrors()
        clrTextInput(loginKeys)
        if (verify(values['-User-'], values['-Pass-']) == True):
            window[f'-COL{layout}-'].update(visible = False)
            layout = 3
            window[f'-COL{layout}-'].update(visible = True)
        else:
            window['_text1_'].update(visible = True)
            
    ## Verify Registration        
    if event == "Sign Up":
        print("sign up")
        clearErrors()
        if ((values['-newPass-'] == values['-verifyPass-']) and (values['-newPass-'] != "" and values['-newUser-'] != "")):
            verifyReg = register(values['-newUser-'], values['-newPass-'])
            if(verifyReg < 0):
                window['_text2_'].update(visible = True)
            elif (verifyReg < 1):
                window['_text4_'].update(visible = True)
            else:
                clrTextInput(signupKeys)
                window[f'-COL{layout}-'].update(visible=False)
                layout = 1
                window[f'-COL{layout}-'].update(visible=True)
        else:
            window['_text3_'].update(visible = True)
    
    ## Open mode screen  
    if event in ['AOO', 'VOO', 'AAI', 'VVI']:
        updateText('-ParTitle-', f'Please Enter the {event} Parameters')
        pacingMode = event
        changeVisibility(pacingModePar(event))
        window[f'-COL{layout}-'].update(visible=False)
        layout = 4
        window[f'-COL{layout}-'].update(visible=True)
    
    ## Go to previous page
    if event == 'Go Back':
        resetVisibility()
        clrAllTextInput(pacingMode)
        window[f'-COL{layout}-'].update(visible=False)
        layout = layout-1
        window[f'-COL{layout}-'].update(visible=True)
    
    ## Go back to login screen
    if (event == "Logout" or event == "Back to Login"):
        if event == "Back to Login":
            clrTextInput(signupKeys)
        clearErrors()
        window[f'-COL{layout}-'].update(visible=False)
        layout = 1
        window[f'-COL{layout}-'].update(visible=True)
        
window.close()



