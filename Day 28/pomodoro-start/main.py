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
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(str(timer))
    # reset canvas text
    canvas.itemconfig(timer_text, text='00:00')
    # reset label
    titel_label.config(text='Timer', fg=GREEN)
    # reset checkmarks
    label_checkmark.config(text=' ')




# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps +=1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 60:
        titel_label.config(text='Break', fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        titel_label.config(text='Break', fg=PINK)
        count_down(short_break_sec)
    else:
        titel_label.config(text='Work', fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'

    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ''
        for _ in range(math.floor(reps/2)):
            mark +='✔'
        label_checkmark.config(text=mark)

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
label_checkmark = Label(font=(FONT_NAME, 35, 'italic'), bg=YELLOW)


titel_label.grid(column=2, row=0)
label_checkmark.grid(column=2, row=4)

## Button

start_btn = Button(text='Start', highlightthickness=0, command=start_timer)
reset_btn = Button(text='Reset', highlightthickness=0, command=reset_timer)

start_btn.grid(column=1, row=3)
reset_btn.grid(column=3, row=3)


window.mainloop()