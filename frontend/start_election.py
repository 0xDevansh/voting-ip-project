import tkinter as tk
import tkinter.messagebox
import tkinter.ttk as ttk


# for easy access cand_entry is in referendum

class StartElectionFrame(ttk.Frame):
    def __init__(self, app, context):
        super().__init__(app)
        poll = context['poll']
        print(poll)
        sec_key = poll['security_key']
        # sec_key = 'password'

        def start_election():
            ent_password = entry1.get()

            if ent_password == sec_key:
                app.show_frame('voting_window')
            else:
                tkinter.messagebox.showerror(title= "error" , message= "Security key is incorrect")

        for i in range(4):
            self.grid_rowconfigure(i, weight=1)
        for i in range(1):
            self.grid_columnconfigure(i, weight=1)

        self.frame = tk.Frame(self)
        self.frame.grid()



        label1 = tk.Label(self, text="Your election has been created" , font= 20)
        label1.grid(row=0, column=0 , pady= 10)

        label2 = tk.Label(self, text="Enter Security Key to Start")
        label2.grid(row=1, column=0,  pady= 10)
        entry1 = tk.Entry(self)
        entry1.grid(row=2, column=0)

        start_button = tk.Button(self, text="Start", command = start_election)
        start_button.grid(row=3, column=0 ,  pady= 10)
