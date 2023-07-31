
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Data entry Form")

frame = tk.Frame(root)
frame.pack()

User_info_frame = tk.LabelFrame(frame, text = "User Informaton")
User_info_frame.grid(row=0 , column=0 , sticky="news")

Name_Inst = tk.Label(User_info_frame , text = "Name of the institution")
Name_Inst.grid(row =0 , column =0)
Name_Inst_Entry = tk.Entry(User_info_frame)
Name_Inst_Entry.grid(row=0 , column=1 , padx= 50 , pady= 15)

type_Inst = tk.Label(User_info_frame , text = "Type of the institution")
type_Inst.grid(row =1 , column =0)
type_Inst_Entry = tk.Entry(User_info_frame)
type_Inst_Entry.grid(row=1 , column=1 , padx= 50 , pady= 15)

purpose_of_election = tk.Label(User_info_frame , text = "Purpose of election")
purpose_of_election.grid(row =2 , column =0)
purpose_of_election_Entry = tk.Entry(User_info_frame)
purpose_of_election_Entry.grid(row=2 , column=1 , padx= 50 , pady= 15)

Election_info_frame = tk.LabelFrame(frame, text = "Election Information")
Election_info_frame.grid(row=1 , column=0 , sticky= "news")

Title_elc = tk.Label(Election_info_frame , text = "Title of Election")
Title_elc.grid(row =0 , column =0)
Title_elc_Entry = tk.Entry(Election_info_frame)
Title_elc_Entry.grid(row=0 , column=1 , padx= 50 , pady= 15)

Description = tk.Label(Election_info_frame , text = "Desccription of Election")
Description.grid(row =1 , column =0)
Description_Entry = tk.Entry(Election_info_frame)
Description_Entry.grid(row=1 , column=1 , padx= 50 , pady= 15)

No_Cand = tk.Label(Election_info_frame , text = "Number of Candidates")
No_Cand.grid(row =2 , column =0)
No_Cand_Entry = tk.Entry(Election_info_frame)
No_Cand_Entry.grid(row=2 , column=1 , padx= 50 , pady= 15)

Date = tk.Label(Election_info_frame , text = "Date")
Date.grid(row =3 , column =0)
Date_Entry = tk.Entry(Election_info_frame)
Date_Entry.grid(row=3 , column=1 , padx= 50 , pady= 15)

No_Voter = tk.Label(Election_info_frame , text = "Number of  Voters")
No_Voter.grid(row =4 , column =0)
No_Voter_Entry = tk.Entry(Election_info_frame)
No_Voter_Entry.grid(row=4 , column=1 , padx= 50 , pady= 15)

Sec_Key = tk.Label(Election_info_frame , text = "Security Key")
Sec_Key.grid(row =5 , column =0)
Sec_Key_Entry = tk.Entry(Election_info_frame)
Sec_Key_Entry.grid(row=5 , column=1 , padx= 50 , pady= 15)

Dec_frame = tk.LabelFrame(frame, text = "Declaration")
Dec_frame.grid(row=2 , column=0 , sticky= "news")

Dec_info = tk.Label(Dec_frame , text = "Information Declaration")
Dec_info.grid(row =0 , column =0)
Dec_info_CB = tk.Checkbutton(Dec_frame , text = "I verify all the information provided above is True")
Dec_info_CB.grid(row=0 , column=1 , padx= 50 , pady= 15)

Dec_TaC = tk.Label(Dec_frame , text = "Terms and Condition Declaration")
Dec_TaC.grid(row =1 , column =0)
Dec_TaC_CB = tk.Checkbutton(Dec_frame , text = "I accept all the T&C")
Dec_TaC_CB.grid(row=1 , column=1 , padx= 50 , pady= 15)


root.mainloop()