from tkinter import *

window = Tk()
window.title("My GUI Program")
window.minsize(width=500 , height=500)
window.config(padx=20 ,pady=20)

my_label = Label(text="Here is Label", font=("Arial" , 24 , "bold"))
my_label.grid(row=1,column=1)
my_label['text'] = "New Text"

def btn():
    NEW_TEXT = input.get()
    my_label.config(text=NEW_TEXT)
button = Button(text="click here" , command=btn)
button.grid(row=1 , column=3)
New_button = Button(text="click here" , command=btn)
New_button.grid(row=2 , column=2)
input = Entry()
input.grid(row=3 , column=4)

















window.mainloop()