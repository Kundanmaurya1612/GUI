from tkinter import Tk, Label, Button, Canvas, PhotoImage
import math

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    count_minute = math.floor(count / 60)
    count_second = count % 60

    if count_second < 10:
        count_second = f"0{count_second}"

    canvas.itemconfig(clock, text=f"{count_minute}:{count_second}")
    if count > 0:
        global TIMER
        TIMER = window.after(1000, countdown, count-1)
    else:
        global CHECK
        CHECK +=1

        window.attributes('-topmost', True)
        check_mark.config(text=check_mark['text']+"✔️")
        status.config(text="Break",fg=GREEN)
        if CHECK == 4:
            window.attributes('-topmost', False)
            break_session(20*60)

        else:
            window.attributes('-topmost', False)
            break_session(5)  

# ---------------------------- Break MECHANISM ------------------------------- #
def break_session(count):
    count_minute = math.floor(count / 60)
    count_second = count % 60

    if count_second < 10:
        count_second = f"0{count_second}"

    canvas.itemconfig(clock, text=f"{count_minute}:{count_second}")
    if count > 0:
        global TIMER
        TIMER = window.after(1000, break_session, count-1)
    else:
        window.attributes('-topmost', True)
        status.config(text="FOCUS",fg=PINK)
        window.attributes('-topmost', False)
        countdown(10)

# ---------------------------- 5 sec ------------------------------- #
def prepare(count):
    canvas.itemconfig(clock, text=f"{count}")
    if count > 1:
        status.config(text="FOCUS", fg=PINK)
        global TIMER
        TIMER = window.after(1000, prepare, count-1)
    else:
        countdown(10)

# ---------------------------- Initializer ------------------------------- #
def start_countdown():
    prepare(5)

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_countdown():
    window.after_cancel(TIMER)
    canvas.itemconfig(clock, text="00:00")
    check_mark.config(text='')
    status.config(text="Timer", fg=GREEN)
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#F26849"
RED = "#e7305b"
GREEN = "#379B46"
YELLOW = "#f7f5dd"
NEW = "#e7b57f"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK = 0
TIMER = ""

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()

window.title("Pomodoro")
window.config(padx=100, pady=50, background=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
clock = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 32, "bold"))
canvas.grid(row=1, column=1)
status = Label(window, text="Timer", fg=GREEN, bg=YELLOW, font=("Courier", 34, "bold"))
status.grid(row=0, column=1)

start_button = Button(window, text="Start",bg=NEW,activebackground=NEW, command=start_countdown,fg="#1F1F1F", font=("courier", 15, "bold")).grid(row=2, column=0)

reset_button = Button(window, text="Reset",bg=NEW,activebackground=NEW,command=reset_countdown,fg="#1F1F1F", font=("courier", 15, "bold")).grid(row=2, column=2)

check_mark = Label(window, text="",bg=YELLOW, fg=GREEN)
check_mark.grid(row=4,column=1)





window.mainloop()