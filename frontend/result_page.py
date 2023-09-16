import tkinter as tk
import tkinter.ttk as ttk
import traceback
from tkinter import messagebox

from backend.db.Database import Database

class ResultFrame(ttk.Frame):
    def __init__(self, app, context):
        super().__init__(app)
        poll = context['poll']
        result = None
        candidates = None
        actual_num_votes = 0
        if 'result' in context:
            result = context['result']
        try:
            db = Database.get_instance()
            if not result:
                result = db.get_result(poll['id'])
            candidates = db.get_poll_candidates(poll['id'])
            actual_num_votes = db.get_num_votes(poll['id'])
            if poll['type'] == 'referendum':
                candidates = db.get_poll_proposals(poll['id'])
        except Exception as exc:
            traceback.print_exc()
            tk.messagebox.showerror(message=str(exc))
        candidate_names = list(map(lambda c: c['name'], candidates))
        num_voters = poll['num_voters']
        name_of_institution = poll['inst_name']
        title = poll['name']
        description = poll['description']
        type = poll['type']
        max_approved =  poll['max_approved']
        min_threshold = poll['min_threshold']
        voter_turnout = round((actual_num_votes/(num_voters))*100,1)
        def Generate():
            print('HERE')
            try:
                db = Database.get_instance()
                poll_result = context['result'] if 'result' in context else None
                if not poll_result:
                    poll_result = db.get_result(poll['id'])
                    if not result:
                        raise Exception('Result not found')
                    if type  == 'approval':
                        Winners = poll_result['winners']
                        Order = poll_result['order']
                        btn1.grid_remove()

                        for i in range(3):
                            self.grid_rowconfigure(i, weight=1)
                        self.grid_columnconfigure(0, weight=1)
                        self.frame = tk.Frame(self)
                        self.frame.grid()

                        self.title_label = tk.Label(self.frame, text= "THE RESULT ARE")
                        self.title_label.grid(row=0, column=0)

                        User_info_frame = tk.LabelFrame(self.frame)
                        User_info_frame.grid(row=1, column=0, sticky="news")

                        label1 = tk.Label(       User_info_frame, text = "By : " + name_of_institution)
                        label1.grid(row=1,column=2 ,pady= 10 , padx=0)
                        #
                        label2 = tk.Label(       User_info_frame, text= title)
                        label2.grid(row=0, column=1, pady=10, padx=0)
                        #
                        label4 = tk.Label(       User_info_frame, text="Type : "  +  type)
                        label4.grid(row=2, column=0, pady=10, padx=0)
                        #
                        label5 = tk.Label(       User_info_frame, text="Voter_turnout :" + str(voter_turnout))
                        label5.grid(row=2, column=2, pady=10, padx=0)
                        #
                        label6 = tk.Label(       User_info_frame, text="max approved : " + str(max_approved))
                        label6.grid(row=3, column=0, pady=10, padx=0)
                        #
                        label7 = tk.Label(       User_info_frame, text='min_threshold :' + str(min_threshold))
                        label7.grid(row=3, column=2, pady=10, padx=0)
                        #
                        label8 = tk.Label(       User_info_frame, text="max approved : " + str(max_approved))
                        label8.grid(row=3, column=0, pady=10, padx=0)
                        #
                        label9 = tk.Label(       User_info_frame, text="Winners")
                        label9.grid(row=4, column=1, pady=10, padx=0)
                        #
                        label10 = tk.Label(       User_info_frame, text=str(Winners))
                        label10.grid(row=5, column=1, pady=10, padx=0)
                        #
                        label11 = tk.Label(       User_info_frame, text= "Final Tally :")
                        label11.grid(row=6, column=0, pady=10, padx=0)
                        l1 = []
                        for i in range(len(candidate_names)):
                            l1.append('')
                            l1[i] = tk.Label(       User_info_frame, text= str(Order[i]) )
                            l1[i].grid(row=7+i, column=1, pady=10, padx=0)
                        print(poll_result)

                    elif type  == 'fptp':
                        Winners = poll_result['winners']
                        Order = poll_result['order']
                        btn1.grid_remove()

                        for i in range(3):
                            self.grid_rowconfigure(i, weight=1)
                        self.grid_columnconfigure(0, weight=1)
                        self.frame = tk.Frame(self)
                        self.frame.grid()

                        self.title_label = tk.Label(self.frame, text= "THE RESULT ARE")
                        self.title_label.grid(row=0, column=0)

                        User_info_frame = tk.LabelFrame(self.frame)
                        User_info_frame.grid(row=1, column=0, sticky="news")

                        label1 = tk.Label(       User_info_frame, text = "By : " + name_of_institution)
                        label1.grid(row=1,column=1 ,pady= 10 , padx=0)
                        #
                        label2 = tk.Label(       User_info_frame, text= title)
                        label2.grid(row=0, column=1, pady=10, padx=0)
                        #
                        label4 = tk.Label(       User_info_frame, text="Type : "  +  type)
                        label4.grid(row=2, column=0, pady=10, padx=0)
                        #
                        label5 = tk.Label(       User_info_frame, text="Voter_turnout :" + str(voter_turnout))
                        label5.grid(row=2, column=2, pady=10, padx=0)
                        #
                        label9 = tk.Label(       User_info_frame, text="Winners")
                        label9.grid(row=3, column=1, pady=10, padx=0)
                        #
                        label10 = tk.Label(       User_info_frame, text=str(Winners))
                        label10.grid(row=4, column=1, pady=10, padx=0)
                        #
                        label11 = tk.Label(       User_info_frame, text= "Final Tally :")
                        label11.grid(row=5, column=0, pady=10, padx=0)
                        l1 = []
                    for i in range(len(candidate_names)):
                        l1.append('')
                        l1[i] = tk.Label(       User_info_frame, text= str(Order[i]) )
                        l1[i].grid(row=6+i, column=1, pady=10, padx=0)






                    print(poll_result)
            except Exception as exc:
                traceback.print_exc()
                tk.messagebox.showerror(message=str(exc))

        for i in range(1):
            self.grid_rowconfigure(i, weight=1)
        self.grid_columnconfigure(0, weight=1)

        btn1 =tk.Button(self, text="Generate Result" , command = Generate)
        btn1.grid(row = 0 , column= 0)
