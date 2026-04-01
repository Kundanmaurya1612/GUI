from tkinter import * # type: ignore
from tkinter import messagebox
import random
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = [random.choice(letters) for letter in range(random.randint(8, 10))]
    nr_numbers = [random.choice(numbers) for letter in range(random.randint(2, 4))]
    nr_symbols = [random.choice(symbols) for letter in range(random.randint(2, 4))]

    password_list = nr_letters + nr_numbers + nr_symbols
    random.shuffle(password_list)

    password = "".join(password_list)

    epassword.delete(0, END)
    epassword.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    name = ename.get()
    email = eemail.get()
    password = epassword.get()
    data = {
        name: {
            "Email": email,
            "Password": password
        }
    }
    if name != "" and email != "" and password != "":
        is_yes = messagebox.askyesno("Info","Data will be saved in data.txt\n\n       Want to save?")
        if is_yes:
            try:
                with open("./Password Generator/data.json", "r") as file:
                    # Read old data
                    json_data = json.load(file)
            except FileNotFoundError:
                # If file doesn't exist, start with the new data
                json_data = data
            else:
                # Update old data with new data
                json_data.update(data)

            finally:
                ename.delete(0, END)
                epassword.delete(0, END)
            with open("./Password Generator/data.json", "w") as file:
                #saving updated data
                json.dump(json_data, file, indent=4)
    else:
        messagebox.showerror("Error", "Some field are empty!")

def search_data():
    name = ename.get()
    try:
        with open("./Password Generator/data.json") as file:
            json_data = json.load(file)
            if name in json_data:
                messagebox.showinfo("Info", f"Name/website: {name}\nEmail: {json_data[name]['Email']}\nPassword: {json_data[name]['Password']}")
            else:
                messagebox.showerror("Error", f"Password has not generated for {name}")
    except FileNotFoundError:
        messagebox.showerror("Error", "File Not Found")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Generator")
window.config(padx=40,pady=20)

canvas = Canvas(window, width=200, height=200)
img = PhotoImage(file="./Password Generator/logo.png")
canvas.create_image(100,100,image=img)
canvas.grid(row=0, column=1)

name = Label(window,text="Name/Website:")
name.grid(row=1,column=0)
email = Label(window,text="Email:")
email.grid(row=2,column=0)
password = Label(window,text="Password:")
password.grid(row=3,column=0)

ename = Entry(window, width= 30)
ename.focus()
ename.grid(row=1, column=1, columnspan=2,sticky="w")
eemail = Entry(window, width=30)
eemail.grid(row=2, column=1,columnspan=2,sticky="w")
epassword = Entry(window, width=30)
epassword.grid(row=3,column=1,sticky="w")

generate = Button(window, text="Generate", width= 10, command=generate_password)
generate.grid(row=3,column=2,sticky="w")
add = Button(window, text="Add",width=40,command=save_data)
add.grid(row=4,column=1,columnspan=2,sticky="w")
search = Button(window, text="Search", width=10, command=search_data)
search.grid(row=1, column=2,sticky="w")

window.mainloop()