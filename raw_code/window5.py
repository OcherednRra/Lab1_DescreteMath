import tkinter as tk
from window2 import get_D1
from window3 import get_D2
from window4 import get_Z1, get_Z2

def result_window():
    root = tk.Tk()
    root.minsize(350, 260)
    root.maxsize(350, 260)
    root.title("Результати")
    root['bg'] = 'grey'

    info_frame = tk.Frame(root, highlightbackground="black", highlightthickness=1)
    info_frame.pack(fill=tk.BOTH, pady=(4, 3))

    lbl_title = tk.Label(info_frame, text='Результати', font=("Segoe UI", 11, "bold"))
    lbl_title.pack(pady=(0, 10))

    lbl_title = tk.Label(info_frame, text='Множина D:', font=("Segoe UI", 9, "bold"))
    lbl_title.pack()

    lbl_title = tk.Label(info_frame, text='D = ((A\B)∪(B⋂A))\(C∪B) = '+get_D1(), font=("Segoe UI", 9))
    lbl_title.pack()

    lbl_title = tk.Label(info_frame, text='D(спрощений) = A\(C∪B) = '+get_D2(), font=("Segoe UI", 9))
    lbl_title.pack()

    def compare_sets():
        if get_Z1() == get_Z2():
            lbl_compare['text'] = "Результати співпадають"
            lbl_compare_1['text'] = "Результати співпадають"


    lbl_compare = tk.Label(info_frame, text='', font=("Segoe UI", 9), fg='green')
    lbl_compare.pack()

    lbl_title = tk.Label(info_frame, text='Множина Z:', font=("Segoe UI", 9, "bold"))
    lbl_title.pack()

    lbl_title = tk.Label(info_frame, text='Z(власний алгоритм) = '+get_Z1(), font=("Segoe UI", 9))
    lbl_title.pack()

    lbl_title = tk.Label(info_frame, text='Z(алгоритм Python) = '+get_Z2(), font=("Segoe UI", 9))
    lbl_title.pack()

    lbl_compare_1 = tk.Label(info_frame, text='', font=("Segoe UI", 9), fg='green')
    lbl_compare_1.pack()

    btn_solution = tk.Button(info_frame, text="Порівняти результати", bg="#C0C0C0", activebackground='grey', command=compare_sets)
    btn_solution.pack(pady=(10, 15))

    root.mainloop()
