from tkinter import *

from numpy.ma.extras import row_stack

## window

window = Tk()
window.title('Miles to Km Converter')
window.minsize(width=600, height=400)
window.config(padx=180,pady=100)

## Entry
#side
entry = Entry(width=20)
entry.grid(column=1, row=0)
entry.config()

# function
def calculater():
    try:
        value = entry.get()
        miles = float(value)
        kilometers = miles * 1.60934
        answer.config(text=f"{kilometers:.2f} km")
    except ValueError:
        answer.config(text="Invalid input")

## Label

label = Label(text='Miles', font=('Aries', 10, 'bold'))
label.grid(column=3, row=0)
label.config(padx=10)

## Second text label

label_2 = Label(text='is equal to ', font=('Aries', 10, 'bold'))
label_2.grid(column = 0, row = 1)
label_2.config(padx=10)

## third Km label

label_3 = Label(text='Km', font=('Aries', 10, 'bold'))
label_3.grid(column = 3, row = 1)
label_3.config(padx=2)

## Answer

answer = Label(text='0', font=('Italic', 15, 'bold'))
answer.grid(column=1, row = 1)


## Button

button = Button(text='Calculate', command=calculater)
button.grid(column=1, row=3)










window.mainloop()