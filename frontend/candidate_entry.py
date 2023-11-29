import tkinter as tk
import tkinter.messagebox
import tkinter.ttk as ttk
import traceback

from backend.db.Database import Database
from frontend.utils import snake_case


class CandidateEntryFrame(ttk.Frame):
    def __init__(self, app, context):
        super().__init__(app)
        poll = context['poll']
        num_candidates = poll['num_candidates']
        Candidate_Number_Label = []
        Candidate_Name_Entry = []
        Candidate_Faction_Entry = []
        Candidate_Name_data = []
        Candidate_Faction_data = []

        def get_data():
            # Retrieve input data
            data = []
            for i in range(num_candidates):
                if Candidate_Name_Entry[i].get() and Candidate_Faction_Entry[i].get():
                    Candidate_Name_data.append(Candidate_Name_Entry[i].get())
                    Candidate_Faction_data.append(Candidate_Faction_Entry[i].get())
                    data.append({"name": Candidate_Name_data[i], "faction": Candidate_Faction_data[i]})
                else:
                    tk.messagebox.showerror(title="Error", message='Candidate' + str(i + 1) + ' data incomplete')
                    Candidate_Name_data.clear()
                    Candidate_Faction_data.clear()
                    return

            # Send data to the database
            try:
                db = Database.get_instance()
                db_candidates = []
                cand_ids = []
                for cand in data:
                    candidate_id = snake_case(cand['name'])
                    if candidate_id in cand_ids:
                        tk.messagebox.showerror(title="Error", message='Candidate names are too similar!')
                        cand_ids.clear()
                        return
                    cand_ids.append(candidate_id)
                    db_candidates.append({'candidate_id': candidate_id, 'name': cand['name'], 'faction': cand['faction']})
                db.register_candidates(poll['id'], db_candidates)
                app.show_frame('elec_navigation')
            except Exception as exc:
                traceback.print_exc()
                tk.messagebox.showerror(message=str(exc))

        self.frame = tk.Frame(self)
        self.frame.pack()

        Cand_entry_frame = tk.LabelFrame(self.frame, text="Candidate Entry")
        Cand_entry_frame.grid(row=0, column=0, sticky="news")
        text_for_labels = ["Sno. ", "Name", "Faction"]
        Labels = []

        # Create labels for sno, name, and faction
        for i in range(len(text_for_labels)):
            Labels.append(tk.Label(Cand_entry_frame, text=text_for_labels[i]))
            Labels[i].grid(row=0, column=i, padx=50)

        # Place Labels and Entry boxes
        for i in range(num_candidates):
            Candidate_Number_Label.append(tk.Label(Cand_entry_frame, text="Candidate" + str(i + 1)))
            Candidate_Name_Entry.append(tk.Entry(Cand_entry_frame))
            Candidate_Faction_Entry.append(tk.Entry(Cand_entry_frame))

            Candidate_Number_Label[i].grid(row=i + 1, column=0)
            Candidate_Name_Entry[i].grid(row=i + 1, column=1, padx=50, pady=10)
            Candidate_Faction_Entry[i].grid(row=i + 1, column=2, padx=50, pady=10)

        # Submit button
        button = tk.Button(Cand_entry_frame, text="Submit", command=get_data)
        button.grid(row=num_candidates + 1, column=1)







