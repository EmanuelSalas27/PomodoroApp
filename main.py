import tkinter

COLOR_PRIMARY = '#302b27'
COLOR_SECONDARY = '#F72541'
COLOR_TERTIARY = '#28965A'

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0
timer = None

window = tkinter.Tk()
window.title('Pomodoro APP')
window.geometry('300x300')
window.config(bg=COLOR_PRIMARY)
window.resizable(False, False)


def start_timer():
    start_button['state'] = 'disabled'
    global reps
    reps += 1
    if reps % 2 == 0:
        window.attributes('-topmost', True)
        change_colors(COLOR_TERTIARY)
        title_label['text'] = 'BREAK TIME'
        count_down(SHORT_BREAK_MIN)
        window.attributes('-topmost', False)
    elif reps >= 8:
        change_colors(COLOR_TERTIARY)
        title_label['text'] = 'BREAK TIME'
        count_down(LONG_BREAK_MIN)
        reps = 0
        if len(check_marks['text']) < 8:
            check_marks['text'] += '★'
        start_button['state'] = 'active'
        reset_timer()
    else:
        window.attributes('-topmost', False)
        change_colors(COLOR_SECONDARY)
        title_label['text'] = 'WORK TIME'
        count_down(WORK_MIN)


def count_down(count):
    if count >= 0:
        global timer
        timer = window.after(100, count_down, count-1)
        time_label['text'] = count
    else:
        start_timer()


def reset_timer():
    global reps
    reps = 0
    if timer is not None:
        window.after_cancel(timer)
    time_label['text'] = '00'
    title_label['text'] = 'PRESS START'
    start_button['state'] = 'active'
    change_colors(COLOR_PRIMARY)


def change_colors(new_color):
    title_label['bg'] = new_color
    time_label['bg'] = new_color
    start_button['bg'] = new_color
    reset_button['bg'] = new_color
    check_marks['bg'] = new_color
    window['bg'] = new_color


title_label = tkinter.Label(text='PRESS START', bg=COLOR_PRIMARY, fg='White', font=("Courier", 20), anchor='center')
title_label.pack(pady=50)

time_label = tkinter.Label(text='00', bg=COLOR_PRIMARY, font=("Courier", 44), fg='White')
time_label.pack()

start_button = tkinter.Button(text='Start', bg=COLOR_PRIMARY, fg='White', borderwidth=0, command=start_timer)
start_button.place(x=10, y=260)

reset_button = tkinter.Button(text='Reset', bg=COLOR_PRIMARY, fg='White', borderwidth=0, command=reset_timer)
reset_button.place(x=220, y=260)

check_marks = tkinter.Label(text='', bg=COLOR_PRIMARY, fg='White', borderwidth=0)
check_marks.place(x=100, y=265)

window.mainloop()
