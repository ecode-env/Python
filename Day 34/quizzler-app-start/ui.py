import tkinter
from tkinter import Canvas, PhotoImage, Label, Button
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_interface: QuizBrain):
        self.quiz = quiz_interface
        self.window = tkinter.Tk()
        self.window.title('Quizzler')
        self.window.config(pady=25,padx=25,bg=THEME_COLOR)


        self.canvas = Canvas(width=350,height=300,bg='white')
        self.question_text = self.canvas.create_text(
            150,125,
            width=280,
            text='hello',
            fill=THEME_COLOR,
            font=('Arial', 15, 'italic')
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)


        self.score = Label(text='Score: 0', fg='white', bg=THEME_COLOR)
        self.score.grid(column=1, row=0)

        true_image = PhotoImage(file='images/true.png')
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(column=0, row=2)

        false_image = PhotoImage(file='images/false.png')
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.true_pressed)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()
    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text='You have reached end of quiz.')
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def true_pressed(self):
        self.get_feedback(self.quiz.check_answer('True'))
    def false_pressed(self):
        self.get_feedback(self.quiz.check_answer('False'))
    def get_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000,func=self.get_next_question)
