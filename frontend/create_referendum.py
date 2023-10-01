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
                min_threshold = None
            Data_Entry = {"Name": name_institution,
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
                    print('Referendum created: ', poll)
                    app.show_frame('ref_entry', context={'poll': poll})
                except Exception as exc:
                    print(exc)
                    tkinter.messagebox.showerror(title='Error109', message=str(exc))
                finally:
                    return Data_Entry



        self.frame = ttk.Frame(self)
        self.frame.pack()

        User_info_frame = ttk.LabelFrame(self.frame, text="User Informaton")
        User_info_frame.grid(row=0, column=0, sticky="news")

        name_institution = ttk.Label(User_info_frame, text="Name of the institution")
        name_institution.grid(row=0, column=0)
        name_institution_Entry = ttk.Entry(User_info_frame)
        name_institution_Entry.grid(row=0, column=1, padx=50, pady=10)



        referendum_info_frame = ttk.LabelFrame(self.frame, text="Referendum Information")
        referendum_info_frame.grid(row=1, column=0, sticky="news")

        title_referendum = ttk.Label(referendum_info_frame, text="Title of referendum")
        title_referendum_Entry = ttk.Entry(referendum_info_frame)
        title_referendum.grid(row=0, column=0)
        title_referendum_Entry.grid(row=0, column=1, padx=50, pady=10)


        Description = ttk.Label(referendum_info_frame, text="Description of referendum")
        Description.grid(row=1, column=0)
        Description_Entry = ttk.Entry(referendum_info_frame)
        Description_Entry.grid(row=1, column=1, padx=50, pady=10)

        No_Cand = ttk.Label(referendum_info_frame, text="Number of Proposals")
        No_Cand.grid(row=2, column=0)
        No_Cand_Entry = ttk.Entry(referendum_info_frame)
        No_Cand_Entry.grid(row=2, column=1, padx=50, pady=10)

        Date = ttk.Label(referendum_info_frame, text="Date")
        Date.grid(row=3, column=0)
        Date_Entry = ttk.Entry(referendum_info_frame)
        Date_Entry.grid(row=3, column=1, padx=50, pady=10)

        No_Voter = ttk.Label(referendum_info_frame, text="Number of  Voters")
        No_Voter.grid(row=4, column=0)
        No_Voter_Entry = ttk.Entry(referendum_info_frame)
        No_Voter_Entry.grid(row=4, column=1, padx=50, pady=10)

        Sec_Key = ttk.Label(referendum_info_frame, text="Security Key")
        Sec_Key.grid(row=5, column=0)
        Sec_Key_Entry = ttk.Entry(referendum_info_frame)
        Sec_Key_Entry.grid(row=5, column=1, padx=50, pady=10)

        Min_thr_Key = ttk.Label(referendum_info_frame, text="minimum approval threshold")
        Min_thr_Key.grid(row=6, column=0)
        Min_thr_Key_Entry = ttk.Spinbox(referendum_info_frame , from_= 0 , to= 100)
        Min_thr_Key_Entry.grid(row=6, column=1, padx=50, pady=10)



        Dec_frame = ttk.LabelFrame(self.frame, text="Declaration")
        Dec_frame.grid(row=2, column=0, sticky="news")
        terms_and_conditions = """
               **Terms and Conditions for Poll Pilot**

               **Last Updated: [01/10/2023]**

               These Terms and Conditions ("Terms") govern your use of the Poll Pilot App ("App") provided by [Front Bench techologies LLC ] ("Company," "we," "us," or "our"). By downloading, installing, accessing, or using the App, you agree to comply with and be bound by these Terms. If you do not agree with these Terms, please do not use the App.

               1. App Usage

               1.1. Eligibility: You must be at least 13 years old to use the App. If you are under the age of 13, please do not use the App.

               1.2. License: Subject to these Terms, we grant you a limited, non-exclusive, non-transferable, and revocable license to use the App.

               1.3. User Content: The App allows you to create and share content ("User Content"). You are solely responsible for your User Content, and you agree not to create, upload, or share any content that violates these Terms, any applicable laws, or infringes upon any third-party rights.

               2. Accuracy Disclaimer

               2.1. Inaccuracy Disclaimer: The App is provided for creative and entertainment purposes only. While we strive to provide accurate and up-to-date information, we do not guarantee the accuracy, completeness, or reliability of any content or creations made using the App. You acknowledge that any content or information obtained through the App is at your own risk, and we are not responsible for any inaccuracies, errors, or omissions.

               3. Data Privacy

               3.1. Data Collection: We do not collect, store, or process any personal data through the App. Your use of the App does not require the provision of personal information, and we do not track or store any data that can be used to identify you personally.

               3.2. Cookies: The App may use cookies or similar technologies for basic functionality, but these do not collect personal information.

               4. Limitation of Liability

               4.1. No Liability: To the extent permitted by law, we shall not be liable for any direct, indirect, incidental, special, or consequential damages arising out of or in connection with the use of the App. This includes, but is not limited to, any errors, inaccuracies, or omissions in the App or User Content.

               By using the App, you agree to these Terms and acknowledge that you have read, understood, and accepted them. If you do not agree with any part of these Terms, please refrain from using the App.
               """

        Dec_tnc = ttk.Label(Dec_frame, text="Terms and Condition Declaration")
        tnc_var = tk.StringVar(value="Uncheked")

        def Show_tnc():
            tkinter.messagebox.showinfo(message=terms_and_conditions)

        Dec_tnc_Button = ttk.Button(Dec_frame, text="Show T&C", command=Show_tnc)
        Dec_tnc_Button.grid(row=2, column=0, padx=50)
        Dec_tnc.grid(row=1, column=0)
        Dec_tnc_CB = ttk.Checkbutton(Dec_frame, text="I accept all the T&C", variable=tnc_var,
                                     onvalue="Checked", offvalue="Uncheked")
        Dec_tnc_CB.grid(row=1, column=1, padx=50, pady=10)

        button1 = ttk.Button(self.frame, text="SUBMIT", command=enter_data)
        button1.grid(row=3, column=0, sticky='news', padx=10
                   , pady=10)

        button1 = ttk.Button(self.frame, text="SUBMIT", command=enter_data)
        button1.grid(row=3, column=0, sticky='news', padx=10
                     , pady=10)
        Button_frame = ttk.LabelFrame(self.frame)
        Button_frame.grid(row=4, column=0, sticky="news")
        for i in range(3):
            Button_frame.grid_columnconfigure(i, weight=1)

        def Help():
            tkinter.messagebox.showinfo(title="Help", message="Take Data from Documentation")

        button_1 = ttk.Button(Button_frame, text="Help", command=Help)
        button_1.grid(row=0, column=0, sticky='news', padx=10
                     , pady=10)
        button_2 = ttk.Button(Button_frame, text="Go Home", command=app.show_frame_factory('opening'))
        button_2.grid(row=0, column=2, sticky='news', padx=10
                     , pady=10)