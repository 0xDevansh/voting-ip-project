import tkinter as tk
import tkinter.ttk as ttk

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        # self.geometry('300x200')
        self.title('Poll Pilot')

        style = ttk.Style()
        style.theme_use('clam')
        FrontPage().pack(ipadx=100, ipady=10)

class FrontPage(ttk.Frame):
    def __init__(self):
        super().__init__()
        ttk.Button(text='Create new poll').pack()
        ttk.Button(text='Cast vote').pack()
        ttk.Button(text='Calculate poll result').pack()

class CreatePollPage(ttk.Frame):
    def __init__(self):
        super().__init__()
        ttk.Label(text='Create new poll', padding=()).pack()
        ttk.Label(text='Poll name:', padding=()).pack()
        ttk.Entry().pack()
        ttk.Label(text='Algorithm:', padding=()).pack()
        ttk.OptionMenu().pack()
