import tkinter as tk
import tkinter.ttk as ttk

class Helpframe(ttk.Frame):
    def __init__(self, app, context):
        super().__init__(app)
        self.grid_columnconfigure(0, weight=1)
        # 6 = no of elements to be centered
        for i in range(3):
            self.grid_rowconfigure(i, weight=1)
        self.info1 = ttk.Label(self, text="How to")
        self.info1.grid(row=0, column=0)
        self.frame1 = ttk.Frame(self)
        self.frame1.grid(row =1 , column = 0)
        for i in range(2):
            self.frame1.grid_rowconfigure(i, weight=1)
        self.frame1.grid_columnconfigure(0, weight=1)
        self.frame1.grid_columnconfigure(1, weight=1)
        info2 = ttk.Label(self.frame1, text="Poll Pilot is a solution for conducting polls or elections at any scale, small or large. This program allows users to create polls, let the voters vote and generate the result based on any of the four polling algorithms.")
        info2.grid(row=0, column=0)
        self.btn4 = ttk.Button(self, text="    Back   ", command=app.show_frame_factory('opening'))
        self.btn4.grid(row=2, column=0)

