import os
import secrets
import string
import tkinter as tk
from tkinter import messagebox, ttk
import json 


BACKGROUND = "#101827"
SURFACE = "#182235"
SURFACE_ALT = "#202d43"
TEXT = "#f4f7fb"
MUTED = "#9aa9bd"
ACCENT = "#6c8cff"
ACCENT_HOVER = "#829cff"
SUCCESS = "#5ed6a0"
ERROR = "#ff8c8c"


def generate_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(secrets.choice(characters) for _ in range(16))
    password_var.set(password)
    password_entry.select_range(0, tk.END)
    password_entry.focus_set()
    set_status("Secure password generated", SUCCESS)


def copy_password():
    password = password_var.get()
    if not password:
        set_status("Generate a password before copying", ERROR)
        return

    window.clipboard_clear()
    window.clipboard_append(password)
    window.update()
    set_status("Password copied to clipboard", SUCCESS)


def save_password():
    website = website_var.get().strip()
    email = email_var.get().strip()
    password = password_var.get()

    if not website or not email or not password:
        set_status("Complete all fields before saving", ERROR)
        messagebox.showwarning("Missing details", "Please complete all fields before saving.")
        return

    confirmed = messagebox.askyesno(
        "Confirm save",
        f"Save credentials for {website}?\n\nUsername: {email}",
        parent=window,
    )
    if not confirmed:
        return
    new_data = {
        website:{
            "email": email ,
            "password": password,
    }
    }
    file_path = os.path.join(os.path.dirname(__file__), "data.json")
    try:
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {}

        data.update(new_data)

        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    except (OSError, json.JSONDecodeError) as error:
        set_status("Unable to save credentials", ERROR)
        messagebox.showerror(
            "Save failed",
            f"Could not save credentials:\n{error}",
            parent=window,
        )
        return

    website_var.set("")
    password_var.set("")
    website_entry.focus_set()
    set_status("Credentials saved successfully", SUCCESS)


def toggle_password():
    password_entry.configure(show="" if password_entry.cget("show") else "•")
    reveal_button.configure(text="Hide" if password_entry.cget("show") == "" else "Show")


def set_status(message, color=TEXT):
    status_label.configure(text=message, foreground=color)
    window.after(4000, lambda: status_label.configure(text="Ready to secure your accounts", foreground=MUTED))


def search_password():
    website = search_var.get().strip()

    if not website:
        messagebox.showwarning(
            "Search",
            "Please enter a website name.",
            parent=window,
        )
        return

    file_path = os.path.join(os.path.dirname(__file__), "data.json")

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}
    except OSError as error:
        messagebox.showerror("Search failed", str(error), parent=window)
        return

    account = data.get(website)

    if account is None:
        messagebox.showwarning(
            "Not found",
            f"No saved login found for {website}.",
            parent=window,
        )
        return

    messagebox.askyesno(
        "Saved credentials",
        f"Website: {website}\n\n"
        f"Email: {account['email']}\n"
        f"Password: {account['password']}\n\n"
        "Do you want to close this message?",
        parent=window,
    )


window = tk.Tk()
window.title("Vault • Password Manager")
window.configure(bg=BACKGROUND)
window.resizable(False, False)

style = ttk.Style(window)
style.theme_use("clam")
style.configure(
    "App.TButton",
    background=ACCENT,
    foreground=TEXT,
    borderwidth=0,
    padding=(14, 10),
    font=("Helvetica", 10, "bold"),
)
style.map("App.TButton", background=[("active", ACCENT_HOVER)])
style.configure(
    "Secondary.TButton",
    background=SURFACE_ALT,
    foreground=TEXT,
    borderwidth=0,
    padding=(12, 9),
    font=("Helvetica", 10, "bold"),
)
style.map("Secondary.TButton", background=[("active", "#2c3b55")])
style.configure(
    "Field.TEntry",
    fieldbackground=SURFACE_ALT,
    foreground=TEXT,
    insertcolor=TEXT,
    borderwidth=0,
    padding=10,
    font=("Helvetica", 11),
)

