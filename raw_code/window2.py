import tkinter as tk

def full_solution_window(A, B, C):
    root = tk.Tk()
    root.minsize(350, 263)
    root.maxsize(350, 263)
    root.title("Обчислення заданого виразу")
    root['bg'] = 'grey'

    A = {int(i) for i in A}
    B = {int(i) for i in B}
    C = {int(i) for i in C}

    info_frame = tk.Frame(root, highlightbackground="black", highlightthickness=1)
    info_frame.pack(fill=tk.BOTH, pady=(4, 3))

    lbl_title = tk.Label(info_frame, text='Заданий вираз:', font=("Segoe UI", 10, 'bold'))
    lbl_title.pack()

    lbl_title = tk.Label(info_frame, text='D = ((A\B)∪(B⋂A))\(C∪B) = ' + str(((A-B)|(B&A))-(C|B)), font=("Segoe UI", 9))
    lbl_title.pack(pady=(0, 5))

    lbl_title = tk.Label(info_frame, text='A = '+str(A), justify=tk.LEFT, font=("Segoe UI", 9))
    lbl_title.pack()

    lbl_title = tk.Label(info_frame, text='B = '+str(B), justify=tk.LEFT, font=("Segoe UI", 9))
    lbl_title.pack()

    lbl_title = tk.Label(info_frame, text='C = '+str(C), justify=tk.LEFT, font=("Segoe UI", 9))
    lbl_title.pack()

    solution_frame = tk.Frame(root, highlightbackground="black", highlightthickness=1)
    solution_frame.pack(fill=tk.BOTH, pady=(0, 3))

    def show_result():
        lbl_solution_title['fg'] = 'black'
        lbl_solution_1['fg'] = 'black'
        lbl_solution_2['fg'] = 'black'
        lbl_solution_3['fg'] = 'black'
        lbl_solution_4['fg'] = 'black'
        lbl_solution_5['fg'] = 'black'

    def save_result():
        with open('full_solution.txt', 'w', encoding='utf-8') as file:
            file.write(lbl_solution_title["text"] + '\n')
            file.write(lbl_solution_1["text"] + '\n')
            file.write(lbl_solution_2["text"] + '\n')
            file.write(lbl_solution_3["text"] + '\n')
            file.write(lbl_solution_4["text"] + '\n')
            file.write(lbl_solution_5["text"] + '\n')


    lbl_solution_title = tk.Label(solution_frame, text="Розв'язок:", font=("Segoe UI", 9, "bold"), fg='#f0f0f0')
    lbl_solution_title.grid(column=0, row=0)

    lbl_solution_1 = tk.Label(solution_frame, text="1.  A\B = " + str(A-B), fg='#f0f0f0')
    lbl_solution_1.grid(column=2, row=0, sticky='w')

    lbl_solution_2 = tk.Label(solution_frame, text="2.  B⋂A = " + str(B&A), fg='#f0f0f0')
    lbl_solution_2.grid(column=2, row=1, sticky='w')

    lbl_solution_3 = tk.Label(solution_frame, text="3.  (A\B)∪(B⋂A) = " + str((A-B)|(B&A)), fg='#f0f0f0')
    lbl_solution_3.grid(column=2, row=2, sticky='w')

    lbl_solution_4 = tk.Label(solution_frame, text="4.  C∪B = " + str(C|B), fg='#f0f0f0')
    lbl_solution_4.grid(column=2, row=3, sticky='w')

    lbl_solution_5 = tk.Label(solution_frame, text="5.  ((A\B)∪(B⋂A))\(C∪B) = " + str(((A-B)|(B&A))-(C|B)), fg='#f0f0f0')
    lbl_solution_5.grid(column=2, row=4, sticky='w')
    global D
    D = str(((A-B)|(B&A))-(C|B))
    btn_solution = tk.Button(info_frame, text="Розв'язок", width=10, bg="#C0C0C0", activebackground='grey', command=show_result)
    btn_solution.pack(side=tk.LEFT, padx=(30, 0), pady=(0, 5))

    btn_solution = tk.Button(info_frame, text="Зберегти", width=10, bg="#C0C0C0", activebackground='grey', command=save_result)
    btn_solution.pack(padx=(100, 0), pady=(0, 5))

    root.mainloop()

def get_D1():
    return D
