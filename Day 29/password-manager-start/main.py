# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *

window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)

# Canvas for Logo
canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# Entry
website = Entry(width=35)
website.grid(column=1, row=1, columnspan=2)

email = Entry(width=35)
email.grid(column=1, row=2, columnspan=2)

password = Entry(width=21)
password.grid(column=1, row=3)

## Label

website_label = Label(text='Website:')
website_label.grid(column=0, row=1)


email_label = Label(text='Email/Username:')
email_label .grid(column=0, row=2)


password_label = Label(text='Password:')
password_label.grid(column=0, row=3)


## Button

generate_password = Button(text='Generate Password', width=12)
generate_password.grid(column=2, row=3)

add = Button(text='Add', width=36)
add.grid(column=1,row=4, columnspan=2)





window.mainloop()
