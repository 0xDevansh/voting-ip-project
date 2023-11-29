import tkinter as tk
import tkinter.messagebox
import tkinter.ttk as ttk
import traceback

from backend.db.Database import Database


# Create a frame for entering referendum information
class ReferendumEntryFrame(ttk.Frame):
    def __init__(self, app, context):
        super().__init__(app)
        poll = context['poll']
        num_proposals = poll['num_candidates']

        # Lists to store labels, entry widgets, and proposal data
        proposal_number_labels = []  # Labels for proposal numbers
        proposal_title_entries = []  # Entry widgets for proposal titles
        proposal_description_entries = []  # Entry widgets for proposal descriptions

        def get_data():
            # Lists to store proposal titles and descriptions
            proposal_titles = []
            proposal_descriptions = []
            data = []

            # Iterate through each proposal entry
            for i in range(num_proposals):
                # Check if both title and description are provided for each proposal
                if proposal_title_entries[i].get() and proposal_description_entries[i].get():
                    proposal_titles.append(proposal_title_entries[i].get())
                    proposal_descriptions.append(proposal_description_entries[i].get())
                    data.append({"name": proposal_titles[i], "description": proposal_descriptions[i]})
                else:
                    # Show error if any proposal data is incomplete
                    tkinter.messagebox.showerror(title="Error", message=f'Proposal {i + 1} data incomplete')
                    break

            try:
                # Register proposals in the database
                db = Database.get_instance()
                db.register_proposals(poll['id'], data)
                app.show_frame('elec_navigation')
            except Exception as exc:
                # Handle exceptions and show error message
                traceback.print_exc()
                ttk.messagebox.showerror(message=str(exc))

        # Create a frame to hold the referendum entry widgets
        self.frame = ttk.Frame(self)
        self.frame.pack()

        ref_entry_frame = ttk.LabelFrame(self.frame, text="Referendum Entry")
        ref_entry_frame.grid(row=0, column=0, sticky="news")

        # Create labels for Sno., Title, and Description
        label_texts = ["Sno. ", "Title", "Description"]
        labels = []
        for i in range(len(label_texts)):
            labels.append(ttk.Label(ref_entry_frame, text=label_texts[i]))
            labels[i].grid(row=0, column=i, padx=50)

        # Create entry widgets for each proposal
        for i in range(num_proposals):
            proposal_number_labels.append(ttk.Label(ref_entry_frame, text=f"Proposal {i + 1}"))
            proposal_title_entries.append(ttk.Entry(ref_entry_frame))
            proposal_description_entries.append(ttk.Entry(ref_entry_frame))

            proposal_number_labels[i].grid(row=i + 1, column=0)
            proposal_title_entries[i].grid(row=i + 1, column=1, padx=50, pady=10)
            proposal_description_entries[i].grid(row=i + 1, column=2, padx=50, pady=10)

        # Create a submit button to trigger data submission
        submit_button = ttk.Button(ref_entry_frame, text="Submit", command=get_data)
        submit_button.grid(row=num_proposals + 1, column=1)
