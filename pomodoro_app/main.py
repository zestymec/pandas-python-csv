from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    WORK_MIN * 60
    count_down(5 * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
# import time
# count = 23
# while True:
#     time.sleep(1)
#     count-=1
def count_down(count):

    count_min = math.floor(count/60)
    count_sec = count % 60

    canvas.itemconfig(timer_text , text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro App")
my_label = Label(text="Timer", font=("Arial", 54, "bold"), fg=GREEN, bg=YELLOW)
my_label.grid(row=1, column=2)
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(
    file="/Users/apple/umeraziz/pandas-python-csv/pomodoro_app/tomato.png"
)


canvas.create_image(100, 112, image=tomato_img)

timer_text = canvas.create_text(100, 130.0, text=0, fill="white", font=(FONT_NAME, 35, "bold"))

canvas.grid(row=2, column=2)

startbutton = Button(text="Start", bg=YELLOW, highlightbackground=YELLOW , command=start_timer)
startbutton.grid(row=3, column=1)
resetbutton = Button(text="Reset", bg=YELLOW, highlightbackground=YELLOW)
resetbutton.grid(row=3, column=3)
checmark = Label(text="✓", fg=GREEN, bg=YELLOW)
checmark.grid(row=4, column=2)

window.mainloop()
