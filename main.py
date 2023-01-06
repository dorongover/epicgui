import PySimpleGUI as sg
sg.theme('DarkAmber') 
layout = [
    [sg.Button("press here to start"),sg.InputText()]
]

window = sg.Window("title",layout)
while True:
    event,values = window.read()
    if event == sg.WIN_CLOSED:
        break