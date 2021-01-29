from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manger')
window.config(padx=20, pady=20)

lock_img = PhotoImage(file='logo.png')
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=lock_img)
canvas.pack()

window.mainloop()
