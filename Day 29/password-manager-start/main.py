# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    with open('data.txt', mode='a') as data:
        data.write(f'| {website.get()} | {email.get()} | {password.get()} | \n')

        website.delete(0, END)
        password.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *

window = Tk()
window.title('Password Manager')
window.config(padx=70, pady=70)

# Canvas for Logo
canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# Entry Fields
website = Entry(width=43)
website.focus()
website.grid(row=1, column=1, columnspan=2)

email = Entry(width=43)
email.insert(0, 'eyob@gmail.com')
email.grid(row=2, column=1, columnspan=2)

password = Entry(width=22)  # Adjust width so it fits with the button
password.grid(row=3, column=1, sticky="w")

# Labels
website_label = Label(text='Website:')
website_label.grid(column=0, row=1)

email_label = Label(text='Email/Username:')
email_label.grid(column=0, row=2)

password_label = Label(text='Password:')
password_label.grid(column=0, row=3)

# Buttons
generate_password = Button(text='Generate Password', width=15)
generate_password.grid(row=3, column=2)

add = Button(text='Add', width=40, command=save)
add.grid(row=4, column=1, columnspan=2)

window.mainloop()
