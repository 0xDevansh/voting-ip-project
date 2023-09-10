import tkinter as tk
import tkinter.messagebox
import tkinter.ttk as ttk


# for easy access cand_entry is in referendum

class VotingSecurityCheck(ttk.Frame):
    def __init__(self, app):
        super().__init__(app)
        password = "password" # security key to be assigned here

        def next_vote():
            ent_password = entry1.get()

            if ent_password == password:
                app.show_frame('voting_window')
            else:
                tkinter.messagebox.showerror(title= "error" , message= "Security key is incorrect")

        def terminate_election():
            ent_password = entry1.get()

            if ent_password == password:
                app.show_frame('result_page')
            else:
                tkinter.messagebox.showerror(title="error", message="Security key is incorrect")

        for i in range(5):
            self.grid_rowconfigure(i, weight=1)
        for i in range(1):
            self.grid_columnconfigure(i, weight=1)

        self.frame = tk.Frame(self)
        self.frame.grid()



        label1 = tk.Label(self, text="Vote Has been registered" , font= 20)
        label1.grid(row=0, column=0 , pady= 10)

        label2 = tk.Label(self, text="Enter Security Key to Continue")
        label2.grid(row=1, column=0,  pady= 10)
        entry1 = tk.Entry(self)
        entry1.grid(row=2, column=0)

        start_button = tk.Button(self, text="Next Vote", command = next_vote)
        start_button.grid(row=3, column=0 ,  pady= 10)

        terminate_button = tk.Button(self, text="Terminate", command=terminate_election)
        terminate_button.grid(row=4, column=0, pady=10)
