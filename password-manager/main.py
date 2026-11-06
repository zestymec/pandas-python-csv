# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

import tkinter as tk
# from pathlib import Path

window = tk.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = tk.Canvas(window, width=200, height=200)
logo_path = 'password-manager/logo.png'
logo = tk.PhotoImage(file=logo_path)
canvas.create_image(100, 100, image=logo)
canvas.pack()

window.mainloop()