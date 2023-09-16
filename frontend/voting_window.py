import tkinter as tk
import tkinter.messagebox
import tkinter.ttk as ttk
from tkinter import messagebox

from backend.db.Database import Database


#Renmae to Election window

class VotingWindow(ttk.Frame):
    def __init__(self, app, context):
        super().__init__(app)
        poll = context['poll']
        db = Database.get_instance()
        candidates = db.get_poll_candidates(poll['id'])
        num_of_candidate = poll['num_candidates']
        type = poll['type']
        election_title = poll['name']
        self.candidate_names = []
        self.candidate_party = []
        for cand in candidates:
            self.candidate_names.append(cand['name'])
            self.candidate_party.append(cand['faction'])


        if type == 'approval':
            label_list_1 = []
            label_list_2= []
            checkbutton_list = []
            checkbutton_var = []
            checkbutton_var_value= []
            approval_list = []
            votes = []
            def get_data_approval():
                Check = 0
                for i in range(num_of_candidate):
                    checkbutton_var_value.append(checkbutton_var[i].get())

                for j in range(num_of_candidate):
                    if checkbutton_var_value[j] == 'Yes':
                        approval_list.append(self.candidate_names[j])
                        Check += 1

                    else:
                        pass
                if len(approval_list) == 0:
                    approval_list.append('NOTA')
                votes.append(approval_list.copy())
                checkbutton_var_value.clear()
                approval_list.clear()
                print(votes)
                # app.show_frame('voting_security_check')


            for i in range(3):
                self.grid_rowconfigure(i, weight=1)
            self.grid_columnconfigure(0, weight=1)
            self.frame = tk.Frame(self)
            self.frame.grid()

            self.title_label =  tk.Label(self.frame , text= election_title )
            self.title_label.grid(row= 0 , column=0)
            User_info_frame = tk.LabelFrame(self.frame)
            User_info_frame.grid(row=1, column=0, sticky="news")

            label1 = tk.Label(User_info_frame, text="Candidate Name")
            label1.grid(row=0, column=0, pady=10)
            label2 = tk.Label(User_info_frame, text="Candidate Party")
            label2.grid(row=0, column=1,padx =20,  pady=10)
            labecheckbutton_list = tk.Label(User_info_frame, text="Select here")
            labecheckbutton_list.grid(row=0, column=2, padx= 20 , pady=10)
            for i in range(num_of_candidate):
                label_list_1.append(tk.Label(User_info_frame , text= self.candidate_names[i]))
                label_list_1[i].grid(row = i+1 , column= 0)
                label_list_2.append(tk.Label(User_info_frame , text= self.candidate_party[i]))
                label_list_2[i].grid(row= i+1 , column= 1)
                checkbutton_var.append(tk.StringVar(value= 'No'))

                checkbutton_list.append(tk.Checkbutton(User_info_frame, variable=checkbutton_var[i],
                                    onvalue="Yes", offvalue="No"))
                checkbutton_list[i].grid(row= i+1 , column= 2)

            Btn_1 = tk.Button(User_info_frame , text='submit', command= get_data_approval)
            Btn_1.grid(row = num_of_candidate + 1 , column= 1)
        elif type == 'fptp':

            """
            if 'None of the Above' in self.candidate_names:
                pass
            else:
                self.candidate_names.append("None of the Above")
                self.candidate_party.append('NOTA')
                num_of_candidate+=1
            """
            label_list_1 = []
            label_list_2 = []
            votes = []
            def getvote_fptp():
                Vote = var_for_combobox.get()
                votes.append(Vote)
                app.show_frame('voting_security_check')
                print(votes)
            for i in range(3):
                self.grid_rowconfigure(i, weight=1)
            self.grid_columnconfigure(0, weight=1)
            self.frame = tk.Frame(self)
            self.frame.grid()

            self.title_label =  tk.Label(self.frame , text= election_title )
            self.title_label.grid(row= 0 , column=0)
            User_info_frame = tk.LabelFrame(self.frame)
            User_info_frame.grid(row=1, column=0, sticky="news")

            label1 = tk.Label(User_info_frame, text="Candidate Name")
            label1.grid(row=0, column=0, pady=10)
            label2 = tk.Label(User_info_frame, text="Candidate Party")
            label2.grid(row=0, column=2,padx =20,  pady=10)
            for i in range(num_of_candidate):
                label_list_1.append(tk.Label(User_info_frame , text= self.candidate_names[i]))
                label_list_1[i].grid(row = i+1 , column= 0 , pady= 10)
                label_list_2.append(tk.Label(User_info_frame , text= self.candidate_party[i]))
                label_list_2[i].grid(row= i+1 , column= 2 , pady = 10)
            var_for_combobox =  tk.StringVar()
            Votebox = ttk.Combobox(User_info_frame, textvariable= var_for_combobox)
            Votebox['values'] = self.candidate_names
            Votebox.grid(row= num_of_candidate + 1 , column = 1)
            Btn_1 = tk.Button(User_info_frame , text='submit' , command= getvote_fptp)
            Btn_1.grid(row = num_of_candidate + 2 , column= 1)
        elif type == 'runoff':
            counter = ['1']
            label_list_1 = []
            label_list_2 = []
            l3 = []
            l4 = []
            rank_votes = []
            votes = []

            def get_data_runoff():

                try:
                    rank_Vote = var_for_combobox.get()
                    self.candidate_names.remove(rank_Vote)
                    counter.append('')
                    votes.append(rank_Vote)
                except:
                    tkinter.messagebox.showerror(title="ERORR" , message="Please select a valid candidate from dropdown")


                Label20 = tk.Label(User_info_frame, text="Please enter your choice number:- " + str(len(counter)))
                Label20.grid(row=num_of_candidate + 1, column=1, pady=10, padx=10)
                Votebox = ttk.Combobox(User_info_frame, textvariable=var_for_combobox)
                Votebox['values'] = self.candidate_names
                Votebox.grid(row=num_of_candidate + 2, column=1, pady=10, padx=10)
                def get_vote_runoff():
                    try:
                        rank_Vote = var_for_combobox.get()
                        self.candidate_names.remove(rank_Vote)
                        counter.append('')
                        votes.append(rank_Vote)
                    except:
                       pass

                    rank_votes.append(votes)
                    app.show_frame('voting_security_check')
                    print(rank_votes)
                if len(counter) >= 3:
                    Btn_2 =tk.Button(User_info_frame, text= 'terminate', command= get_vote_runoff)
                    Btn_2.grid(row=num_of_candidate + 3, column=2, pady=10, padx=10)
                    if len(counter) == num_of_candidate:
                        Btn_1.grid_remove()


                print(rank_Vote ,votes)

            for i in range(3):
                self.grid_rowconfigure(i, weight=1)
            self.grid_columnconfigure(0, weight=1)
            self.frame = tk.Frame(self)
            self.frame.grid()

            self.title_label = tk.Label(self.frame, text=election_title)
            self.title_label.grid(row=0, column=0)
            User_info_frame = tk.LabelFrame(self.frame)
            User_info_frame.grid(row=1, column=0, sticky="news")

            label1 = tk.Label(User_info_frame, text="Candidate Name")
            label1.grid(row=0, column=0, pady=10, padx = 10)
            label2 = tk.Label(User_info_frame, text="Candidate Party")
            label2.grid(row=0, column=2, padx=10, pady=10)
            for i in range(num_of_candidate):
                label_list_1.append(tk.Label(User_info_frame, text=self.candidate_names[i]))
                label_list_1[i].grid(row=i + 1, column=0, pady=10,padx=10)
                label_list_2.append(tk.Label(User_info_frame, text=self.candidate_party[i]))
                label_list_2[i].grid(row=i + 1, column=2, pady=10, padx=10)
            var_for_combobox = tk.StringVar()
            Label20 = tk.Label(User_info_frame, text = "Please enter your choice number:- " + str(len(counter)))
            Label20.grid(row=num_of_candidate + 1, column=1 ,pady=10, padx=10)
            Votebox = ttk.Combobox(User_info_frame, textvariable=var_for_combobox)
            Votebox['values'] = self.candidate_names
            Votebox.grid(row=num_of_candidate + 2, column=1, pady=10, padx=10)
            Btn_1 = tk.Button(User_info_frame, text='submit', command=get_data_runoff)
            Btn_1.grid(row=num_of_candidate + 3, column=0, pady=10, padx=10)
        elif type == 'referendum':
            label_list_1 = []
            label_list_2= []
            combobox_list = []
            votes = []
            def get_vote_referendum():
                Check = 0
                for i in range(num_of_candidate):
                    Choice = combobox_list[i].get()
                    if Choice in ['Approve' , 'Dissaprove' , 'Abstain']:
                        votes.append(Choice)
                        if i == num_of_candidate - 1:
                             print(votes)
                             app.show_frame('voting_security_check')
                    else:
                        tk.messagebox.showerror(title='Error', message="Please select a valid choice in referendum :-" + str(i+1))
                        votes.clear()
                        break



            for i in range(3):
                self.grid_rowconfigure(i, weight=1)
            self.grid_columnconfigure(0, weight=1)
            self.frame = tk.Frame(self)
            self.frame.grid()

            self.title_label =  tk.Label(self.frame , text= election_title )
            self.title_label.grid(row= 0 , column=0)
            User_info_frame = tk.LabelFrame(self.frame)
            User_info_frame.grid(row=1, column=0, sticky="news")

            label1 = tk.Label(User_info_frame, text="Referendum Name")
            label1.grid(row=0, column=0, pady=10)
            label2 = tk.Label(User_info_frame, text="Referendum Description")
            label2.grid(row=0, column=1,padx =20,  pady=10)
            labelcombobox_list = tk.Label(User_info_frame, text="Select here")
            labelcombobox_list.grid(row=0, column=2, padx= 20 , pady=10)
            for i in range(num_of_candidate):
                label_list_1.append(tk.Label(User_info_frame , text= self.candidate_names[i]))
                label_list_1[i].grid(row = i+1 , column= 0)
                label_list_2.append(tk.Button(User_info_frame, text= 'Show description', command=self.show_ref_description(i)))
                label_list_2[i].grid(row= i+1 , column= 1)
                combobox_list.append(ttk.Combobox(User_info_frame, values= ['Approve' , 'Dissaprove' , 'Abstain']))
                combobox_list[i].grid(row= i+1 , column= 2)
            Btn_1 = tk.Button(User_info_frame , text='submit' , command=get_vote_referendum)
            Btn_1.grid(row = num_of_candidate + 1 , column= 1)

    def show_ref_description(self, i):
        return lambda: tk.messagebox.showinfo(title = self.candidate_names[i] , message=self.candidate_party[i])







