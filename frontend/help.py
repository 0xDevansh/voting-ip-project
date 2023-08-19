import tkinter as tk
import tkinter.ttk as ttk

class Helpframe(ttk.Frame):
    def __init__(self, app):
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
        info2 = ttk.Label(self.frame1, text="This page will be updated soon")
        info2.grid(row=0, column=0)
        info3 = ttk.Label(self.frame1, text="Very soon")
        info3.grid(row=0, column=1)
        self.btn4 = ttk.Button(self, text="    Back   ", command=app.show_frame_factory('opening'))
        self.btn4.grid(row=2, column=0)

