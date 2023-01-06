import random
import PySimpleGUI as sg
sg.theme('DarkAmber')

word_ls = ['develop','work','make','tomorrow','control','visual','computer','interest','bruh']


def combine_sentence(word_ls):
  sentence = ""
  for i in range(len(word_ls)):
    sentence += word_ls[i] + " "
  return sentence


sentence = combine_sentence(random.sample(word_ls, len(word_ls)))

layout = [
    [sg.Text(sentence)],
    [sg.Button("press here to start",key="field"),sg.InputText(key='text')]
]

window = sg.Window("title",layout)
win = False
while True:
    event,values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "field":
        t = values['text']
        if t == sentence:
            win = True
        break
