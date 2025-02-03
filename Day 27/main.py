from tkinter import *

window = Tk()
window.title('my first GUI program')
window.minsize(width=700,height=500)
##pad
window.config(padx=100,pady=100)

## LABEL
my_label = Label(text='I am a label', font=('Arial', 24, 'bold'))
my_label.config(text='new text')
my_label.grid(column=0, row=0)
##pad
my_label.config(padx=50,pady=50)


## Button
def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)

button = Button(text='Click me', command=button_clicked)
button.grid(column=1, row=1)
## Button 2

button_2 = Button(text='Click me', command=button_clicked)
button_2.grid(column=2, row=0)
## Input

input = Entry(width=20)
input.grid(column=3, row=2)
##print(input.get()) it doesnt work



window.mainloop()
