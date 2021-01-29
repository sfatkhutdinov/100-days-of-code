from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    character_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    symbol_list = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    number_list = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = character_list + symbol_list + number_list
    random.shuffle(password_list)

    password = ''.join(password_list)
    password_entry.insert(END, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title='Oops', message="Please don't leave any field empty!")
        is_ok = False
    else:
        is_ok = messagebox.askokcancel(title=website, message=f'These are the details entered:'
                                                              f'\nEmail: {email}'
                                                              f'\nPassword: {password}'
                                                              f'\nIs it ok to save?')
    if is_ok:
        with open('data.txt', 'a') as data:
            entry = f'{website} | {email} | {password}\n'
            data.write(entry)
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manger')
window.config(padx=50, pady=50)

lock_img = PhotoImage(file='logo.png')
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

website_label = Label(text='Website:')
website_label.grid(column=0, row=1)
website_entry = Entry(width=40)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)

username_label = Label(text='Email/Username:')
username_label.grid(column=0, row=2)
username_entry = Entry(width=40)
username_entry.insert(END, 'stanislav@mail.com')
username_entry.grid(column=1, row=2, columnspan=2)

password_label = Label(text='Password:')
password_label.grid(column=0, row=3)
password_entry = Entry(width=22)
password_entry.grid(column=1, row=3)

generate_pass_btn = Button(text='Generate Password', command=generate_password)
generate_pass_btn.grid(column=2, row=3)

add_btn = Button(text='Add', width=38, command=save)
add_btn.grid(column=1, row=4, columnspan=2)

window.mainloop()
