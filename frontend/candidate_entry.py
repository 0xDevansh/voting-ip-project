import tkinter as tk
import tkinter.messagebox
import tkinter.ttk as ttk
from backend.db.Database import Database


# for easy access cand_entry is in referendum

class CandidateEntryFrame(ttk.Frame):
    def __init__(self, app, context):
        super().__init__(app)
        num_candidates = 5
        l1 = []

        l2 = []

        l3 = []
        l4 = []
        l5 = []
        Data = {}
        def get_data():
            for i in range(num_candidates):
                if l2[i].get() and l3[i].get():
                   l4.append(l2[i].get())
                   l5.append(l3[i].get())
                   Data['candidate ' + str(i+1)] = {"candidate_name" : l4[i], "Party" : l5[i]}

                else:
                    tkinter.messagebox.showerror(title="Error", message='Candidate' + str(i+1) + 'data incomplete')
                    break

            print(l4)
            print(Data)
            app.show_frame('start_election')



        self.frame = tk.Frame(self)
        self.frame.pack()

        Cand_entry_frame = tk.LabelFrame(self.frame, text="Candidate Entry")
        Cand_entry_frame.grid(row=0, column=0, sticky="news")


        for i in range(num_candidates):
           l1.append(tk.Label(Cand_entry_frame, text="Candidate" + str(i + 1)))
           l2.append(tk.Entry(Cand_entry_frame))
           l3.append(tk.Entry(Cand_entry_frame))

           l1[i].grid(row=i, column=0)
           l2[i].grid(row=i, column=1 , padx=50, pady=10)
           l3[i].grid(row=i, column=2, padx=50, pady=10)


        button = tk.Button(Cand_entry_frame, text="Submit" , command= get_data)

        button.grid(row=num_candidates, column=1)



#        toe_button = tk.Button(Cand_entry_frame, text="o", )
 #       toe_button.grid(row=0, column=2)




