import tkinter as tk
import tkinter.messagebox
import tkinter.ttk as ttk
import traceback
from backend.db.Database import Database
from frontend.utils import snake_case


class CreateElectionFrame(ttk.Frame):
    def __init__(self, app, context):
        super().__init__(app)

        # Function to handle the submission of election data
        def enter_data():
            # Extracting data from input fields
            name_institution = name_institution_Entry.get()
            election_type = Type_of_election_Entry.get()

            # Mapping election type to code
            type_codes = {
                'Approval Voting': 'approval',
                'First Past the Post': 'fptp',
                'Instant Runoff': 'runoff'
            }
            type_code = type_codes.get(election_type)

            title_election = title_election_Entry.get()
            description = Description_Entry.get()
            num_candidates = No_Cand_Entry.get()
            number_voter = No_Voter_Entry.get()
            security_key = Sec_Key_Entry.get()
            tnc = tnc_var.get()
            min_threshold = Min_thr_Key_Entry.get()
            max_approved = Max_app_Key_Entry.get()

            # Variables for validation
            Alpha = 0
            l = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

            # Validation: Checking if certain fields are integers
            try:
                int(num_candidates)
            except ValueError:
                l[0] = 1

            try:
                int(number_voter)
            except ValueError:
                l[1] = 1

            # Validation: Checking security key length
            if len(security_key) < 8:
                l[2] = 1

            # Validation: Checking if title and description are provided
            if not (title_election and description):
                l[3] = 1

            # Validation: Checking if terms and conditions are accepted
            if tnc != 'Checked':
                l[4] = 1

            # Validation: Checking if a valid election type is selected
            if election_type not in ["First Past the Post", "Instant Runoff", "Approval Voting"]:
                l[5] = 1

            # Validation: Checking specific conditions for 'Approval Voting' type
            if election_type == "Approval Voting" and max_approved:
                try:
                    int(max_approved)
                    if max_approved > num_candidates:
                        l[6] = 1
                except ValueError:
                    l[7] = 1
            else:
                try:
                    max_approved = None
                    int(min_threshold)
                    if int(min_threshold) == 0:
                        min_threshold = None
                except ValueError:
                    min_threshold = None

            # Creating a dictionary with entered data
            Data_Entry = {
                "Name": name_institution, "Type_elec": election_type,
                "title elec": title_election, "desc": description,
                "Num voter": number_voter, "Num_can": num_candidates,
                "Sec_key": security_key, "tnc": tnc,
                "min_thr": min_threshold, "max_app": max_approved
            }

            # Handling validation errors
            if l[0] == 1:
                tkinter.messagebox.showerror(title="Error101", message='Number of Candidates must be integer')
            elif l[1] == 1:
                tkinter.messagebox.showerror(title="Error102", message='Number of Voters Must be integer')
            elif l[2] == 1:
                tkinter.messagebox.showerror(title="Error103",
                                             message='Security Key must be at least 8 characters long')
            elif l[3] == 1:
                tkinter.messagebox.showerror(title="Error104",
                                             message='Title, Description, and Date of Election Required')
            elif l[5] == 1:
                tkinter.messagebox.showerror(title="Error105", message="You have not selected the type of election")
            elif l[4] == 1:
                tkinter.messagebox.showerror(title="Error106", message="You have not accepted the Terms and Condition")
            elif l[7] == 1:
                tkinter.messagebox.showerror(title="Error107", message="max approved must be an integer")
            elif l[6] == 1:
                tkinter.messagebox.showerror(title="Error108",
                                             message="max approved can't be more than total candidates")
            else:
                # Save to database
                try:
                    db = Database.get_instance()
                    poll = db.create_poll(name=title_election, type=type_code, description=description,
                                          security_key=security_key, secure_mode=True, inst_name=name_institution,
                                          num_candidates=num_candidates, num_voters=number_voter,
                                          max_approved=max_approved, min_threshold=min_threshold)
                    app.show_frame('cand_entry', context={'poll': poll})
                except Exception as exc:
                    traceback.print_exc()
                    tkinter.messagebox.showerror(title='Error109', message=str(exc))

            return Data_Entry

        # Function to change the visibility of certain fields based on the election type selected
        def change_election_type(event):
            elec_type = Type_of_election_Entry.get()

            # Check if a valid election type is selected
            if elec_type in ["First Past the Post", "Instant Runoff", "Approval Voting"]:
                Election_info_frame.grid(row=1, column=0, sticky="news")
                Dec_frame.grid(row=2, column=0, sticky="news")
                button1.grid(row=3, column=0, sticky='news', padx=10, pady=10)
            else:
                tkinter.messagebox.showerror(message="Please select a valid choice", title="Error")

            # Check if the selected election type is 'Approval Voting'
            if elec_type == "Approval Voting":
                Min_thr_Key.grid(row=6, column=0)
                Min_thr_Key_Entry.grid(row=6, column=1, padx=50, pady=10)
                Max_app_Key.grid(row=7, column=0)
                Max_app_Key_Entry.grid(row=7, column=1, padx=50, pady=10)
            else:
                Min_thr_Key.grid_remove()
                Min_thr_Key_Entry.grid_remove()
                Max_app_Key.grid_remove()
                Max_app_Key_Entry.grid_remove()

        # Main Frame
        self.frame = ttk.Frame(self)
        self.frame.pack()

        # User Information Frame
        User_info_frame = ttk.LabelFrame(self.frame, text="User Information")
        User_info_frame.grid(row=0, column=0, sticky="news")
        for i in range(2):
            User_info_frame.grid_rowconfigure(i, weight=1)
        for i in range(2):
            User_info_frame.grid_columnconfigure(i, weight=1)

        # Labels and entry boxes for user information
        name_institution = ttk.Label(User_info_frame, text="Name of the institution")
        name_institution.grid(row=0, column=0)
        name_institution_Entry = ttk.Entry(User_info_frame)
        name_institution_Entry.grid(row=0, column=1, padx=50, pady=10)

        Type_of_election = ttk.Label(User_info_frame, text="Type of election")
        Type_of_election.grid(row=2, column=0)
        Type_of_election_Entry = ttk.Combobox(User_info_frame,
                                              values=["First Past the Post", "Instant Runoff", "Approval Voting"])
        Type_of_election_Entry.grid(row=2, column=1, padx=50, pady=10, sticky='ew')
        Type_of_election_Entry.bind("<<ComboboxSelected>>", change_election_type)

        # Election Information Frame
        Election_info_frame = ttk.LabelFrame(self.frame, text="Election Information")
        for i in range(8):
            Election_info_frame.grid_rowconfigure(i, weight=1)
        for i in range(2):
            Election_info_frame.grid_columnconfigure(i, weight=1)

        # Labels and entry boxes for election information
        title_election = ttk.Label(Election_info_frame, text="Title of Election")
        title_election_Entry = ttk.Entry(Election_info_frame)
        title_election.grid(row=0, column=0)
        title_election_Entry.grid(row=0, column=1, padx=50, pady=10)

        Description = ttk.Label(Election_info_frame, text="Description of Election")
        Description.grid(row=1, column=0)
        Description_Entry = ttk.Entry(Election_info_frame)
        Description_Entry.grid(row=1, column=1, padx=50, pady=10)

        No_Cand = ttk.Label(Election_info_frame, text="Number of Candidates")
        No_Cand.grid(row=2, column=0)
        No_Cand_Entry = ttk.Entry(Election_info_frame)
        No_Cand_Entry.grid(row=2, column=1, padx=50, pady=10)

        No_Voter = ttk.Label(Election_info_frame, text="Number of Voters")
        No_Voter.grid(row=4, column=0)
        No_Voter_Entry = ttk.Entry(Election_info_frame)
        No_Voter_Entry.grid(row=4, column=1, padx=50, pady=10)

        Sec_Key = ttk.Label(Election_info_frame, text="Security Key")
        Sec_Key.grid(row=5, column=0)
        Sec_Key_Entry = ttk.Entry(Election_info_frame)
        Sec_Key_Entry.grid(row=5, column=1, padx=50, pady=10)

        Min_thr_Key = ttk.Label(Election_info_frame, text="Minimum Approval Threshold (%)")
        Min_thr_Key_Entry = ttk.Spinbox(Election_info_frame, from_=0, to=100)

        Max_app_Key = ttk.Label(Election_info_frame, text="Maximum Approved")
        Max_app_Key_Entry = ttk.Entry(Election_info_frame)

        # Declaration Frame
        Dec_frame = ttk.LabelFrame(self.frame, text="Declaration")
        terms_and_conditions = ''
        with open('frontend/tos.txt') as file:
            terms_and_conditions = file.read()

        Dec_tnc = ttk.Label(Dec_frame, text="Terms and Condition Declaration")
        tnc_var = tk.StringVar(value="Unchecked")

        # Function to show terms and conditions
        def show_tnc():
            tkinter.messagebox.showinfo(title='Terms and Condition', message=terms_and_conditions)

        Dec_tnc_Button = ttk.Button(Dec_frame, text="Show T&C", command=show_tnc)
        Dec_tnc_Button.grid(row=2, column=0, padx=50)
        Dec_tnc.grid(row=1, column=0)
        Dec_tnc_CB = ttk.Checkbutton(Dec_frame, text="I accept all the T&C", variable=tnc_var,
                                     onvalue="Checked", offvalue="Unchecked")
        Dec_tnc_CB.grid(row=1, column=1, padx=50, pady=10)

        # Submit Button
        button1 = ttk.Button(self.frame, text="Submit", command=enter_data)

        # Button Frame
        Button_frame = ttk.LabelFrame(self.frame)
        Button_frame.grid(row=4, column=0, sticky="news")
        for i in range(3):
            Button_frame.grid_columnconfigure(i, weight=1)

        # Help and Homepage Buttons
        def help():
            tkinter.messagebox.showinfo(title="Help", message="The 'Create Election' window is where users can set up a new election within the voting app, specifying essential details for the upcoming vote.")

        button_help = ttk.Button(Button_frame, text="Help", command=help)
        button_help.grid(row=0, column=0, sticky='news', padx=10, pady=10)

        button_homepage = ttk.Button(Button_frame, text="Go to Homepage", command=app.show_frame_factory('opening'))
        button_homepage.grid(row=0, column=2, sticky='news', padx=10, pady=10)




