import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox
from backend.db.Database import Database
import traceback

#Rename file to data_entry
class CreateElectionFrame(ttk.Frame):
    def __init__(self, app, context):
        super().__init__(app)


        def enter_data():
            name_institution = name_institution_Entry.get()
            type_institution = type_institution_Entry.get()
            type = Type_of_election_Entry.get()
            type_codes = {
                'Approval voting': 'approval',
                'first past the post': 'fptp',
                'Instant Runoff': 'runoff'
            }
            type_code = type_codes[type]
            title_election = title_election_Entry.get()
            description = Description_Entry.get()
            num_candidates = No_Cand_Entry.get() 
            date_election = Date_Entry.get()
            number_voter = No_Voter_Entry.get()
            security_key = Sec_Key_Entry.get()
            tnc = tnc_var.get()
            min_threshold  = Min_thr_Key_Entry.get()
            max_approved = Max_app_Key_Entry.get()
            Alpha = 0
            l = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0]
            try:
                int(num_candidates)
                Alpha += 1
            except ValueError:
                l[0] = 1
            try:
                int(number_voter)
                Alpha += 1
            except ValueError:
                l[1] = 1
            if len(security_key) >= 8:
                Alpha += 1
            else:
                l[2] = 1
            if title_election and description and date_election:
                Alpha += 1
            else:
                l[3] = 1
            if tnc == 'Checked':
                Alpha += 1
            else:
                l[4] = 1
            if type:
                Alpha +=1
            else:
                l[5] = 1
            if max_approved:

                try:
                    int(max_approved)
                    if max_approved <= num_candidates:
                        Alpha +=1
                    else:
                        l[6] = 1
                    Alpha += 1
                except ValueError:
                    l[7] = 1
            else:
                max_approved = 1
                if int(min_threshold) == 0:
                    min_threshold = 50
                Alpha +=1
            Data_Entry = {"Name": name_institution, "Type of inst": type_institution, "Type_elec": type,
                          "title elec": title_election, "desc": description, "Num voter": number_voter,
                          "Num_can": num_candidates, "Date": date_election, "Sec_key": security_key,
                          "tnc": tnc, "min_thr": min_threshold, "max_app": max_approved}

            if l[0] == 1:
                tkinter.messagebox.showerror(title="Erroe101", message='Number of Candidataes must be integer')
            elif l[1] == 1:
                tkinter.messagebox.showerror(title="Error102", message='Number of Voters Must be integer')
            elif l[2] == 1:
                tkinter.messagebox.showerror(title="Error103", message='Security Key must be atleast 8 digit long')
            elif l[3] == 1:
                tkinter.messagebox.showerror(title="Error104",
                                             message='Title , Description and Date of Election Required')
            elif l[5] == 1:
                tkinter.messagebox.showerror(title="Error105", message="You have not selected the type of election")
            elif l[4] == 1:
                tkinter.messagebox.showerror(title="Error106", message="You have not accepted the Terms and Condition")
            elif l[7] == 1:
                tkinter.messagebox.showerror(title="Error107", message="max approved must be integer")
            elif l[6] == 1:
                tkinter.messagebox.showerror(title="Error108", message="max approved cant be more than total canditates")
            else:
                # save to db
                try:
                    db = Database.get_instance()
                    poll = db.create_poll(name=title_election, type=type_code, description=description, security_key=security_key, secure_mode=True, inst_name=name_institution, num_candidates=num_candidates, num_voters=number_voter, max_approved=max_approved, min_threshold=min_threshold)
                    print('Poll created: ', poll)

                    print('success')
                    app.show_frame('cand_entry', context={'poll': poll})
                except Exception as exc:
                    traceback.print_exc()
                    tkinter.messagebox.showerror(title='Error109', message=str(exc))

            return Data_Entry

        def do():
            che = Type_of_election_Entry.get()
            if che == "Approval voting":
                Min_thr_Key.grid(row=6, column=0)
                Min_thr_Key_Entry.grid(row=6, column=1, padx=50, pady=10)

                Max_app_Key.grid(row=7, column=0)
                Max_app_Key_Entry.grid(row=7, column=1, padx=50, pady=10)

            else:
                Min_thr_Key.grid_remove()
                Min_thr_Key_Entry.grid_remove()

                Max_app_Key.grid_remove()
                Max_app_Key_Entry.grid_remove()


        self.frame = tk.Frame(self)
        self.frame.pack()


        User_info_frame = tk.LabelFrame(self.frame, text="User Informaton")
        User_info_frame.grid(row=0, column=0, sticky="news")

        name_institution = tk.Label(User_info_frame, text="Name of the institution")
        name_institution.grid(row=0, column=0)
        name_institution_Entry = tk.Entry(User_info_frame)
        name_institution_Entry.grid(row=0, column=1, padx=50, pady=10)

        type_institution = tk.Label(User_info_frame, text="Type of the institution")
        type_institution.grid(row=1, column=0)
        type_institution_Entry = tk.Entry(User_info_frame)
        type_institution_Entry.grid(row=1, column=1, padx=50, pady=10)

        Type_of_election = tk.Label(User_info_frame, text="Type of election")
        Type_of_election.grid(row=2, column=0)
        Type_of_election_Entry = ttk.Combobox(User_info_frame, values= ["first past the post", "Instant Runoff" , "Approval voting"])
        Type_of_election_Entry.grid(row=2, column=1, padx=50, pady=10)

        update_button = tk.Button(User_info_frame , text="update" , command = do)
        update_button.grid(row=2 , column=2)



        Election_info_frame = tk.LabelFrame(self.frame, text="Election Information")
        Election_info_frame.grid(row=1, column=0, sticky="news")

        title_election = tk.Label(Election_info_frame, text="Title of Election")
        title_election_Entry = tk.Entry(Election_info_frame)
        title_election.grid(row=0, column=0)
        title_election_Entry.grid(row=0, column=1, padx=50, pady=10)


        Description = tk.Label(Election_info_frame, text="Desccription of Election")
        Description.grid(row=1, column=0)
        Description_Entry = tk.Entry(Election_info_frame)
        Description_Entry.grid(row=1, column=1, padx=50, pady=10)

        No_Cand = tk.Label(Election_info_frame, text="Number of Candidates")
        No_Cand.grid(row=2, column=0)
        No_Cand_Entry = tk.Entry(Election_info_frame)
        No_Cand_Entry.grid(row=2, column=1, padx=50, pady=10)

        Date = tk.Label(Election_info_frame, text="Date")
        Date.grid(row=3, column=0)
        Date_Entry = tk.Entry(Election_info_frame)
        Date_Entry.grid(row=3, column=1, padx=50, pady=10)

        No_Voter = tk.Label(Election_info_frame, text="Number of  Voters")
        No_Voter.grid(row=4, column=0)
        No_Voter_Entry = tk.Entry(Election_info_frame)
        No_Voter_Entry.grid(row=4, column=1, padx=50, pady=10)

        Sec_Key = tk.Label(Election_info_frame, text="Security Key")
        Sec_Key.grid(row=5, column=0)
        Sec_Key_Entry = tk.Entry(Election_info_frame)
        Sec_Key_Entry.grid(row=5, column=1, padx=50, pady=10)

        Min_thr_Key = tk.Label(Election_info_frame, text="minimum approval threshold")

        Min_thr_Key_Entry = tk.Spinbox(Election_info_frame , from_= 0 , to= 100)


        Max_app_Key = tk.Label(Election_info_frame, text="maximum approved")

        Max_app_Key_Entry = tk.Entry(Election_info_frame)


        Dec_frame = tk.LabelFrame(self.frame, text="Declaration")
        Dec_frame.grid(row=2, column=0, sticky="news")

        Dec_tnc = tk.Label(Dec_frame, text="Terms and Condition Declaration")
        tnc_var = tk.StringVar(value="Uncheked")
        Dec_tnc.grid(row=1, column=0)
        Dec_tnc_CB = tk.Checkbutton(Dec_frame, text="I accept all the T&C", variable=tnc_var,
                                    onvalue="Checked", offvalue="Uncheked")
        Dec_tnc_CB.grid(row=1, column=1, padx=50, pady=10)

        button1 = tk.Button(self.frame, text="SUBMIT", command=enter_data)
        button1.grid(row=3, column=0, sticky='news', padx=10
                     , pady=10)


