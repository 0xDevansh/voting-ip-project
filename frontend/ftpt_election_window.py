import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
#Renmae to Election window

class VotingWindow(ttk.Frame):
    def __init__(self, app):
        super().__init__(app)
        num_of_candidate = 5
        type = 'approval'
        election_title = 'The Dumb contest'
        candidate_list = ["modi" , "Borris" , "Trump" , "Erodoan", "Meloni"]
        candidate_party = ["BJP" , "Cons" , "Rep" , "TNP" , "Brothers of Italy" ]


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
                app.show_frame('start_election')


            for i in range(3):
                self.grid_rowconfigure(i, weight=1)
            self.grid_columnconfigure(0, weight=1)
            self.frame = tk.Frame(self)
            self.frame.grid()

            self.title_label =  tk.Label(self.frame , text= election_title )
            self.title_label.grid(row= 0 , column=0)
            User_info_frame = tk.LabelFrame(self.frame, text="User Informaton")
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
                l2.append(tk.Label(User_info_frame , text= candidate_party[i]))
                l2[i].grid(row= i+1 , column= 1)
                l4.append(tk.StringVar(value= 'No'))

                l3.append(tk.Checkbutton(User_info_frame, variable=l4[i],
                                    onvalue="Yes", offvalue="No"))
                l3[i].grid(row= i+1 , column= 2)

            Btn_1 = tk.Button(User_info_frame , text='submit', command= get_data)
            Btn_1.grid(row = num_of_candidate + 1 , column= 1)






