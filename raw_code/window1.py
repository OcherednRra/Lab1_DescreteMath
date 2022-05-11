import tkinter as tk

def student_info_window():
    global clicks
    root = tk.Tk()
    root.minsize(350, 184)
    root.maxsize(350, 184)
    root.title("Інформація про лабораторну роботу")
    root['bg'] = 'grey'

    info_frame = tk.Frame(root, highlightbackground="black", highlightthickness=1)
    info_frame.pack(fill=tk.BOTH, pady=(4, 3))

    lbl_pib_0 = tk.Label(info_frame, text='Підготував:', font=("Segoe UI", 9, 'bold'))
    lbl_pib_0.grid(column=0, row=0, sticky='w')

    lbl_pib_1 = tk.Label(info_frame, text='Поляков Валентин Олегович')
    lbl_pib_1.grid(column=1, row=0, sticky='w')

    lbl_group_0 = tk.Label(info_frame, text='Група:', font=("Segoe UI", 9, 'bold'))
    lbl_group_0.grid(column=0, row=1, sticky='w')

    lbl_group_1 = tk.Label(info_frame, text='IO-15')
    lbl_group_1.grid(column=1, row=1, sticky='w')

    lbl_n_0 = tk.Label(info_frame, text='Номер у списку групи:', font=("Segoe UI", 9, 'bold'))
    lbl_n_0.grid(column=0, row=2, sticky='w')

    lbl_n_1 = tk.Label(info_frame, text='15')
    lbl_n_1.grid(column=1, row=2, sticky='w')

    frame_variant = tk.Frame(root, highlightbackground="black", highlightthickness=1)
    frame_variant.pack(fill=tk.BOTH)

    lbl_variant = tk.Label(frame_variant, text="Розрахунок варіанту лабораторної роботи", font=("Segoe UI", 9, 'bold'))
    lbl_variant.pack()

    lbl_variant_1 = tk.Label(frame_variant, text="Варіант лабораторної роботи обчислюється за формулою:", font=("Segoe UI", 9, 'italic'))
    lbl_variant_1.pack()

    lbl_variant_2 = tk.Label(frame_variant, text="(N + G%60)%30 + 1,", font=("Segoe UI", 10))
    lbl_variant_2.pack()

    lbl_variant_3 = tk.Label(frame_variant, text="де N - номер групи, G - номер групи", font=("Segoe UI", 9, 'italic'))
    lbl_variant_3.pack()

    n = f"{(15 + 15%60)%30 + 1}"

    lbl_variant_4 = tk.Label(frame_variant, text="Тому номер варіанту = (15 + 15%60)%30 + 1 = "+n, font=("Segoe UI", 9, 'bold'))
    lbl_variant_4.pack()

    root.mainloop()
