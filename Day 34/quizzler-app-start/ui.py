import tkinter
from tkinter import Canvas, PhotoImage, Label, Button

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title('Quizzler')
        self.window.config(pady=20,padx=20,bg=THEME_COLOR)


        self.canvas = Canvas(width=300,height=250,bg='white')
        self.question_text = self.canvas.create_text(
            150,125,
            text='hello',
            fill=THEME_COLOR,
            font=('Arial', 10, 'italic')
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)


        self.score = Label(text='Score: 0', fg='white', bg=THEME_COLOR)
        self.score.grid(column=1, row=0)

        true_image = PhotoImage(file='images/true.png')
        self.true_button = Button(image=true_image, highlightthickness=0)
        self.true_button.grid(column=0, row=2)

        false_image = PhotoImage(file='images/false.png')
        self.false_button = Button(image=false_image, highlightthickness=0)
        self.false_button.grid(column=1, row=2)

        self.window.mainloop()
