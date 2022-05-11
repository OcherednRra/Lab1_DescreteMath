import tkinter as tk
from window1 import student_info_window
from window2 import full_solution_window
from window3 import solution_window
from window4 import set_problem
from window5 import result_window
import numpy as np
import random
from time import sleep

# параметри головного вікна
root = tk.Tk()
root.geometry("640x360")
root.resizable(width=False, height=False)
root.title("Лабораторна робота №1")
root['bg'] = 'grey'

""" info_and_mode_frame - фрейм з режимом вводу та інформацією про студента """

info_and_mode_frame = tk.Frame(root, highlightbackground="black", highlightthickness=1, width=640)
info_and_mode_frame.pack(fill=tk.X, pady=(5,0))

# фрейм з радіокнопками
radio_frame = tk.Frame(info_and_mode_frame)
radio_frame.grid(padx=(20, 0))

# надпис
radio_lbl = tk.Label(radio_frame, text='Множину задати:', font=("Segoe UI", 9, 'bold'))
radio_lbl.grid(column=0, row=0, sticky='w')

# флаг
def select_manually():
    l = [[entry_A, entry_B, entry_C], [entry_cardinalily_A, entry_cardinalily_B, entry_cardinalily_C]]
    for e in l[0]:
        e['state']=tk.NORMAL
    for e in l[1]:
        e['state']=tk.DISABLED

def select_auto():
    l = [[entry_A, entry_B, entry_C], [entry_cardinalily_A, entry_cardinalily_B, entry_cardinalily_C]]
    for e in l[0]:
        e['state']=tk.DISABLED
    for e in l[1]:
        e['state']=tk.NORMAL

def str_to_set(s):
    return list(s.replace(' ', '').split(','))

def random_set(a):
    s = set()
    while len(s) != a:
        s.add(str(random.randint(1, 10)))
    return s

def generate():
    global A, B, C, U

    if flag.get() == 1:
        if entry_A.get() == '': A = '{}'
        else: A = str_to_set(entry_A.get())

        if entry_B.get() == '': B = '{}'
        else: B = str_to_set(entry_B.get())

        if entry_C.get() == '': C = '{}'
        else: C = str_to_set(entry_C.get())

        lbl_A_set['text'] = "A = {"+', '.join(A)+"}"
        lbl_B_set['text'] = "B = {"+', '.join(B)+"}"
        lbl_C_set['text'] = "C = {"+', '.join(C)+"}"

    if flag.get() == 0:
        if entry_cardinalily_A.get() == '': A = '{}'
        else: A = int(entry_cardinalily_A.get())

        if entry_cardinalily_B.get() == '': B = '{}'
        else: B = int(entry_cardinalily_B.get())

        if entry_cardinalily_C.get() == '': C = '{}'
        else: C = int(entry_cardinalily_C.get())

        A = random_set(A)
        B = random_set(B)
        C = random_set(C)

        lbl_A_set['text'] = "A = {"+', '.join(A)+"}"
        lbl_B_set['text'] = "B = {"+', '.join(B)+"}"
        lbl_C_set['text'] = "C = {"+', '.join(C)+"}"


    if entry_universal_start.get() == '': start_U = '{}'
    else: start_U = int(entry_universal_start.get())

    if entry_universal_end.get() == '': end_U = '{}'
    else: end_U = int(entry_universal_end.get())
    U = [str(i) for i in range(start_U, end_U+1)]
    lbl_U_set['text'] = "U = {"+', '.join(U)+"}"



flag = tk.BooleanVar()
r1 = tk.Radiobutton(radio_frame, text='вручну', variable=flag, value=1, command=select_manually)
r2 = tk.Radiobutton(radio_frame, text='випадково', variable=flag, value=0, command=select_auto)
r1.grid(column=0, row=1, sticky='w')
r2.grid(column=0, row=2, sticky='w')



# кнопка з інформацією про студента, його варіант та номер групи
clicks = 0
student_btn = tk.Button(info_and_mode_frame,
    text="!   Інформація  !",
    width=18,
    height=1,
    font=("Segoe UI", 11, 'bold'),
    fg='#d9073d',
    bg="#C0C0C0",
    activebackground='grey',
    command=None if clicks==1 else student_info_window)
student_btn.grid(padx=(320, 0), column=1, row=0, sticky='e', ipady=5)
"""-------------------------------------------------------------------------"""

"""---------main_frame - фрейм з полями вводу та виводом результату---------"""

main_frame = tk.Frame(root, width=640, height=300, highlightbackground="black", highlightthickness=1)
main_frame.pack(pady=3, fill=tk.BOTH, ipady=5)

# left_frame
left_frame = tk.Frame(main_frame, height=100, width=320)
left_frame.grid(column=0, row=0, sticky='w', padx=(10, 0))

# назва фрейму
lbl_left = tk.Label(left_frame, text='Задати вручну', font=("Segoe UI", 9, 'bold'))
lbl_left.pack()

# frame_A
frame_A = tk.Frame(left_frame)
frame_A.pack()
lbl_A = tk.Label(frame_A, text='A: ')
lbl_A.pack(side=tk.LEFT)

entry_A = tk.Entry(frame_A, state=tk.DISABLED)
entry_A.pack(side=tk.RIGHT)

# frame_B
frame_B = tk.Frame(left_frame)
frame_B.pack()
lbl_B = tk.Label(frame_B, text='B: ')
entry_B = tk.Entry(frame_B, state=tk.DISABLED)
lbl_B.pack(side=tk.LEFT)
entry_B.pack(side=tk.RIGHT)

