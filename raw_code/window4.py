import tkinter as tk

def own_algorithm(X, Y):
    X = list(X)
    Y = list(Y)
    C = set()
    for i in X:
        if i not in Y:
            C.add(i)
    return C

def set_problem(A, B, C):
    root = tk.Tk()
    root.minsize(350, 173)
    root.maxsize(350, 173)
    root.title("Обчислення заданої дії")
    root['bg'] = 'grey'

    X = {int(i) for i in A}
    Y = {int(i) for i in B}

    info_frame = tk.Frame(root, highlightbackground="black", highlightthickness=1)
    info_frame.pack(fill=tk.BOTH, pady=(4, 3))

    lbl_title = tk.Label(info_frame, text='Множина', font=("Segoe UI", 9, "bold"))
    lbl_title.pack()

    lbl_title = tk.Label(info_frame, text='Z = X\Y', font=("Segoe UI", 9))
    lbl_title.pack()

    lbl_title = tk.Label(info_frame, text='X = '+str(X), font=("Segoe UI", 9))
    lbl_title.pack()

    lbl_title = tk.Label(info_frame, text='Y = '+str(Y), font=("Segoe UI", 9))
    lbl_title.pack()

    def show_result():
        lbl_solution_title['fg'] = 'black'
        lbl_solution_1['fg'] = 'black'

    def save_result():
        with open('set_problem_solution.txt', 'w', encoding='utf-8') as file:
            file.write(lbl_solution_title["text"] + '\n')
            file.write(lbl_solution_1["text"] + '\n')

    solution_frame = tk.Frame(root, highlightbackground="black", highlightthickness=1)
    solution_frame.pack(fill=tk.BOTH, pady=(0, 3))

    lbl_solution_title = tk.Label(solution_frame, text="Розв'язок:", font=("Segoe UI", 9, "bold"), fg='#f0f0f0')
    lbl_solution_title.grid(column=0, row=0)

    lbl_solution_1 = tk.Label(solution_frame, text="Z = {0}\{1} = ".format(X, Y) + str(X-Y), fg='#f0f0f0')
    lbl_solution_1.grid(column=2, row=1, sticky='w', pady=(0, 5))

    global Z2
    Z2 = str(X-Y)

    global Z1
    Z1 = str(own_algorithm(X, Y))

    btn_solution = tk.Button(info_frame, text="Розв'язок", width=10, bg="#C0C0C0", activebackground='grey', command=show_result)
    btn_solution.pack(side=tk.LEFT, padx=(30, 0), pady=(0, 5))

    btn_solution = tk.Button(info_frame, text="Зберегти", width=10, bg="#C0C0C0", activebackground='grey', command=save_result)
    btn_solution.pack(padx=(100, 0), pady=(0, 5))

    root.mainloop()

def get_Z2():
    return Z2

def get_Z1():
    return Z1
