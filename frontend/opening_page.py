import tkinter as tk
import tkinter.ttk as ttk

class OpeningPageFrame(ttk.Frame):
    def __init__(self, app, context):
        super().__init__(app)
        self.grid_columnconfigure(0, weight=1)
        for i in range(8):
            self.grid_rowconfigure(i, weight=1)

        self.head1 = ttk.Label(self, text="POLL PILOT", font=('Times', 12))
        self.head1.grid(row=0, column=0)
        self.head2 = ttk.Label(self, text=" A simple tool to conduct election", font=('Helvetica', 10))
        self.head2.grid(row=1, column=0)

        self.btn1 = ttk.Button(self, text="Create An Election", command=app.show_frame_factory('cre_elec'))
        self.btn1.grid(row=2, column=0)
        self.btn2 = ttk.Button(self, text="Create A Refrendum", command=app.show_frame_factory('create_ref'))
        self.btn2.grid(row=3, column=0)
        self.btn2 = ttk.Button(self, text="Show Elections", command=app.show_frame_factory('elec_navigation'))
        self.btn2.grid(row=4, column=0)
        self.btn3 = ttk.Button(self, text="HELP??", command=app.show_frame_factory('help'))
        self.btn3.grid(row=5, column=0)
        self.btn4 = ttk.Button(self, text="Credits", command=app.show_frame_factory('credits'))
        self.btn4.grid(row=6, column=0)
        self.btn5 = ttk.Button(self, text="TESTS", command=app.show_frame_factory('cand_entry'))
        self.btn5.grid(row=7, column=0)