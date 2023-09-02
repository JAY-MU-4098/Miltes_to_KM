from tkinter import *


def get_answer():
    mile = float(entry.get())
    ans = mile * 1.609 
    answer_label.config(text=f"{ans}")


window = Tk()
window.title("Miles to KM convertor")
window.minsize(width=150, height=100)
window.config(padx=30, pady=20)

entry = Entry(width=10)
entry.grid(column=1, row=0)

miles_label = Label(text="Miles", font=("Times new roman", 10))
miles_label.grid(column=2, row=0)

is_equal_to_label = Label(text="is equal to", font=("Times new roman", 10))
is_equal_to_label.grid(column=0, row=1)

answer_label = Label(text=0, font=("Times new roman", 10))
answer_label.grid(column=1, row=1)

km_label = Label(text="KM", font=("Times new roman", 10))
km_label.grid(column=2, row=1)

button = Button(text="Calculate", command=get_answer)
button.grid(column=1, row=2)
window.mainloop()
