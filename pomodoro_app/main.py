from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0  # FIX 1: reps variable global level par initialize kiya
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text , text="00:00")
    my_label.config(text="Timer")
    checmark.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60  # FIX 2: staticmethod ki jagah SHORT_BREAK_MIN lagaya
    long_break_sec = LONG_BREAK_MIN * 60

    # FIX 3: Pehle yahan extra count_down(5 * 60) tha, use hata diya.

    if reps % 8 == 0:
        count_down(long_break_sec)
        my_label.config(text="long-Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        my_label.config(text="short-Break", fg=PINK)
    else:
        count_down(work_sec)
        my_label.config(text="Timer", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(reps/2)):
            mark += "✓"

        checmark.config(Text=mark)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg=YELLOW)

my_label = Label(text="Timer", font=("Arial", 54, "bold"), fg=GREEN, bg=YELLOW)
my_label.grid(row=1, column=2)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(
    file="/Users/apple/umeraziz/pandas-python-csv/pomodoro_app/tomato.png"
)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(
    100, 130.0, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)
canvas.grid(row=2, column=2)

startbutton = Button(
    text="Start", bg=YELLOW, highlightbackground=YELLOW, command=start_timer
)
startbutton.grid(row=3, column=1)

resetbutton = Button(text="Reset", bg=YELLOW, highlightbackground=YELLOW , command=reset_timer)
resetbutton.grid(row=3, column=3)

checmark = Label(text="", fg=GREEN, bg=YELLOW)
checmark.grid(row=4, column=2)

window.mainloop()