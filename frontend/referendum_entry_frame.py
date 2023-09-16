import tkinter as tk
import tkinter.messagebox
import tkinter.ttk as ttk
import traceback

from backend.db.Database import Database


# for easy access ref_entry is in referendum

class ReferendumEntryFrame(ttk.Frame):
    def __init__(self, app, context):
        super().__init__(app)
        poll = context['poll']
        num_proposals = poll['num_candidates']
        l1 = []

        l2 = []

        l3 = []
        def get_data():
            l4 = []
            l5 = []
            data = []
            for i in range(num_proposals):
                if l2[i].get() and l3[i].get():
                   l4.append(l2[i].get())
                   l5.append(l3[i].get())
                   data.append({"name" : l4[i], "description" : l5[i]})

                else:
                    tkinter.messagebox.showerror(title="Error", message='Proposal' + str(i+1) + 'data incomplete')
                    break
            try:
                print(data)
                db = Database.get_instance()
                db.register_proposals(poll['id'], data)
                app.show_frame('elec_navigation')
            except Exception as exc:
                traceback.print_exc()
                tk.messagebox.showerror(message=str(exc))





        self.frame = tk.Frame(self)
        self.frame.pack()

        ref_entry_frame = tk.LabelFrame(self.frame, text="referendum Entry")
        ref_entry_frame.grid(row=0, column=0, sticky="news")
        text_for_labels = ["Sno. ", "Title", "Description"]
        Labels = []
        for i in range(len((text_for_labels))):
            Labels.append(tk.Label(ref_entry_frame, text=text_for_labels[i]))
            Labels[i].grid(row=0, column=i, padx=50)


        for i in range(num_proposals):
           l1.append(tk.Label(ref_entry_frame, text="Proposal" + str(i + 1)))
           l2.append(tk.Entry(ref_entry_frame))
           l3.append(tk.Entry(ref_entry_frame))

           l1[i].grid(row=i+1, column=0)
           l2[i].grid(row=i+1, column=1 , padx=50, pady=10)
           l3[i].grid(row=i+1, column=2, padx=50, pady=10)


        button = tk.Button(ref_entry_frame, text="Submit" , command= get_data)

        button.grid(row=num_proposals+1, column=1)


