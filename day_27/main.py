import tkinter

window = tkinter.Tk()
window.title("My GUI Program")
window.minsize(width=500 , height=500)

my_label = tkinter.Label(text="Here is Label", font=("Arial" , 24 , "bold"))
my_label.pack(side= "left")










window.mainloop()