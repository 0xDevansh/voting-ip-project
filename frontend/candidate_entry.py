import tkinter as tk
import tkinter.messagebox
import tkinter.ttk as ttk
import traceback

from backend.db.Database import Database
from frontend.utils import snake_case


# for easy access cand_entry is in referendum

class CandidateEntryFrame(ttk.Frame):
    def __init__(self, app, context):
        super().__init__(app)
        poll =context['poll']
        num_candidates = poll['num_candidates']
        l1 = []

        l2 = []

        l3 = []
        l4 = []
        l5 = []
        def get_data():
            data = []
            for i in range(num_candidates):
                if l2[i].get() and l3[i].get():
                   l4.append(l2[i].get())
                   l5.append(l3[i].get())
                   data.append({"name" : l4[i], "faction" : l5[i]})

                else:
                    tkinter.messagebox.showerror(title="Error", message='Candidate' + str(i+1) + 'data incomplete')
                    l4.clear()
                    l5.clear()
                    return

            try:
                db = Database.get_instance()
                db_candidates = []
                cand_ids = []
                for cand in data:
                    candidate_id = snake_case(cand['name'])
                    if candidate_id in cand_ids:
                        tkinter.messagebox.showerror(title="Error", message='Candidate names are too similar!')
                        cand_ids.clear()
                        return
                    cand_ids.append(candidate_id)
                    db_candidates.append({'candidate_id': candidate_id, 'name': cand['name'], 'faction': cand['faction'] })
                db.register_candidates(poll['id'], db_candidates)
                print('Registered candidates:', db_candidates)
                app.show_frame('elec_navigation')
            except Exception as exc:
                traceback.print_exc()
                tk.messagebox.showerror(message=str(exc))




        self.frame = tk.Frame(self)
        self.frame.pack()

        Cand_entry_frame = tk.LabelFrame(self.frame, text="Candidate Entry")
        Cand_entry_frame.grid(row=0, column=0, sticky="news")
        text_for_labels = ["Sno. ", "Name", "faction"]
        Labels = []
        for i in range(len((text_for_labels))):
            Labels.append(tk.Label(Cand_entry_frame, text=text_for_labels[i]))
            Labels[i].grid(row=0, column=i, padx=50)


        for i in range(num_candidates):
           l1.append(tk.Label(Cand_entry_frame, text="Candidate" + str(i + 1)))
           l2.append(tk.Entry(Cand_entry_frame))
           l3.append(tk.Entry(Cand_entry_frame))

           l1[i].grid(row=i+1, column=0)
           l2[i].grid(row=i+1, column=1 , padx=50, pady=10)
           l3[i].grid(row=i+1, column=2, padx=50, pady=10)


        button = tk.Button(Cand_entry_frame, text="Submit" , command= get_data)

        button.grid(row=num_candidates+1, column=1)





#        toe_button = tk.Button(Cand_entry_frame, text="o", )
 #       toe_button.grid(row=0, column=2)




