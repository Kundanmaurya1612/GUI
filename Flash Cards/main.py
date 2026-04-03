from tkinter import *  # type: ignore
import pandas as pd
from tkinter import messagebox

def right_change():
    global score
    score +=1
    del data["name"][number], data["use"][number]
    change()

def wrong_change():
    global score
    score -=1
    change()

def change():
    global number,time
    if number < len(data["name"]) - 1:
        number +=1
        if time: window.after_cancel(id=time)
        canvas.itemconfig(word, text=data["name"][number])
        canvas.itemconfig(word, font=("Ariel", 40, "bold"))
        canvas.itemconfig(card, image=front_card_image)
        canvas.itemconfig(title, text="Name")
        canvas.itemconfig(title, fill="black")
        canvas.itemconfig(word, fill="black")
        time = window.after(3000, flip)
    elif number == len(data["name"]) - 1:
        number +=1
        canvas.itemconfig(word, text=score)
        canvas.itemconfig(word, font=("Ariel", 60, "bold"))
        canvas.itemconfig(card, image=front_card_image)
        canvas.itemconfig(title, text="Score")
        canvas.itemconfig(title, fill="black")
        canvas.itemconfig(word, fill="green")
    else:
        window.destroy()

def flip():
    global number
    canvas.itemconfig(card, image=back_card_image)
    canvas.itemconfig(title, text="Use")
    canvas.itemconfig(title, fill="white")
    canvas.itemconfig(word, text=data['use'][number])
    canvas.itemconfig(word, font=("Ariel", 20, "bold"))
    canvas.itemconfig(word, fill="white")

BACKGROUND_COLOR = "#B1DDC6"

csv = pd.read_csv("./Flash Cards/data/machines.csv")
data = pd.DataFrame.to_dict(csv)

number = 0
score = -1
time = NONE

window = Tk()
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
front_card_image = PhotoImage(file="./Flash Cards/images/card_front.png")
back_card_image = PhotoImage(file="./Flash Cards/images/card_back.png")
wrong_image = PhotoImage(file="./Flash Cards/images/wrong.png")
right_image = PhotoImage(file="./Flash Cards/images/right.png")

canvas = Canvas(window, width=800, height=526,background=BACKGROUND_COLOR, highlightthickness=0)
card = canvas.create_image(400,263,image=front_card_image)
title = canvas.create_text(400,150, text="Name",font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text=data["name"][0], font=("Ariel", 60, "bold"))
canvas.grid(row=0,column=0, columnspan=2)

wrong = Button(window, image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR, borderwidth=0, command=wrong_change)
wrong.grid(row=1, column=0)
right = Button(window, image=right_image, highlightthickness=0, bg=BACKGROUND_COLOR, borderwidth=0,command=right_change)
right.grid(row=1, column=1)

window.after(4000,flip)

window.mainloop()

with open("./Flash Cards/machine_to_learn.csv", "w") as file:
    to_learn = pd.DataFrame(data).to_csv(index=False,lineterminator='\n')
    file.write(to_learn)