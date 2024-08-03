from tkinter import *
import math
#from playsound import playsound
#bugs in checkmarks
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 10
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN)
    checkmark_label.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    reps += 1
    if reps % 8 == 0:
        playsound(sound="sounds/long break start.wav")
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)

    elif reps % 2 == 0:
        playsound(sound="sounds/short break start.wav")
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)

    else:
        playsound(sound="sounds/work start.mp3")
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)


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
        marks = ""
        for i in range(math.floor(reps / 2)):
            marks += "✔"
        checkmark_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
# window.geometry("500x500")
window.config(padx=100, pady=50, bg=YELLOW)

######
canvas = Canvas(window, width=220, height=230, bg=YELLOW, highlightthickness=0)

tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(110, 115, image=tomato_img)

timer_text = canvas.create_text(110, 135, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)
#######

timer_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50))
timer_label.grid(column=1, row=0)

checkmark_label = Label(fg=GREEN, bg=YELLOW)
checkmark_label.grid(column=1, row=3)

start_button = Button(text="Start", font=("Ariel", 10), command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", font=("Ariel", 10), command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()
