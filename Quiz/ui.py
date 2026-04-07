from tkinter import * # type: ignore
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizeInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        wrong_image = PhotoImage(file="./Quiz/images/false.png")
        right_image = PhotoImage(file="./Quiz/images/true.png")

        self.window.config(padx=20, pady=20,bg=THEME_COLOR)
        self.score = Label(self.window, text=f"Score: {quiz.score}", bg= THEME_COLOR, fg="white", font=("Ariel", 15, "normal"))
        self.score.grid(row=0, column=1,pady=10)

        self.canvas = Canvas(self.window,highlightthickness=0,height=250,width=300,bg="white")
        self.question_text = self.canvas.create_text(150,125,text="",font=("Ariel", 20, "italic"), width= 280)
        self.canvas.grid(row=1, column=0,columnspan=2)

        self.wrong = Button(self.window, image=wrong_image, command=self.button_wrong)
        self.wrong.grid(row=2, column=0)
        self.right = Button(self.window, image=right_image, command=self.button_right)
        self.right.grid(row=2, column=1, pady=30)

        self.get_next()

        self.window.mainloop()
        
    def get_next(self): 
        self.canvas.config(bg="white")
        quiz_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=quiz_text)
        

    def button_wrong(self):
        result = self.quiz.check_answer("false")
        if result:
            self.canvas.config(bg="#4EA965")
        else:
            self.canvas.config(bg="#A11818")
        self.score.config(text=f"Score: {self.quiz.score}")
        self.window.after(2000,self.get_next)
        

    def button_right(self):
        result = self.quiz.check_answer("true")
        if result:
            self.canvas.config(bg="#4EA965")
        else:
            self.canvas.config(bg="#A11818")
        self.score.config(text=f"Score: {self.quiz.score}")
        self.window.after(2000,self.get_next)

        
