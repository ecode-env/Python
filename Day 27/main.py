from tkinter import *

window = Tk()
window.title('my first GUI program')
window.minsize(width=500,height=300)

## LABEL


my_label = Label(text='I am a label', font=('Arial', 24, 'bold'))
my_label.pack()

my_label['text'] = 'new text'
my_label.config(text='new text')


## Button
def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)

button = Button(text='Click me', command=button_clicked)
button.pack()

## Input

input = Entry(width=20)
input.pack()
##print(input.get()) it doesnt work



window.mainloop()
