
import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
from tkinter import  messagebox
def enter_data():
    name_inst = Name_Inst_Entry.get()
    type_inst_ = type_Inst_Entry.get()
    purpose = purpose_of_election_Entry.get()
    title_elc = Title_elc_Entry.get()
    description = Description_Entry.get()
    Num_candi = No_Cand_Entry.get()
    Date_elec = Date_Entry.get()
    Num_voter = No_Voter_Entry.get()
    Security_Key = Sec_Key_Entry.get()
    Tac = Tac_var.get()
    Alpha = 0
    l = [0,0,0,0,0,0,0,0,0,0]
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


    if Alpha == 5:
        if Voting_Page.state() == 'withdrawn':
            Voting_Page.deiconify()
            window.withdraw()
        else:
            Voting_Page.withdraw()
            window.deiconify()
    elif l[0] == 1:
        tkinter.messagebox.showerror(title= "Erroe101" , message = 'Number of Candidataes must be integer')
    elif l[1] == 1:
        tkinter.messagebox.showerror(title="Error102", message='Number of Voters Must be integer')
    elif l[2] == 1:
        tkinter.messagebox.showerror(title="Error103", message='Password must be atleast 8 digit long')
    elif l[3] == 1:
        tkinter.messagebox.showerror(title="Error104", message='Title , Description and Date of Election Required')
    elif l[4] == 1:
        tkinter.messagebox.showerror(title="Error105", message="You have not accepted the Terms and Condition")

    print(type(Num_candi))
    print(name_inst,type_inst_,purpose,title_elc,description,Num_voter, Num_candi, Date_elec, Security_Key, Tac)
    print(Alpha)

def create_data_entry_frame():
    root = tk.Tk()
    window = tk.Toplevel(root)
    root.title("Data entry Form")

    frame = tk.Frame(window)
    frame.pack()

    User_info_frame = tk.LabelFrame(frame, text = "User Informaton")
    User_info_frame.grid(row=0 , column=0 , sticky="news")

    Name_Inst = tk.Label(User_info_frame , text = "Name of the institution")
    Name_Inst.grid(row =0 , column =0)
    Name_Inst_Entry = tk.Entry(User_info_frame)
    Name_Inst_Entry.grid(row=0 , column=1 , padx= 50 , pady= 10)

    type_Inst = tk.Label(User_info_frame , text = "Type of the institution")
    type_Inst.grid(row =1 , column =0)
    type_Inst_Entry = tk.Entry(User_info_frame)
    type_Inst_Entry.grid(row=1 , column=1 , padx= 50 , pady= 10)

    purpose_of_election = tk.Label(User_info_frame , text = "Purpose of election")
    purpose_of_election.grid(row =2 , column =0)
    purpose_of_election_Entry = tk.Entry(User_info_frame)
    purpose_of_election_Entry.grid(row=2 , column=1 , padx= 50 , pady= 10)

    Election_info_frame = tk.LabelFrame(frame, text = "Election Information")
    Election_info_frame.grid(row=1 , column=0 , sticky= "news")

    Title_elc = tk.Label(Election_info_frame , text = "Title of Election")
    Title_elc.grid(row =0 , column =0)
    Title_elc_Entry = tk.Entry(Election_info_frame)
    Title_elc_Entry.grid(row=0 , column=1 , padx= 50 , pady= 10)

    Description = tk.Label(Election_info_frame , text = "Desccription of Election")
    Description.grid(row =1 , column =0)
    Description_Entry = tk.Entry(Election_info_frame)
    Description_Entry.grid(row=1 , column=1 , padx= 50 , pady= 10)

    No_Cand = tk.Label(Election_info_frame , text = "Number of Candidates")
    No_Cand.grid(row =2 , column =0)
    No_Cand_Entry = tk.Entry(Election_info_frame)
    No_Cand_Entry.grid(row=2 , column=1 , padx= 50 , pady= 10)

    Date = tk.Label(Election_info_frame , text = "Date")
    Date.grid(row =3 , column =0)
    Date_Entry = tk.Entry(Election_info_frame)
    Date_Entry.grid(row=3 , column=1 , padx= 50 , pady= 10)

    No_Voter = tk.Label(Election_info_frame , text = "Number of  Voters")
    No_Voter.grid(row =4 , column =0)
    No_Voter_Entry = tk.Entry(Election_info_frame)
    No_Voter_Entry.grid(row=4 , column=1 , padx= 50 , pady= 10)

    Sec_Key = tk.Label(Election_info_frame , text = "Security Key")
    Sec_Key.grid(row =5 , column =0)
    Sec_Key_Entry = tk.Entry(Election_info_frame)
    Sec_Key_Entry.grid(row=5 , column=1 , padx= 50 , pady= 10)

    Dec_frame = tk.LabelFrame(frame, text = "Declaration")
    Dec_frame.grid(row=2 , column=0 , sticky= "news")

    Dec_TaC = tk.Label(Dec_frame , text = "Terms and Condition Declaration")
    Tac_var = tk.StringVar(value="Uncheked")
    Dec_TaC.grid(row =1 , column =0)
    Dec_TaC_CB = tk.Checkbutton(Dec_frame , text = "I accept all the T&C", variable= Tac_var ,
                                onvalue= "Checked" , offvalue="Uncheked")
    Dec_TaC_CB.grid(row=1 , column=1 , padx= 50 , pady= 10)

    button1= tk.Button(frame, text="SUBMIT" , command= enter_data)
    button1.grid(row=3 , column=0 , sticky='news', padx=10
                 ,pady= 10)
    Voting_Page = tk.Toplevel(root)
    Voting_Page.title('voting page')
    Voting_Page.withdraw()

    root.withdraw()
    return root

if __name__ == '__main__':
    window = create_data_entry_frame()
    window.mainloop()