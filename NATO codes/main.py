import pandas
import tkinter as tk

student_data_frame = pandas.read_csv("./NATO codes/nato_phonetic_alphabet.csv")

NATO = {row.letter: row.code for (index, row) in student_data_frame.iterrows()}

def List():
    for word in result:
        word.pack_forget()
    if entry.get().isalpha():
        code = [NATO[letter] for letter in entry.get().upper() if letter in NATO]
        for i in range(len(code)):
            words = tk.Label(window, text=code[i])
            words.pack()
            result.append(words)
    
window = tk.Tk()
window.minsize(300,300)

label = tk.Label(window, text="Enter a word to get phonetic: ").pack()
entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="Get List", command=List)
button.pack()

result = []

window.mainloop()
