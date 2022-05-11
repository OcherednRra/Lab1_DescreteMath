import tkinter as tk

class FullSolutionWindow(tk.Toplevel):
    def __init__(self, parent, hash):
        super().__init__(parent)
        self.initialization_variables(hash)
        self.user_interface()

    def initialization_variables(self, hash):
        self.A = {int(i) for i in hash['A']}
        self.B = {int(i) for i in hash['B']}
        self.C = {int(i) for i in hash['C']}

    def user_interface(self):
        self.fonts()
        self.window_configuration()
        self.problem_frame()

    def fonts(self):
        self.normal_font = ("Segoe UI", 9, 'normal')
        self.bold_font = ("Segoe UI", 9, 'bold')
        self.italic_font = ("Segoe UI", 9, 'italic')

    def window_configuration(self):
        self.minsize(350, 263)
        self.maxsize(350, 263)
        self.title("Обчислення заданого виразу")
        self['bg'] = 'grey'

    def show_result(self):
        for i in range(1, 7):
            self.nametowidget('.!fullsolutionwindow.sf.l'+str(i))['fg'] = 'black'

    def save_result(self):
        with open('txt/full_solution.txt', 'w', encoding='utf-8') as file:
            for i in range(1, 7):
                file.write(self.nametowidget('.!fullsolutionwindow.sf.l'+str(i))["text"] + '\n')

    def task_info_frame(self):
        info_frame = tk.Frame(self, highlightbackground="black", highlightthickness=1)
        info_frame.pack(fill=tk.BOTH, pady=(4, 3))

        opt = {'master': info_frame, 'font': self.normal_font, 'justify': tk.LEFT}
        temp = 'D = ((A\B)∪(B⋂A))\(C∪B) = ' + str(((self.A-self.B)|(self.B&self.A))-(self.C|self.B))

        tk.Label(info_frame, text='Заданий вираз:', font=("Segoe UI", 10, 'bold')).pack()
        tk.Label(info_frame, text=temp, font=self.normal_font).pack(pady=(0, 5))
        tk.Label(**opt, text='A = '+str(self.A)).pack()
        tk.Label(**opt, text='B = '+str(self.B)).pack()
        tk.Label(**opt, text='C = '+str(self.C)).pack()

        self.functional_buttons(info_frame)

    def functional_buttons(self, info_frame):
        opt = {'master': info_frame, 'width': 10, 'bg': '#C0C0C0', "activebackground": 'grey'}

        tk.Button(**opt, text="Розв'язок", command=self.show_result).pack(side=tk.LEFT, padx=(30, 0), pady=(0, 5))
        tk.Button(**opt, text="Зберегти", command=self.save_result).pack(padx=(100, 0), pady=(0, 5))

    def task_solution_frame(self):
        solution_frame = tk.Frame(self, highlightbackground="black", highlightthickness=1, name='sf')
        solution_frame.pack(fill=tk.BOTH, pady=(0, 3))

        opt = {'master': solution_frame, 'fg': '#f0f0f0'}

        temp = "Розв'язок:"
        tk.Label(**opt, name='l1', text=temp, font=self.bold_font).grid(column=0, row=0)

        temp = "1.  A\B = " + str(self.A-self.B)
        tk.Label(**opt, name='l2', text=temp).grid(column=2, row=0, sticky='w')

        temp ="2.  B⋂A = " + str(self.B&self.A)
        tk.Label(**opt, name='l3', text=temp).grid(column=2, row=1, sticky='w')

        temp = "3.  (A\B)∪(B⋂A) = " + str((self.A-self.B)|(self.B&self.A))
        tk.Label(**opt, name='l4', text=temp).grid(column=2, row=2, sticky='w')

        temp = "4.  C∪B = " + str(self.C|self.B)
        tk.Label(**opt, name='l5', text=temp).grid(column=2, row=3, sticky='w')

        temp = "5.  ((A\B)∪(B⋂A))\(C∪B) = " + str(((self.A-self.B)|(self.B&self.A))-(self.C|self.B))
        tk.Label(**opt, name='l6', text=temp).grid(column=2, row=4, sticky='w')

    def problem_frame(self):
        self.task_info_frame()
        self.task_solution_frame()
