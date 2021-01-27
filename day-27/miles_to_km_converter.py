from tkinter import *

window = Tk()
window.title("Miles to Kilometers Converter")
# window.minsize(width=500, height=300)
window.config(padx=50, pady=50)

label = Label(text='is equal to')
label.grid(column=0, row=1)

mile_label = Label(text='Miles')
mile_label.grid(column=2, row=0)

km_label = Label(text='Km')
km_label.grid(column=2, row=1)

result_label = Label(text='0')
result_label.grid(column=1, row=1)

entry = Entry(width=8)
# Add some text to begin with
entry.insert(END, string="0")
entry.grid(column=1, row=0)


# Buttons
def calculate():
    user_input = float(entry.get())
    result = round(user_input * 1.609)
    result_label.config(text=result)


# calls action() when pressed
button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

window.mainloop()
