import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    count_down(1 * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'

    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')

    if count > 0:
        window.after(1000, count_down, count - 1)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomodora')
window.config(padx=100,pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224,  bg=YELLOW, highlightthickness=0)
time_image = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=time_image)
timer_text = canvas.create_text(100,140, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=2, row=2)


## Label

titel_label = Label(text='Timer', font=(FONT_NAME, 50), bg=YELLOW, fg=GREEN)
label_checkmark = Label(text='✔', font=(FONT_NAME, 35, 'italic'), bg=YELLOW)


titel_label.grid(column=2, row=0)
label_checkmark.grid(column=2, row=4)

## Button

start_btn = Button(text='Start', highlightthickness=0, command=start_timer)
reset_btn = Button(text='Reset', highlightthickness=0)

start_btn.grid(column=1, row=3)
reset_btn.grid(column=3, row=3)


window.mainloop()