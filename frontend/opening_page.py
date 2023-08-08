import tkinter as tk
import tkinter.ttk as ttk

class OpeningPageFrame(ttk.Frame):
    def __init__(self, app):
        super().__init__(app)
        print('Opening frame created')

        self.head1 = tk.Label(self, text="POLL PILOT", font=('Times', 12))
        self.head1.place(x=170, y=10, height=20)
        self.head2 = tk.Label(self, text=" A simple tool to conduct election", font=('Helvetica', 10))
        self.head2.place(x=120, y=30, height=20)

        self.btn1 = ttk.Button(self, text="      Create An Election        ", command=app.show_frame_factory('createelec'))
        self.btn1.place(x=130, y=100, height=30)
        self.btn2 = ttk.Button(self, text="        Create A Refrendum       ", command=app.show_frame_factory('createref'))
        self.btn2.place(x=150, y=150, height=30)
        self.btn3 = ttk.Button(self, text="            HELP??              ", command=app.show_frame_factory('help'))
        self.btn3.place(x=130, y=200, height=30)
        self.btn4 = ttk.Button(self, text="            Credits                  ", command=app.show_frame_factory('credits'))
        self.btn4.place(x=150, y=250, height=30)

        self.pack()
        print('Opening frame placed')