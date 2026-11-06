from tkinter import *
from tkinter import messagebox
import os

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = web_input.get()
    email = mail_input.get()
    password = pass_input.get()

    if not website or not email or not password:
        messagebox.showwarning(
            "Error",
            "Please don't leave any fields empty!"
        )
        return

    
    do = messagebox.askokcancel(title=website , message=f"These are the details entered: \nEmail: {email} \n Password: {password} \n Is it ok to save?")
    if do:
        file_path = os.path.join(os.path.dirname(__file__), "data.txt")


    with open(file_path, "a") as file:
        file.write(
            f"Website: {website} | Email: {email} | Password: {password}\n"
        )

    web_input.delete(0, END)
    pass_input.delete(0, END)

    

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
web_input.focus()

mail = Label(text="Email/Username:", **label_config)
mail.grid(row=3, column=1)

mail_input = Entry(width=35, bg="white", fg="black")
mail_input.grid(row=3, column=2, columnspan=2)
mail_input.insert(0 , "@email.com")

pasw = Label(text="Password:", **label_config)
pasw.grid(row=4, column=1)

pass_input = Entry(width=21, bg="white", fg="black")
pass_input.grid(row=4, column=2)

generate_button = Button(text="Generate Password")
generate_button.grid(row=4, column=3)

add_button = Button(
    text="Add",
    width=36,
    command=save_password
)
add_button.grid(row=5, column=2, columnspan=2)

window.mainloop()