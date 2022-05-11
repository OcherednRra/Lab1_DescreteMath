import tkinter as tk

class ResultWindow(tk.Toplevel):
    def __init__(self, parent, hash):
        super().__init__(parent)
        self.initialization_variables(hash)
        self.user_interface()

    def initialization_variables(self, hash):
        self.A = {int(i) for i in hash['A']}
        self.B = {int(i) for i in hash['B']}
        self.C = {int(i) for i in hash['C']}

    def user_interface(self):
        self.window_configuration()
        self.result_frame()

    def fonts(self):
        self.normal_font = ("Segoe UI", 9, 'normal')
        self.bold_font = ("Segoe UI", 9, 'bold')
        self.italic_font = ("Segoe UI", 9, 'italic')

    def window_configuration(self):
        self.geometry("350x260")
        self.resizable(width=False, height=False)
        self.title("Результати")
        self['bg'] = 'grey'

    def compare_sets(self):
        D = self.nametowidget('.!resultwindow.if.d')
        if self.full_algorithm() == self.short_algorithm():
            D['text'] = "Результати співпадають"
            D['fg'] = 'green'
        else:
            D['text'] = 'Результати не співпадають'
            D['fg'] = 'red'

        Z = self.nametowidget('.!resultwindow.if.z')
        if self.own_algorithm() == self.python_algorithm():
            Z['text'] = "Результати співпадають"
            Z['fg'] = 'green'
        else:
            Z['text'] = 'Результати не співпадають'
            Z['fg'] = 'red'

    def full_algorithm(self):
        A, B, C = self.A, self.B, self.C
        return str(((A-B)|(B&A))-(C|B))

    def short_algorithm(self):
        A, B, C = self.A, self.B, self.C
        return (str(A-(C|B)))

    def own_algorithm(self):
        X, Y, C = list(self.A), list(self.B), set()
        for i in X:
            if i not in Y: C.add(i)
        return str(C)

    def python_algorithm(self):
        return str(self.A-self.B)

    def result_frame(self):
        info_frame = tk.Frame(self, name='if', highlightbackground="black", highlightthickness=1)
        info_frame.pack(fill=tk.BOTH, pady=(4, 3))

        opt = {'master': info_frame, 'font': self.normal_font}

        tk.Label(info_frame, text='Результати', font=("Segoe UI", 11, "bold")).pack(pady=(0, 10))
        tk.Label(info_frame, text='Множина D:', font=self.bold_font).pack()

        tk.Label(**opt, text='D = ((A\B)∪(B⋂A))\(C∪B) = '+self.full_algorithm()).pack()
        tk.Label(**opt, text='D(спрощений) = A\(C∪B) = '+self.short_algorithm()).pack()
        tk.Label(**opt, name='d', text='').pack()

        tk.Label(info_frame, text='Множина Z:', font=self.bold_font).pack()

        tk.Label(**opt, text='Z(власний алгоритм) = '+self.own_algorithm()).pack()
        tk.Label(**opt, text='Z(алгоритм Python) = '+self.python_algorithm()).pack()
        tk.Label(**opt, name='z', text='').pack()

        btn_solution = tk.Button(info_frame, text="Порівняти результати", bg="#C0C0C0",\
                                 activebackground='grey', command=self.compare_sets)
        btn_solution.pack(pady=(10, 15))
