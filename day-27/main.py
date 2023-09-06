from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)
# Label

my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.grid(row=1, column=1)
my_label["text"] = "New text"
my_label.config(text="Next Text", pady=50, padx=50)

# Button


def button_clicked():
    print("I got clicked")
    s = input.get()
    my_label.config(text=s)


button = Button(text="Click Me", command=button_clicked)
button.grid(row=2, column=2)

# Entry

input = Entry(width=10)
input.grid(row=3, column=4)

second_button = Button(text="New Button")
second_button.grid(row=1, column=3)

window.mainloop()
