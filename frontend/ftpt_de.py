import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox

#Rename file to data_entry
class ele_de_frame(ttk.Frame):
    def __init__(self, app):
        super().__init__(app)


        def enter_data():
            name_inst = Name_Inst_Entry.get()
            type_inst_ = type_Inst_Entry.get()
            Type = Type_of_election_Entry.get()
            title_elc = Title_elc_Entry.get()
            description = Description_Entry.get()
            Num_candi = No_Cand_Entry.get()
            Date_elec = Date_Entry.get()
            Num_voter = No_Voter_Entry.get()
            Security_Key = Sec_Key_Entry.get()
            Tac = Tac_var.get()
            min_threshold  = Min_thr_Key_Entry.get()
            max_approved = Max_app_Key_Entry.get()
            Alpha = 0
            l = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0]
            try:
                int(Num_candi)
                Alpha += 1
            except ValueError:
                l[0] = 1
            try:
                int(Num_voter)
                Alpha += 1
            except ValueError:
                l[1] = 1
            if len(Security_Key) >= 8:
                Alpha += 1
            else:
                l[2] = 1
            if title_elc and description and Date_elec:
                Alpha += 1
            else:
                l[3] = 1
            if Tac == 'Checked':
                Alpha += 1
            else:
                l[4] = 1
            if Type:
                Alpha +=1
            else:
                l[5] = 1
            if int(min_threshold) == 0:
                min_threshold = 50
            elif min_threshold:
                pass
            else:
                min_threshold = 50
            if max_approved:
                try:
                    int(max_approved)
                    if max_approved <= Num_candi:
                        Alpha +=1
                    else:
                        l[6] = 1
                    Alpha += 1
                except ValueError:
                    l[7] = 1
            else:
                max_approved = 1
                Alpha +=1
            Data_Entry = {"Name": name_inst, "Type of inst": type_inst_, "Type_elec": Type,
                          "title elec": title_elc, "desc": description, "Num voter": Num_voter,
                          "Num_can": Num_candi, "Date": Date_elec, "Sec_key": Security_Key,
                          "Tac": Tac, "min_thr": min_threshold, "max_app": max_approved}
            if Alpha == 8:
                print("succsess")
                app.show_frame('opening')
                print(Data_Entry)
            elif l[0] == 1:
                tkinter.messagebox.showerror(title="Erroe101", message='Number of Candidataes must be integer')
            elif l[1] == 1:
                tkinter.messagebox.showerror(title="Error102", message='Number of Voters Must be integer')
            elif l[2] == 1:
                tkinter.messagebox.showerror(title="Error103", message='Password must be atleast 8 digit long')
            elif l[3] == 1:
                tkinter.messagebox.showerror(title="Error104",
                                             message='Title , Description and Date of Election Required')
            elif l[5] == 1:
                tkinter.messagebox.showerror(title="Error105", message="You have not selected the type of election")
            elif l[4] == 1:
                tkinter.messagebox.showerror(title="Error106", message="You have not accepted the Terms and Condition")
            elif l[7] == 1:
                tkinter.messagebox.showerror(title="Error106", message="max approved must be integer")
            elif l[6] == 1:
                tkinter.messagebox.showerror(title="Error107", message="max approved cant be more than total canditates")

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

        Name_Inst = tk.Label(User_info_frame, text="Name of the institution")
        Name_Inst.grid(row=0, column=0)
        Name_Inst_Entry = tk.Entry(User_info_frame)
        Name_Inst_Entry.grid(row=0, column=1, padx=50, pady=10)

        type_Inst = tk.Label(User_info_frame, text="Type of the institution")
        type_Inst.grid(row=1, column=0)
        type_Inst_Entry = tk.Entry(User_info_frame)
        type_Inst_Entry.grid(row=1, column=1, padx=50, pady=10)

        Type_of_election = tk.Label(User_info_frame, text="Type of election")
        Type_of_election.grid(row=2, column=0)
        Type_of_election_Entry = ttk.Combobox(User_info_frame, values= ["first past the post", "Instant Runoff" , "Approval voting"])
        Type_of_election_Entry.grid(row=2, column=1, padx=50, pady=10)
        toe_button = tk.Button(User_info_frame , text="o" , command = do)
        toe_button.grid(row=2 , column=2)



        Election_info_frame = tk.LabelFrame(self.frame, text="Election Information")
        Election_info_frame.grid(row=1, column=0, sticky="news")

        Title_elc = tk.Label(Election_info_frame, text="Title of Election")
        Title_elc_Entry = tk.Entry(Election_info_frame)
        Title_elc.grid(row=0, column=0)
        Title_elc_Entry.grid(row=0, column=1, padx=50, pady=10)


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

        Dec_TaC = tk.Label(Dec_frame, text="Terms and Condition Declaration")
        Tac_var = tk.StringVar(value="Uncheked")
        Dec_TaC.grid(row=1, column=0)
        Dec_TaC_CB = tk.Checkbutton(Dec_frame, text="I accept all the T&C", variable=Tac_var,
                                    onvalue="Checked", offvalue="Uncheked")
        Dec_TaC_CB.grid(row=1, column=1, padx=50, pady=10)

        button1 = tk.Button(self.frame, text="SUBMIT", command=enter_data)
        button1.grid(row=3, column=0, sticky='news', padx=10
                     , pady=10)

