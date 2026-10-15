from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=300, height=150)
window.config(padx=20, pady=20)

input_miles = Entry(width=10)
input_miles.grid(row=0, column=1)

label_miles = Label(text="Miles")
label_miles.grid(row=0, column=2)

label_is_equal = Label(text="is equal to")
label_is_equal.grid(row=1, column=0)

label_result = Label(text="0")
label_result.grid(row=1, column=1)

label_km = Label(text="Km")
label_km.grid(row=1, column=2)

def calculate_km():
    miles = float(input_miles.get())
    km = round(miles * 1.60934, 2)
    label_result.config(text=str(km))

button = Button(text="Calculate", command=calculate_km)
button.grid(row=2, column=1)

window.mainloop()