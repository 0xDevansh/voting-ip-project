import tkinter as tk
import tkinter.messagebox
import tkinter.ttk as ttk
from tkinter import messagebox
#Renmae to Election window

class VotingWindow(ttk.Frame):
    def __init__(self, app, context):
        super().__init__(app)
        num_of_candidate = 5
        type = 'referendum'
        election_title = 'The Dumb contest'
        candidate_list = ["modi" , "Borris" , "Trump" , "Erodoan", "Meloni"]
        self.candidate_party = ["BJP" , "Cons" , "Rep" , "TNP" , "Brothers of Italy" ]


        if type == 'approval':
            l1 = []
            l2= []
            l3 = []
            l4 = []
            l5= []
            l6 = []
            votes = []
            def get_data():
                Check = 0
                for i in range(num_of_candidate):
                    l5.append(l4[i].get())

                for j in range(num_of_candidate):
                    if l5[j] == 'Yes':
                        l6.append(candidate_list[j])
                        Check += 1

                    else:
                        pass
                if len(l6) == 0:
                    l6.append('NOTA')
                votes.append(l6.copy())
                voter_number = len(votes)
                print("Vote - ", voter_number, " :- " , l6 )
                l5.clear()
                l6.clear()
                print(votes)
                app.show_frame('voting_security_check')


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
            label3 = tk.Label(User_info_frame, text="Select here")
            label3.grid(row=0, column=2, padx= 20 , pady=10)
            for i in range(num_of_candidate):
                l1.append(tk.Label(User_info_frame , text= candidate_list[i]))
                l1[i].grid(row = i+1 , column= 0)
                l2.append(tk.Label(User_info_frame , text= self.candidate_party[i]))
                l2[i].grid(row= i+1 , column= 1)
                l4.append(tk.StringVar(value= 'No'))

                l3.append(tk.Checkbutton(User_info_frame, variable=l4[i],
                                    onvalue="Yes", offvalue="No"))
                l3[i].grid(row= i+1 , column= 2)

            Btn_1 = tk.Button(User_info_frame , text='submit', command= get_data)
            Btn_1.grid(row = num_of_candidate + 1 , column= 1)
        elif type == 'ftpt':
            if 'None of the Above' in candidate_list:
                pass
            else:
                candidate_list.append("None of the Above")
                self.candidate_party.append('NOTA')
                num_of_candidate+=1
            l1 = []
            l2 = []
            l3 = []
            l4 = []
            votes = []
            def getvote():
                Vote = n.get()
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
                l1.append(tk.Label(User_info_frame , text= candidate_list[i]))
                l1[i].grid(row = i+1 , column= 0 , pady= 10)
                l2.append(tk.Label(User_info_frame , text= self.candidate_party[i]))
                l2[i].grid(row= i+1 , column= 2 , pady = 10)
            n =  tk.StringVar()
            Votebox = ttk.Combobox(User_info_frame, textvariable= n)
            Votebox['values'] = candidate_list
            Votebox.grid(row= num_of_candidate + 1 , column = 1)
            Btn_1 = tk.Button(User_info_frame , text='submit' , command= getvote)
            Btn_1.grid(row = num_of_candidate + 2 , column= 1)
        elif type == 'runoff':
            counter = ['1']
            l1 = []
            l2 = []
            l3 = []
            l4 = []
            votes = []
            total_vote = []

            def get_vote():

                try:
                    rank_Vote = n.get()
                    candidate_list.remove(rank_Vote)
                    counter.append('')
                    total_vote.append(rank_Vote)
                except:
                    tkinter.messagebox.showerror(title="ERORR" , message="Please select a valid candidate from dropdown")


                Label20 = tk.Label(User_info_frame, text="Please enter your choice number:- " + str(len(counter)))
                Label20.grid(row=num_of_candidate + 1, column=1, pady=10, padx=10)
                Votebox = ttk.Combobox(User_info_frame, textvariable=n)
                Votebox['values'] = candidate_list
                Votebox.grid(row=num_of_candidate + 2, column=1, pady=10, padx=10)
                def terminate():
                    try:
                        rank_Vote = n.get()
                        candidate_list.remove(rank_Vote)
                        counter.append('')
                        total_vote.append(rank_Vote)
                    except:
                       pass

                    votes.append(total_vote)
                    app.show_frame('voting_security_check')
                    print(votes)
                if len(counter) >= 3:
                    Btn_2 =tk.Button(User_info_frame, text= 'terminate', command= terminate)
                    Btn_2.grid(row=num_of_candidate + 3, column=2, pady=10, padx=10)
                    if len(counter) == num_of_candidate:
                        Btn_1.grid_remove()


                print(rank_Vote ,total_vote)

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
                l1.append(tk.Label(User_info_frame, text=candidate_list[i]))
                l1[i].grid(row=i + 1, column=0, pady=10,padx=10)
                l2.append(tk.Label(User_info_frame, text=self.candidate_party[i]))
                l2[i].grid(row=i + 1, column=2, pady=10, padx=10)
            n = tk.StringVar()
            Label20 = tk.Label(User_info_frame, text = "Please enter your choice number:- " + str(len(counter)))
            Label20.grid(row=num_of_candidate + 1, column=1 ,pady=10, padx=10)
            Votebox = ttk.Combobox(User_info_frame, textvariable=n)
            Votebox['values'] = candidate_list
            Votebox.grid(row=num_of_candidate + 2, column=1, pady=10, padx=10)
            Btn_1 = tk.Button(User_info_frame, text='submit', command=get_vote)
            Btn_1.grid(row=num_of_candidate + 3, column=0, pady=10, padx=10)
        elif type == 'referendum':
            l1 = []
            l2= []
            l3 = []
            votes = []
            def get_data():
                Check = 0
                for i in range(num_of_candidate):
                    Choice = l3[i].get()
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

            label1 = tk.Label(User_info_frame, text="Refrendum Name")
            label1.grid(row=0, column=0, pady=10)
            label2 = tk.Label(User_info_frame, text="Refrendum Description")
            label2.grid(row=0, column=1,padx =20,  pady=10)
            label3 = tk.Label(User_info_frame, text="Select here")
            label3.grid(row=0, column=2, padx= 20 , pady=10)
            for i in range(num_of_candidate):
                l1.append(tk.Label(User_info_frame , text= candidate_list[i]))
                l1[i].grid(row = i+1 , column= 0)
                l2.append(tk.Button(User_info_frame, text= 'Show description', command=self.show_ref_description(i)))
                l2[i].grid(row= i+1 , column= 1)
                l3.append(ttk.Combobox(User_info_frame, values= ['Approve' , 'Dissaprove' , 'Abstain']))
                l3[i].grid(row= i+1 , column= 2)
            Btn_1 = tk.Button(User_info_frame , text='submit' , command=get_data)
            Btn_1.grid(row = num_of_candidate + 1 , column= 1)

    def show_ref_description(self, i):
        return lambda: tk.messagebox.showerror(message=self.candidate_party[i])







