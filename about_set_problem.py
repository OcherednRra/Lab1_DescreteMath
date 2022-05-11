import tkinter as tk

class AboutSetProblem(tk.Toplevel):
    def __init__(self, parent, hash):
        super().__init__(parent)
        self.initialization_variables(hash)
        self.user_interface(hash)

    def initialization_variables(self, hash):
        self.A = {int(i) for i in hash['A']}
        self.B = {int(i) for i in hash['B']}
        self.C = {int(i) for i in hash['C']}

    def user_interface(self, hash):
        self.fonts()
        self.window_configuration()
        self.problem_frame(hash)

    def fonts(self):
        self.normal_font = ("Segoe UI", 9, 'normal')
        self.bold_font = ("Segoe UI", 9, 'bold')
        self.italic_font = ("Segoe UI", 9, 'italic')

    def window_configuration(self):
        self.geometry("350x173")
        self.resizable(width=False, height=False)
        self.title("Обчислення заданої дії")
        self['bg'] = 'grey'

    def task_info_frame(self):
        info_frame = tk.Frame(self, highlightbackground="black", highlightthickness=1)
        info_frame.pack(fill=tk.BOTH, pady=(4, 3))

        opt = {'master': info_frame, 'font': self.normal_font}
        tk.Label(info_frame, text='Множина', font=self.bold_font).pack()
        tk.Label(**opt, text='Z = X\Y').pack()
        tk.Label(**opt, text='X = '+str(self.A), ).pack()
        tk.Label(**opt, text='Y = '+str(self.B)).pack()

        self.functional_buttons(info_frame)

    def show_result(self):
        for i in range(1, 3):
            self.nametowidget('.!aboutsetproblem.sf.l' + str(i))['fg'] = 'black'

    def save_result(self):
        with open('txt/set_problem_solution.txt', 'w', encoding='utf-8') as file:
            for i in range(1, 3):
                file.write(self.nametowidget('.!aboutsetproblem.sf.l' + str(i))['text']+'\n')

    def functional_buttons(self, info_frame):
        opt = {'master': info_frame, 'width': 10, 'bg': '#C0C0C0', "activebackground": 'grey'}

        tk.Button(**opt, text="Розв'язок", command=self.show_result).\
                        pack(side=tk.LEFT, padx=(30, 0), pady=(0, 5))
        tk.Button(**opt, text="Зберегти", command=self.save_result).\
                        pack(padx=(100, 0), pady=(0, 5))

    def task_solution_frame(self):
        solution_frame = tk.Frame(self, name='sf', highlightbackground="black", highlightthickness=1)
        solution_frame.pack(fill=tk.BOTH, pady=(0, 3))

        opt = {'master': solution_frame, 'fg': '#f0f0f0'}
        tk.Label(**opt, name='l1', text="Розв'язок:", font=self.bold_font).\
                        grid(column=0, row=0)
        tk.Label(**opt, name='l2', text="Z = {0}\{1} = ".format(self.A,self.B) + str(self.A-self.B)).\
                        grid(column=2, row=1, sticky='w', pady=(0, 5))

    def problem_frame(self, hash):
        self.task_info_frame()
        self.task_solution_frame()
