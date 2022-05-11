import tkinter as tk

def solution_window(A, B, C):
    root = tk.Tk()
    root.minsize(350, 200)
    root.maxsize(350, 200)
    root.title("Обчислення заданого виразу")
    root['bg'] = 'grey'

    A = {int(i) for i in A}
    B = {int(i) for i in B}
    C = {int(i) for i in C}

    info_frame = tk.Frame(root, highlightbackground="black", highlightthickness=1)
    info_frame.pack(fill=tk.BOTH, pady=(4, 3))

    lbl_title = tk.Label(info_frame, text='Спрощений вираз:', font=("Segoe UI", 10, 'bold'))
    lbl_title.pack()

    lbl_title = tk.Label(info_frame, text='D = A\(C∪B) = '+ str(A-(C|B)), font=("Segoe UI", 9))
    lbl_title.pack(pady=(0, 5))

    lbl_title = tk.Label(info_frame, text='A = '+str({int(i) for i in A}), justify=tk.LEFT, font=("Segoe UI", 9))
    lbl_title.pack()

    lbl_title = tk.Label(info_frame, text='B = '+str({int(i) for i in B}), justify=tk.LEFT, font=("Segoe UI", 9))
    lbl_title.pack()

    lbl_title = tk.Label(info_frame, text='C = '+str({int(i) for i in C}), justify=tk.LEFT, font=("Segoe UI", 9))
    lbl_title.pack()

    def show_result():
        lbl_solution_title['fg'] = 'black'
        lbl_solution_1['fg'] = 'black'
        lbl_solution_2['fg'] = 'black'

    def save_result():
        with open('short_solution.txt', 'w', encoding='utf-8') as file:
            file.write(lbl_solution_title["text"] + '\n')
            file.write(lbl_solution_1["text"] + '\n')
            file.write(lbl_solution_2["text"] + '\n')

    solution_frame = tk.Frame(root, highlightbackground="black", highlightthickness=1)
    solution_frame.pack(fill=tk.BOTH, pady=(0, 3))

    lbl_solution_title = tk.Label(solution_frame, text="Розв'язок:", font=("Segoe UI", 9, "bold"), fg='#f0f0f0')
    lbl_solution_title.grid(column=0, row=0)

    lbl_solution_1 = tk.Label(solution_frame, text="1.  C∪B = " + str(C|B), fg='#f0f0f0')
    lbl_solution_1.grid(column=2, row=0, sticky='w')

    lbl_solution_2 = tk.Label(solution_frame, text="2.  A\(C∪B) = " + str(A-(C|B)), fg='#f0f0f0')
    lbl_solution_2.grid(column=2, row=1, sticky='w')
    global D
    D = str(A-(C|B))

    btn_solution = tk.Button(info_frame, text="Розв'язок", width=10, bg="#C0C0C0", activebackground='grey', command=show_result)
    btn_solution.pack(side=tk.LEFT, padx=(30, 0), pady=(0, 5))

    btn_solution = tk.Button(info_frame, text="Зберегти", width=10, bg="#C0C0C0", activebackground='grey', command=save_result)
    btn_solution.pack(padx=(100, 0), pady=(0, 5))

    root.mainloop()

def get_D2():
    return D
