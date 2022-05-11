import tkinter as tk
import random

from student_info_window import StudentInfoWindow
from full_solution_window import FullSolutionWindow
from solution_window import SolutionWindow
from about_set_problem import AboutSetProblem
from result_window import ResultWindow


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.user_interface()
        self.hash = {}

    def user_interface(self):
        self.fonts()
        self.window_configuration()
        self.radiobuttons_and_about_student_frame()
        self.main_frame()
        self.button_frame()

    def fonts(self):
        self.normal_font = ("Segoe UI", 9, 'normal')
        self.bold_font = ("Segoe UI", 9, 'bold')
        self.italic_font = ("Segoe UI", 9, 'italic')

    def window_configuration(self):
        # configure the root window
        self.geometry('640x360')
        self.resizable(width=False, height=False)
        self.title('Лабораторна робота №1')
        self['bg'] = 'grey'

    def radiobuttons_and_about_student_frame(self):
        # radiobuttons & info frame
        info_and_mode_frame = tk.Frame(
            self,
            highlightthickness=1,
            highlightbackground='black',
            width=640)
        info_and_mode_frame.pack(fill=tk.X, pady=(5, 0))

        self.radiobuttons_frame(info_and_mode_frame)
        self.about_student_button(info_and_mode_frame)

    def radiobuttons_frame(self, frame):
        # radiobuttons frame
        radio_frame = tk.Frame(frame)
        radio_frame.grid(padx=(20, 0))
        tk.Label(radio_frame, text='Множину задати:', font=self.bold_font).\
            grid(column=0, row=0, sticky='w')

        self.create_radiobuttons(radio_frame)

    def create_radiobuttons(self, radio_frame):
        self.flag = tk.BooleanVar()
        tk.Radiobutton(radio_frame, text="manually", variable=self.flag, value=0,
                       command=lambda: self.select_mode("manually")).\
            grid(column=0, row=1, sticky='w')

        tk.Radiobutton(radio_frame, text="auto", variable=self.flag, value=1,
                       command=lambda: self.select_mode("auto")).\
            grid(column=0, row=2, sticky='w')

    def select_mode(self, mode):
        if mode not in ["manually", "auto"]:
            return -1
        for i in ['a', 'b', 'c']:
            self.nametowidget('.mf.lf.f'+i+'.'+i)['state'] = tk.DISABLED\
                                if mode == 'manually' else tk.NORMAL
            self.nametowidget('.mf.rf.fc'+i+'.c'+i)['state'] = tk.NORMAL\
                if mode == 'manually' else tk.DISABLED

    def str_to_set(self, str_):
        return list(str_.replace(' ', '').split(','))

    def random_set(self, a):
        s = set()
        while len(s) != a:
            s.add(str(random.randint(1, 10)))
        return s

    def generate_by_condition(self, flag):
        for i in ['a', 'b', 'c']:
            if flag:
                temp_set = self.nametowidget('.mf.rf.fc'+i+'.c'+i).get()
                self.hash[i.title()] = '{}' if temp_set == ''\
                    else self.str_to_set(temp_set)
            temp_set = self.nametowidget('.mf.lf.f'+i+'.'+i).get()
            self.hash[i.title()] = self.random_set(
                '{}' if temp_set == '' else int(temp_set))

        self.lbl_A_set['text'] = "A = {"+', '.join(self.hash['A'])+"}"
        self.lbl_B_set['text'] = "B = {"+', '.join(self.hash['B'])+"}"
        self.lbl_C_set['text'] = "C = {"+', '.join(self.hash['C'])+"}"

    def generate_univ_set(self):
        temp = self.nametowidget('.mf.fu.us').get()
        start = '{}' if temp == '' else int(temp)

        temp = self.nametowidget('.mf.fu.ue').get()
        end = '{}' if temp == '' else int(temp)

        U = [str(i) for i in range(start, end+1)]
        self.lbl_U_set['text'] = "U = {"+', '.join(U)+"}"

    def generate_task(self):
        if self.flag.get() == 1:
            self.generate_by_condition(True)
        else:
            self.generate_by_condition(False)

        self.generate_univ_set()

    def about_student_button(self, frame):
        b = tk.Button(frame, width=18, height=1, fg='#d9073d', bg="#C0C0C0",
                      text='!   Інформація  !', activebackground='grey',
                      font=("Segoe UI", 11, 'bold'),
                      command=self.open_student_info_window)
        b.grid(padx=(320, 0), column=1, row=0, sticky='e', ipady=5)

    def left_and_right_frames_content(self, flag):
        c = (flag == 'r')
        frame_ = tk.Frame(self.main_frame, height=100,
                          width=320, name='rf' if c else 'lf')
        frame_.grid(column=0 if c else 2, row=0,
                    sticky='e' if c else 'w', padx=(10, 0) if c else (0, 0))

        text_ = ('Задати вручну', "fc", '', 'c')\
            if c else ('Задати випадково', 'f', 'Потужність ', '')

        tk.Label(frame_, text=text_[0], font=self.bold_font).pack()
        for i in ['a', 'b', 'c']:
            frame = tk.Frame(frame_, name=text_[1]+i)
            frame.pack()

            tk.Label(frame, text=text_[2]+i.title() + ': ').pack(side=tk.LEFT)
            tk.Entry(frame, state=tk.DISABLED,
                     name=text_[3]+i).pack(side=tk.RIGHT)

    def universal_frame_content(self):
        universal_frame = tk.Frame(self.main_frame, name='fu')
        universal_frame.grid(column=1, row=0, sticky='w', padx=(35, 30))

        tk.Label(universal_frame, text='Діапазон універсальної множини',
                 font=self.bold_font).grid(column=0, row=0, columnspan=2)

        tk.Label(universal_frame, text='start: ').grid(column=0, row=1)
        tk.Entry(universal_frame, name='us').grid(column=1, row=1)

        tk.Label(universal_frame, text='end:  ').grid(column=0, row=2)
        tk.Entry(universal_frame, name='ue').grid(column=1, row=2)

    def generate_button(self):
        tk.Button(self.main_frame, text='Згенерувати множини',
                  font=self.italic_font, width=60, height=1, bg="#C0C0C0",
                  activebackground='grey', command=self.generate_task).\
            grid(pady=(5, 0), column=0, row=1, columnspan=3)

    def task_condition(self):
        task_sets_frame = tk.Frame(
            self, highlightbackground="black", highlightthickness=1)
        task_sets_frame.pack(fill=tk.BOTH, ipady=3)

        self.lbl_A_set = tk.Label(task_sets_frame, text="A = { }")
        self.lbl_A_set.pack(pady=(3, 0))

        self.lbl_B_set = tk.Label(task_sets_frame, text='B = { }')
        self.lbl_B_set.pack()

        self.lbl_C_set = tk.Label(task_sets_frame, text='C = { }')
        self.lbl_C_set.pack()

        self.lbl_U_set = tk.Label(task_sets_frame, text='U = { }')
        self.lbl_U_set.pack()

    def main_frame(self):
        self.main_frame = tk.Frame(self, name='mf', width=640, height=300,
                                   highlightbackground="black",
                                   highlightthickness=1)
        self.main_frame.pack(pady=3, fill=tk.BOTH, ipady=5)

        self.left_and_right_frames_content('l')
        self.left_and_right_frames_content('r')
        self.universal_frame_content()
        self.generate_button()
        self.task_condition()

    def button_frame(self):
        button_frame = tk.Frame(
            self, highlightbackground="black", highlightthickness=1)
        button_frame.pack(fill=tk.BOTH, pady=(4, 0))

        params = {'master': button_frame, 'width': 13, 'height': 2, 'bg': '#C0C0C0',
                  'activebackground': 'grey'}

        params_pack = {'side': tk.LEFT, 'padx': (0, 12), 'pady': (7, 7), }

        tk.Button(text='1', **params, command=self.open_full_solution_window).\
            pack(side=tk.LEFT, padx=(97, 12), pady=(7, 7))
        tk.Button(text='2', **params, command=self.open_solution_window).\
            pack(**params_pack)
        tk.Button(text='3', **params, command=self.open_about_set_problem).\
            pack(**params_pack)
        tk.Button(text='4', **params, command=self.open_result_window).\
            pack(**params_pack)

    def open_student_info_window(self):
        student_info_window = StudentInfoWindow(self)
        student_info_window.grab_set()

    def open_full_solution_window(self):
        full_solution_window = FullSolutionWindow(self, hash=self.hash)
        full_solution_window.grab_set()

    def open_solution_window(self):
        solution_window = SolutionWindow(self, hash=self.hash)
        solution_window.grab_set()

    def open_about_set_problem(self):
        about_set_problem = AboutSetProblem(self, hash=self.hash)
        about_set_problem.grab_set()

    def open_result_window(self):
        result_window = ResultWindow(self, self.hash)
        result_window.grab_set()


if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()
