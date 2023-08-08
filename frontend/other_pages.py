import tkinter as tk
import tkinter.ttk as ttk

class CreditsFrame(ttk.Frame):
    def __init__(self, app):
        super().__init__(app)
        # Text to be added to info label from the Documentation
        self.info1 = tk.Label(self, text="By:")
        self.info1.pack()
        self.info2 = tk.Label(self, text="Atharv Dubey &")
        self.info2.pack()
        self.info3 = tk.Label(self, text="Devansh Kandpal")
        self.info3.pack()
        self.btn4 = tk.Button(self, text="    Back   ", command=app.show_frame_factory('opening'))
        self.btn4.place(x=400, y=250, height=20)