# frame_C
frame_C = tk.Frame(left_frame)
frame_C.pack()
lbl_C = tk.Label(frame_C, text='C: ')
entry_C = tk.Entry(frame_C, state=tk.DISABLED)
lbl_C.pack(side=tk.LEFT)
entry_C.pack(side=tk.RIGHT)

# right_frame
right_frame = tk.Frame(main_frame, height=100, width=320)
right_frame.grid(column=2, row=0, sticky='e')

# назва фрейму
lbl2 = tk.Label(right_frame, text='Задати випадково', font=("Segoe UI", 9, 'bold'))
lbl2.pack()

# frame_cardinalily_A
frame_cardinalily_A = tk.Frame(right_frame)
frame_cardinalily_A.pack()
lbl_cardinalily_A = tk.Label(frame_cardinalily_A, text='Потужність A: ')
entry_cardinalily_A = tk.Entry(frame_cardinalily_A, state=tk.DISABLED)
lbl_cardinalily_A.pack(side=tk.LEFT)
entry_cardinalily_A.pack(side=tk.RIGHT)

# frame_cardinalily_B
frame_cardinalily_B = tk.Frame(right_frame)
frame_cardinalily_B.pack()
lbl_cardinalily_B = tk.Label(frame_cardinalily_B, text='Потужність B: ')
entry_cardinalily_B = tk.Entry(frame_cardinalily_B, state=tk.DISABLED)
lbl_cardinalily_B.pack(side=tk.LEFT)
entry_cardinalily_B.pack(side=tk.RIGHT)

# frame_cardinalily_C
frame_cardinalily_C = tk.Frame(right_frame)
frame_cardinalily_C.pack()
lbl_cardinalily_C = tk.Label(frame_cardinalily_C, text='Потужність C: ')
entry_cardinalily_C = tk.Entry(frame_cardinalily_C, state=tk.DISABLED)
lbl_cardinalily_C.pack(side=tk.LEFT)
entry_cardinalily_C.pack(side=tk.RIGHT)

# universal_frame
universal_frame = tk.Frame(main_frame)
universal_frame.grid(column=1, row=0, sticky='w', padx=(35, 30))

# назва фрейму
lbl_universal = tk.Label(universal_frame, text='Діапазон універсальної множини', font=("Segoe UI", 9, 'bold'))
lbl_universal.pack()

# стартове число
universal_frame_start = tk.Frame(universal_frame)
universal_frame_start.pack()
lbl_universal_start = tk.Label(universal_frame_start, text='start: ')
entry_universal_start = tk.Entry(universal_frame_start)
lbl_universal_start.pack(side=tk.LEFT)
entry_universal_start.pack()

# кінцеве число
universal_frame_end = tk.Frame(universal_frame)
universal_frame_end.pack()
lbl_universal_end = tk.Label(universal_frame_end, text='end:  ')
entry_universal_end = tk.Entry(universal_frame_end)
lbl_universal_end.pack(pady=(0, 3), side=tk.LEFT)
entry_universal_end.pack(pady=(0, 3))

A = set()
B = set()
C = set()


# кнопка генерації множин, якщо вони не були задані та обчислення
generate_button = tk.Button(main_frame,
    text='Згенерувати множини',
    font=("Segoe UI", 9, 'italic'),
    width=60,
    height=1,
    bg="#C0C0C0",
    activebackground='grey',
    command=generate)
generate_button.grid(pady=(5, 0), column=0, row=1, columnspan=3)

# поле виводу згенерованих множин
task_sets_frame = tk.Frame(root, highlightbackground="black", highlightthickness=1)
task_sets_frame.pack(fill=tk.BOTH, ipady=3)

lbl_A_set = tk.Label(task_sets_frame, text="A = { }")
lbl_A_set.pack(pady=(3, 0))

lbl_B_set = tk.Label(task_sets_frame, text='B = { }')
lbl_B_set.pack()

lbl_C_set = tk.Label(task_sets_frame, text='C = { }')
lbl_C_set.pack()

lbl_U_set = tk.Label(task_sets_frame, text='U = { }')
lbl_U_set.pack()
"""-------------------------------------------------------------------------"""

def full_solution_window_1():
    full_solution_window(A, B, C)

def solution_window_1():
    solution_window(A, B, C)

def set_problem_1():
    set_problem(A, B, C)

def result_window_1():
    result_window()

"""---------------------button_frame - фрейм з кнопками---------------------"""
button_frame = tk.Frame(root, highlightbackground="black", highlightthickness=1)
button_frame.pack(fill=tk.BOTH, pady=(4,0))

# кнопка 1
button_win1 = tk.Button(button_frame, text='1', width=13, height=2,
                                bg="#C0C0C0", activebackground='grey', command=full_solution_window_1)
button_win1.pack(side=tk.LEFT, padx=(97, 12), pady=(7, 7))

# кнопка 2
button_win2 = tk.Button(button_frame, text='2', width=13, height=2,
                                bg="#C0C0C0", activebackground='grey', command=solution_window_1)
button_win2.pack(side=tk.LEFT, padx=(0, 12), pady=(7, 7))

# кнопка 3
button_win3 = tk.Button(button_frame, text='3', width=13, height=2,
                                bg="#C0C0C0", activebackground='grey', command=set_problem_1)
button_win3.pack(side=tk.LEFT, padx=(0, 12), pady=(7, 7))

# кнопка 4
button_win4 = tk.Button(button_frame, text='4', width=13, height=2,
                                bg="#C0C0C0", activebackground='grey', command=result_window_1)
button_win4.pack(side=tk.LEFT, padx=(0, 12), pady=(7, 7))
"""-------------------------------------------------------------------------"""


root.mainloop()
