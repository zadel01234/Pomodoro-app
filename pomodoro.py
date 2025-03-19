import math
from tkinter import *
import time

"""Imported Modules"""

# time.sleep(5)
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25 * 60
SHORT_BREAK_MIN = 5 * 60
LONG_BREAK_MIN = 20 * 60
reps = 0
my_timer = None



# ---------------------------- TIMER RESET ------------------------------- #
def reset_time():
    root.after_cancel(my_timer)
    canvas.itemconfig(timer_text, text="00:00")
    mark = ""
    check_marks.config(text=mark)
    Timer.config(text="Timer", fg=GREEN)
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN)
        Timer.config(text= "Long Break", fg = RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN)
        Timer.config(text="Short Break", fg=PINK)
    else:
        count_down(WORK_MIN)
        Timer.config(text="Work", fg=GREEN)





# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_minutes = math.floor(count/60)
    count_seconds = count % 60
    if count_seconds == 0 or count_seconds < 10:
        count_seconds = f"0{count%60}"


    canvas.itemconfig(timer_text, text = f"{count_minutes}:{count_seconds}")
    print(count)
    if count > 0:
        global my_timer
        my_timer = root.after(1000, count_down, count-1)
    else:
        start_timer()
        mark = ""
        for i in range( math.floor(reps / 2)):
            mark += "✔️"
        check_marks.config( text= mark)


# ---------------------------- UI SETUP ------------------------------- #
root = Tk()
root.title("The Pomodoro App")
root.config(padx=100, pady=50, bg = YELLOW)
# root.minsize(width=600, height=500)


xim = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg = YELLOW, highlightthickness = 0)
canvas.create_image(100,112,image = xim )
timer_text = canvas.create_text(100,130, text="00:00", font = (FONT_NAME,35, "bold"), fill = "white")
canvas.grid(row = 1, column = 1)




Timer = Label(text="Timer", fg = GREEN,bg = YELLOW, font = (FONT_NAME,50))
Timer.grid(row = 0, column= 1)

start = Button(text="start", highlightthickness = 0, width=10, height=2, command=start_timer)
start.grid(row = 2, column= 0)


reset = Button(text="reset", highlightthickness = 0, width=10, height=2, command=reset_time)
reset.grid(row = 2, column= 2)

check_marks = Label( fg = GREEN, bg = YELLOW)
check_marks.grid(row = 3, column = 1)





root.mainloop()