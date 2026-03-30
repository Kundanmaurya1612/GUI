import pandas
import tkinter as tk


student_data_frame = pandas.read_csv("./NATO codes/nato_phonetic_alphabet.csv")



NATO = {row.letter: row.code for (index, row) in student_data_frame.iterrows()}


# user = input("Enter a word to get phonetic: ").upper()

# code = [ NATO[code] for code in user]
# print(f"\n{code}")
def List():
    code = [NATO[letter] for letter in entry.get().upper() if letter in NATO]
    for i in range(len(code)-1):
        tk.Label(window, text=code[i]).pack()

window = tk.Tk()
window.minsize(300,300)

label = tk.Label(window, text="Enter a word to get phonetic: ").pack()
entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="Get List", command=List)
button.pack()





window.mainloop()
