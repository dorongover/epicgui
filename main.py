import random as ran
import PySimpleGUI as sg
sg.theme('DarkAmber')
bruh = ran. 
bruh2 = [1,2,3,4,5,6,7,8,9,0]
layout = [
    [sg.Text() ,sg.Button("press here to start"),sg.InputText()]
]

window = sg.Window("title",layout)
while True:
    event,values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 