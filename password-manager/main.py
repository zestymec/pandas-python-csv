from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="white")

canvas = Canvas(
    window,
    width=200,
    height=200,
    bg="white",
    highlightthickness=0,
    bd=0
)
logo = PhotoImage(file="password-manager/logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=1, column=2)

label_config = {"bg": "white", "fg": "black"}

web = Label(text="Website:", **label_config)
web.grid(row=2, column=1)

web_input = Entry(width=35, bg="white", fg="black")
web_input.grid(row=2, column=2, columnspan=2)

mail = Label(text="Email/Username:", **label_config)
mail.grid(row=3, column=1)

mail_input = Entry(width=35, bg="white", fg="black")
mail_input.grid(row=3, column=2, columnspan=2)

pasw = Label(text="Password:", **label_config)
pasw.grid(row=4, column=1)

pass_input = Entry(width=21, bg="white", fg="black")
pass_input.grid(row=4, column=2)

generate_button = Button(text="Generate Password")
generate_button.grid(row=4, column=3)

add_button = Button(text="Add", width=36)
add_button.grid(row=5, column=2, columnspan=2)

window.mainloop()