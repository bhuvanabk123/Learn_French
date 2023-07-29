import random

BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas
current_card = {}
words_dict = {}
# Logic


try:
    words = pandas.read_csv('./data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pandas.read_csv('./data/french_words.csv')
    words_dict = original_data.to_dict(orient = 'records')
else:
    words_dict = words.to_dict(orient = 'records')


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words_dict)
    canvas.itemconfig(title_text, text = "French", fill = 'black')
    canvas.itemconfig(word_text, text = current_card['French'], fill = 'black')
    canvas.itemconfig(canvas_image, image = card_front)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(canvas_image, image = card_back)
    canvas.itemconfig(title_text, text = "English", fill = 'white')
    canvas.itemconfig(word_text, text = current_card['English'], fill = 'white')


words_to_learn = []

def right_button_click():
    words_dict.remove(current_card)
    data = pandas.DataFrame(words_dict)
    data.to_csv('./data/words_to_learn.csv', index = False)
    next_card()





####### UI ###########
window = Tk()
window.config(padx=50, pady = 50, bg= BACKGROUND_COLOR)
window.title( "FlashCard")
# window.minsize(width = , height = 500)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width = 800, height = 526, bg=BACKGROUND_COLOR,highlightthickness=0)

card_front = PhotoImage(file = './images/card_front.png')
canvas_image = canvas.create_image(400,260, image = card_front)
canvas.grid(row= 0, column =0, columnspan=2)

card_back = PhotoImage(file = './images/card_back.png')



title_text = canvas.create_text(400, 150, text = "French", font = ('Ariel' , 40, 'italic'))
word_text =canvas.create_text(400, 260 , text = "WORD",  font = ('Ariel', 60, 'bold'))

right_button_image =  PhotoImage(file = './images/right.png')
right_button = Button(image = right_button_image, highlightthickness=0, command = right_button_click)
right_button.grid(row= 1, column =1)

wrong_button_image = PhotoImage(file = './images/wrong.png')
wrong_button = Button(image = wrong_button_image, highlightthickness=0, command = next_card)
wrong_button.grid(row = 1, column=0)

next_card()

window.mainloop()



