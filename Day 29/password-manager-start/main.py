from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
               'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    # first clear the space
    password.delete(0, END)
    generated_password = ''.join(password_list)
    password.insert(0, generated_password)
    pyperclip.copy(generated_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
   website_entry = website.get()
   email_entry = email.get()
   password_entry = password.get()
   if len(website_entry) == 0 or len(website_entry) == 0 or len(password_entry) == 0:
       messagebox.showinfo(title='Oops!', message="Please don't leave any fields empty!!!")
   else:
       is_it_ok = messagebox.askquestion(title=website_entry, message=f'These are the detail entered:         '
                                                           f'\nEmail: {email_entry} '
                                                           f'\nPassword: {password_entry} '
                                                           f'\nIt is ok to save ? ')
       if is_it_ok == 'yes':
           with open('data.txt', mode='a') as data:
               data.write(f'| {website_entry} | {email_entry} | {password_entry} | \n')

               website.delete(0, END)
               password.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

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

password = Entry(width=22)
password.grid(row=3, column=1, sticky="w")

# Labels
website_label = Label(text='Website:')
website_label.grid(column=0, row=1)

email_label = Label(text='Email/Username:')
email_label.grid(column=0, row=2)

password_label = Label(text='Password:')
password_label.grid(column=0, row=3)

# Buttons
generate_password = Button(text='Generate Password', width=15, command=generate_password)
generate_password.grid(row=3, column=2)

add = Button(text='Add', width=40, command=save)
add.grid(row=4, column=1, columnspan=2)

window.mainloop()
