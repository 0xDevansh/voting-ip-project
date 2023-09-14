import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox

from backend.db.Database import Database


#Rename file to data_entry
class CreateReferendumFrame(ttk.Frame):
    def __init__(self, app, context):
        super().__init__(app)


        def enter_data():
            name_institution = name_institution_Entry.get()
            type_institution = type_institution_Entry.get()
            title_referendum = title_referendum_Entry.get()
            description = Description_Entry.get()
            num_candidates = No_Cand_Entry.get() 
            date_referendum = Date_Entry.get()
            number_voter = No_Voter_Entry.get()
            security_key = Sec_Key_Entry.get()
            tnc = tnc_var.get()
            min_threshold  = Min_thr_Key_Entry.get()
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
            if title_referendum and description and date_referendum:
                Alpha += 1
            else:
                l[3] = 1
            if tnc == 'Checked':
                Alpha += 1
            else:
                l[4] = 1
            if int(min_threshold) == 0:
                min_threshold = 50
            Data_Entry = {"Name": name_institution, "Type_of_inst": type_institution,
                          "title_elec": title_referendum, "desc": description, "Num_voter": number_voter,
                          "Num_can": num_candidates, "Date": date_referendum, "Sec_key": security_key,
                          "tnc": tnc}

            if l[0] == 1:
                tkinter.messagebox.showerror(title="Erroe101", message='Number of Candidataes must be integer')
            elif l[1] == 1:
                tkinter.messagebox.showerror(title="Error102", message='Number of Voters Must be integer')
            elif l[2] == 1:
                tkinter.messagebox.showerror(title="Error103", message='Security Key must be atleast 8 digit long')
            elif l[3] == 1:
                tkinter.messagebox.showerror(title="Error104",
                                             message='Title , Description and Date of referendum Required')
            elif l[5] == 1:
                tkinter.messagebox.showerror(title="Error105", message="You have not selected the type of referendum")
            elif l[4] == 1:
                tkinter.messagebox.showerror(title="Error106", message="You have not accepted the Terms and Condition")
            else:
                # save to db
                try:
                    db = Database.get_instance()
                    poll = db.create_poll(name=title_referendum, type='referendum', description=description,
                                          security_key=security_key, secure_mode=True, inst_name=name_institution,
                                          num_candidates=num_candidates, num_voters=number_voter,
                                          min_threshold=min_threshold)
                    print('Poll created: ', poll)
                    app.show_frame('cand_entry', context={'poll': poll})
                except Exception as exc:
                    print(exc)
                    tkinter.messagebox.showerror(title='Error109', message=str(exc))
            return Data_Entry



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




        referendum_info_frame = tk.LabelFrame(self.frame, text="referendum Information")
        referendum_info_frame.grid(row=1, column=0, sticky="news")

        title_referendum = tk.Label(referendum_info_frame, text="Title of referendum")
        title_referendum_Entry = tk.Entry(referendum_info_frame)
        title_referendum.grid(row=0, column=0)
        title_referendum_Entry.grid(row=0, column=1, padx=50, pady=10)


        Description = tk.Label(referendum_info_frame, text="Description of referendum")
        Description.grid(row=1, column=0)
        Description_Entry = tk.Entry(referendum_info_frame)
        Description_Entry.grid(row=1, column=1, padx=50, pady=10)

        No_Cand = tk.Label(referendum_info_frame, text="Number of Referendum")
        No_Cand.grid(row=2, column=0)
        No_Cand_Entry = tk.Entry(referendum_info_frame)
        No_Cand_Entry.grid(row=2, column=1, padx=50, pady=10)

        Date = tk.Label(referendum_info_frame, text="Date")
        Date.grid(row=3, column=0)
        Date_Entry = tk.Entry(referendum_info_frame)
        Date_Entry.grid(row=3, column=1, padx=50, pady=10)

        No_Voter = tk.Label(referendum_info_frame, text="Number of  Voters")
        No_Voter.grid(row=4, column=0)
        No_Voter_Entry = tk.Entry(referendum_info_frame)
        No_Voter_Entry.grid(row=4, column=1, padx=50, pady=10)

        Sec_Key = tk.Label(referendum_info_frame, text="Security Key")
        Sec_Key.grid(row=5, column=0)
        Sec_Key_Entry = tk.Entry(referendum_info_frame)
        Sec_Key_Entry.grid(row=5, column=1, padx=50, pady=10)

        Min_thr_Key = tk.Label(referendum_info_frame, text="minimum approval threshold")
        Min_thr_Key.grid(row=6, column=0)
        Min_thr_Key_Entry = tk.Spinbox(referendum_info_frame , from_= 0 , to= 100)
        Min_thr_Key_Entry.grid(row=6, column=1, padx=50, pady=10)



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