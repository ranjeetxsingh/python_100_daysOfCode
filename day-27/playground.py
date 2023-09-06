from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(height=280, width=420)
window.config(padx=25, pady=25)

my_label = Label(text="is equal to", font=("Arial", 12, "bold"))
my_label.grid(row=2, column=1, pady=10, padx=10)

input = Entry(width=10)
input.grid(row=1, column=2, pady=10, padx=10)

miles_label = Label(text="Miles", font=("Arial", 12, "bold"))
miles_label.grid(row=1, column=3, pady=10, padx=10)

ans_label = Label(text=0, font=("Arial", 12, "bold"))
ans_label.grid(row=2, column=2, pady=10, padx=10)

km_label = Label(text="Km", font=("Arial", 12, "bold"))
km_label.grid(row=2, column=3, pady=10, padx=10)


def calculate():
    value_in_miles = input.get()
    value_in_miles = int(value_in_miles)
    value_in_km = value_in_miles*1.6
    ans_label.config(text=value_in_km)


button = Button(text="Calculate", command=calculate)
button.grid(row=3, column=2)
window.mainloop()
