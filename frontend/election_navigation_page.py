import tkinter as tk
import tkinter.messagebox
import tkinter.ttk as ttk
import traceback

from backend.db.Database import Database


class ElectionNavigationFrame(ttk.Frame):
    def __init__(self, app, context):
        super().__init__(app)

        # Create a frame for the Election Navigation
        self.frame = ttk.Frame(self)
        self.frame.pack()

        try:
            # Fetch election information from the database
            db = Database.get_instance()
            polls = db.get_poll()
        except Exception as exc:
            # Handle exceptions and show error message
            traceback.print_exc()
            tk.messagebox.showerror(message=str(exc))

        # Create a label frame for displaying election information
        election_nav_frame = ttk.LabelFrame(self.frame)
        election_nav_frame.grid(row=0, column=0, sticky="news")

        # Labels for Election information
        text_for_labels = ["Election name", "Type", "Status", "Commands"]
        Labels = []
        for i in range(len(text_for_labels)):
            Labels.append(ttk.Label(election_nav_frame, text=text_for_labels[i]))
            Labels[i].grid(row=0, column=i, padx=50)

        # Lists to store labels and buttons
        Elec_name_label = []
        Elec_type_label = []
        Elec_status_Label = []
        Elec_command_button_1 = []

        # Dictionaries for poll types and status
        poll_types = {
            'fptp': 'First past the post',
            'runoff': 'Runoff',
            'referendum': 'Referendum',
            'approval': 'Approval voting',
        }
        poll_status = {
            'not_started': 'Not started',
            'running': 'In progress',
            'completed': 'Completed',
        }

        # Create labels and buttons for each poll
        for i, poll in enumerate(polls):
            Elec_name_label.append(ttk.Label(election_nav_frame, text=poll['name']))
            Elec_type_label.append(ttk.Label(election_nav_frame, text=poll_types[poll['type']]))
            Elec_status_Label.append(ttk.Label(election_nav_frame, text=poll_status[poll['status']]))

            Elec_name_label[i].grid(row=i + 1, column=0, padx=50, sticky='news')
            Elec_type_label[i].grid(row=i + 1, column=1, padx=50, sticky='news')
            Elec_status_Label[i].grid(row=i + 1, column=2, padx=50, sticky='news')

            # Add buttons based on poll status
            if poll['status'] == 'not_started':
                Elec_command_button_1.append(
                    ttk.Button(election_nav_frame, text="Start Election", command=app.show_frame_factory("start_election", {'poll': poll})))
            elif poll['status'] == "running":
                Elec_command_button_1.append(
                    ttk.Button(election_nav_frame, text='Add vote/Terminate', command=app.show_frame_factory('voting_security_check', {'poll': poll})))
            elif poll['status'] == 'completed':
                Elec_command_button_1.append(
                    ttk.Button(election_nav_frame, text='See Result', command=app.show_frame_factory('result_page', {'poll': poll})))

            Elec_command_button_1[i].grid(row=i + 1, column=3, padx=50, pady=10, sticky='news')

        # Create a button frame for Help and Back buttons
        Button_frame = ttk.LabelFrame(self.frame)
        Button_frame.grid(row=3, column=0, sticky="news")
        for i in range(3):
            Button_frame.grid_columnconfigure(i, weight=1)

        # Function for Help button
        def Help():
            tkinter.messagebox.showinfo(title="Help", message="Take Data from Documentation")

        # Create Help and Back buttons
        button1 = ttk.Button(Button_frame, text="Help", command=Help)
        button1.grid(row=0, column=0, sticky='news', padx=10, pady=10)
        button2 = ttk.Button(Button_frame, text="Back to Home Page", command=app.show_frame_factory('opening'))
        button2.grid(row=0, column=2, sticky='news', padx=10, pady=10)
