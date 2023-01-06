import random
import random as ran
import PySimpleGUI as sg
sg.theme('DarkAmber')

word_ls = ['develop','work','make','tomorrow','control','visual','computer','interest','bruh']



for i in range(6):
    sent = random.choice(word_ls)
    print(sent)

layout = [
    [sg.Button("press here to start",key="field"),sg.InputText(key='text')]
]

window = sg.Window("title",layout)

while True:
    event,values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "field":
        t = values['text']
        print(t)