website_var = tk.StringVar()
email_var = tk.StringVar(value="@email.com")
password_var = tk.StringVar()
search_var = tk.StringVar()

outer = tk.Frame(window, bg=BACKGROUND, padx=34, pady=30)
outer.pack()

header = tk.Frame(outer, bg=BACKGROUND)
header.pack(fill="x", pady=(0, 24))

logo = tk.PhotoImage(file=os.path.join(os.path.dirname(__file__), "logo.png"))
logo = logo.subsample(max(1, logo.width() // 72))
tk.Label(header, image=logo, bg=BACKGROUND).pack(side="left", padx=(0, 16))

heading = tk.Frame(header, bg=BACKGROUND)
heading.pack(side="left")
tk.Label(
    heading,
    text="Your digital vault",
    bg=BACKGROUND,
    fg=TEXT,
    font=("Helvetica", 23, "bold"),
).pack(anchor="w")
tk.Label(
    heading,
    text="Store and generate credentials with confidence.",
    bg=BACKGROUND,
    fg=MUTED,
    font=("Helvetica", 10),
).pack(anchor="w", pady=(5, 0))

card = tk.Frame(outer, bg=SURFACE, padx=24, pady=24)
card.pack(fill="x")

tk.Label(
    card,
    text="ADD NEW LOGIN",
    bg=SURFACE,
    fg=ACCENT_HOVER,
    font=("Helvetica", 9, "bold"),
).grid(row=0, column=0, columnspan=3, sticky="w", pady=(0, 18))

def add_field(label, variable, row):
    tk.Label(
        card,
        text=label,
        bg=SURFACE,
        fg=MUTED,
        font=("Helvetica", 9, "bold"),
    ).grid(row=row, column=0, sticky="w", pady=(0, 7))
    entry = ttk.Entry(card, textvariable=variable, style="Field.TEntry", width=39)
    entry.grid(row=row + 1, column=0, columnspan=3, sticky="ew", pady=(0, 17))
    return entry


website_entry = add_field("WEBSITE OR APP", website_var, 1)
email_entry = add_field("USERNAME OR EMAIL", email_var, 3)

tk.Label(
    card,
    text="PASSWORD",
    bg=SURFACE,
    fg=MUTED,
    font=("Helvetica", 9, "bold"),
).grid(row=5, column=0, sticky="w", pady=(0, 7))

password_entry = ttk.Entry(card, textvariable=password_var, style="Field.TEntry", width=25, show="*")
password_entry.grid(row=6, column=0, sticky="ew", pady=(0, 20))

reveal_button = ttk.Button(card, text="Show", style="Secondary.TButton", command=toggle_password)
reveal_button.grid(row=6, column=1, padx=(8, 6), pady=(0, 20))
ttk.Button(card, text="Generate", style="Secondary.TButton", command=generate_password).grid(
    row=6, column=2, pady=(0, 20)
)

ttk.Button(card, text="Copy", style="Secondary.TButton", command=copy_password).grid(
    row=7, column=0, columnspan=3, sticky="ew", pady=(0, 10)
)
ttk.Button(card, text="Save credential", style="App.TButton", command=save_password).grid(
    row=8, column=0, columnspan=3, sticky="ew"
)

search_frame = tk.Frame(outer, bg=BACKGROUND)
search_frame.pack(fill="x", pady=(10, 0))

tk.Label(
    search_frame,
    text="SEARCH LOGIN",
    bg=BACKGROUND,
    fg=TEXT,
    font=("Helvetica", 10, "bold"),
).pack(side="left", anchor="w")

search_entry = ttk.Entry(search_frame, textvariable=search_var, style="Field.TEntry", width=30)
search_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))

ttk.Button(search_frame, text="Search", style="App.TButton", command=search_password).pack(side="left")

status_label = tk.Label(
    outer,
    text="Ready to secure your accounts",
    bg=BACKGROUND,
    fg=MUTED,
    font=("Helvetica", 9),
)
status_label.pack(pady=(15, 0))

website_entry.focus_set()
window.bind("<Return>", lambda event: save_password())
window.mainloop()
