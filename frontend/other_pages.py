import tkinter as tk
import tkinter.ttk as ttk

class CreditsFrame(ttk.Frame):
    def __init__(self, app):
        super().__init__(app)
        # Text to be added to info label from the Documentation
        self.info1 = ttk.Label(self, text="By:")
        self.info1.grid(row=0, column=0)
        self.info2 = ttk.Label(self, text="Atharv Dubey &")
        self.info2.grid(row=1, column=0)
        self.info3 = ttk.Label(self, text="Devansh Kandpal")
        self.info3.grid(row=2, column=0)
        self.btn4 = ttk.Button(self, text="    Back   ", command=app.show_frame_factory('opening'))
        self.btn4.grid(row=3, column=0)