import tkinter as tk
import tkinter.ttk as ttk
import traceback
from tkinter import messagebox

from backend.db.Database import Database

class ResultFrame(ttk.Frame):
    def __init__(self, app, context):
        super().__init__(app)
        poll = context['poll']
        candidates = None
        actual_num_votes = 0
        try:
            poll_result = context['result'] if 'result' in context else None
            db = Database.get_instance()
            candidates = db.get_poll_candidates(poll['id'])
            actual_num_votes = db.get_num_votes(poll['id'])
            if poll['type'] == 'referendum':
                candidates = db.get_poll_proposals(poll['id'])

            candidate_names = list(map(lambda c: c['name'], candidates))
            num_voters = poll['num_voters']
            name_of_institution = poll['inst_name']
            title = poll['name']
            description = poll['description']
            type = poll['type']
            max_approved =  poll['max_approved']
            min_threshold = poll['min_threshold']
            voter_turnout = round((actual_num_votes/(num_voters))*100,1)

            if not poll_result:
                poll_result = db.get_result(poll['id'])
                if not poll_result:
                    raise Exception('Result not found')
                # Switch candidate ids with names
                candidate_id_name = {}
                for cand in candidates:
                    candidate_id_name[cand['candidate_id']] = cand['name']
                print(poll_result)
                if 'winners' in poll_result and poll_result['winners'] != None:
                    poll_result['winners'] = list(map(lambda w:candidate_id_name[w], poll_result['winners']))
                if 'eliminated' in poll_result and poll_result['eliminated'] != None:
                    poll_result['eliminated'] = list(map(lambda w:candidate_id_name[w], poll_result['eliminated']))
                if 'order' in poll_result and poll_result['order'] != None:
                    poll_result['order'] = list(map(lambda o:[candidate_id_name[o[0]], o[1]], poll_result['order']))



                if type  == 'approval':
                    Winners = poll_result['winners']
                    Order = poll_result['order']

                    for i in range(3):
                        self.grid_rowconfigure(i, weight=1)
                    self.grid_columnconfigure(0, weight=1)
                    self.frame = tk.Frame(self)
                    self.frame.grid()

                    self.title_label = tk.Label(self.frame, text= "THE RESULT ARE")
                    self.title_label.grid(row=0, column=0)

                    User_info_frame = tk.LabelFrame(self.frame)
                    User_info_frame.grid(row=1, column=0, sticky="news")

                    label1 = tk.Label(       User_info_frame, text = "By : " + name_of_institution , font=12)
                    label1.grid(row=1,column=1 ,pady= 10 , padx=0)
                    #
                    label2 = tk.Label(       User_info_frame, text= title , font= 12)
                    label2.grid(row=0, column=1, pady=10, padx=0)
                    #
                    label3 = tk.Label(User_info_frame, text=description)
                    label3.grid(row=2, column=1, pady=10, padx=0)
                    #
                    label4 = tk.Label(       User_info_frame, text="Type : "  +  type)
                    label4.grid(row=3, column=0, pady=10, padx=0)
                    #
                    label5 = tk.Label(       User_info_frame, text="Voter_turnout :" + str(voter_turnout) + '%')
                    label5.grid(row=3, column=2, pady=10, padx=0)
                    #
                    label6 = tk.Label(       User_info_frame, text="max approved : " + str(max_approved))
                    label6.grid(row=4, column=0, pady=10, padx=0)
                    #
                    label7 = tk.Label(       User_info_frame, text='min_threshold :' + str(min_threshold))
                    label7.grid(row=4, column=2, pady=10, padx=0)
                    '''
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
                    '''
                    Winner_info_frame = tk.LabelFrame(self.frame, text = 'The Winner is')
                    Winner_info_frame.grid(row=2, column=0, sticky="news")
                    Label_for_winner = []
                    for i in range(len(Winners)):
                        Label_for_winner.append(tk.Label(Winner_info_frame,text= 'Winner :- ' + Winners[i] ,font= 12))
                        Label_for_winner[i].grid(row =i , column = 0 ,sticky= 'news')
                        Winner_info_frame.grid_columnconfigure(i, weight=1)
                    Election_result_frame = tk.LabelFrame(self.frame, text = 'Total Result')
                    Election_result_frame.grid(row=3, column=0, sticky="news")
                    text_for_header=["S. No" , "Candidate" , "faction" , " Votes"]
                    Label_for_header=[]
                    for i in range(len((text_for_header))):
                        Label_for_header.append(tk.Label(Election_result_frame,text= text_for_header[i]))
                        Label_for_header[i].grid(row =0 , column= i)
                    Sno_label=[]
                    Candidate_label=[]
                    faction_label=[]
                    Votes_Label=[]
                    for i in range(len(Order)):
                        Sno_label.append(tk.Label(Election_result_frame, text= i))
                        Sno_label[i].grid(row=i+1, column=0)
                        Candidate_label.append(tk.Label(Election_result_frame, text=Order[i][0]))
                        Candidate_label[i].grid(row=i + 1, column=1)
                        '''
                        for j in range(len(candidates)):
                            if candidates[j]['candidate_id'] == Order[j][0]:
                               print(candidates[j]['candidate_id'])
                               print(Order[j][0])
                            else:
                                pass
                        '''

                        try:
                            faction = candidates[i]['faction']
                            faction_label.append(tk.Label(Election_result_frame, text=faction))
                            faction_label[i].grid(row=i + 1, column=2)
                        except:
                            faction_label.append(tk.Label(Election_result_frame, text="NA"))
                            faction_label[i].grid(row=i + 1, column=2)


                        Votes_Label.append(tk.Label(Election_result_frame, text=Order[i][1]))
                        Votes_Label[i].grid(row=i + 1, column=3)

                    for i in range(len(Order) + 1):
                        Election_result_frame.grid_columnconfigure(i, weight=1)
                        Election_result_frame.grid_rowconfigure(i, weight=1)





                elif type  == 'fptp':
                    Winners = poll_result['winners']
                    Order = poll_result['order']

                    for i in range(3):
                        self.grid_rowconfigure(i, weight=1)
                    self.grid_columnconfigure(0, weight=1)
                    self.frame = tk.Frame(self)
                    self.frame.grid()

                    self.title_label = tk.Label(self.frame, text= "THE RESULT ARE")
                    self.title_label.grid(row=0, column=0)
                    User_info_frame = tk.LabelFrame(self.frame)
                    User_info_frame.grid(row=1, column=0, sticky="news")

                    label1 = tk.Label(User_info_frame, text="By : " + name_of_institution, font=12)
                    label1.grid(row=1, column=1, pady=10, padx=0)
                    #
                    label2 = tk.Label(User_info_frame, text=title, font=12)
                    label2.grid(row=0, column=1, pady=10, padx=0)
                    #
                    label3 = tk.Label(User_info_frame, text=title)
                    label3.grid(row=2, column=1, pady=10, padx=0)
                    #
                    label4 = tk.Label(User_info_frame, text="Type : " + type)
                    label4.grid(row=3, column=0, pady=10, padx=0)
                    #
                    label5 = tk.Label(User_info_frame, text="Voter_turnout :" + str(voter_turnout))
                    label5.grid(row=3, column=2, pady=10, padx=0)
                    Winner_info_frame = tk.LabelFrame(self.frame, text='The Winner is')
                    Winner_info_frame.grid(row=2, column=0, sticky="news")
                    Label_for_winner = []
                    for i in range(len(Winners)):
                        Label_for_winner.append(
                            tk.Label(Winner_info_frame, text='Winner :- ' + Winners[i], font=12))
                        Label_for_winner[i].grid(row=i, column=0, sticky='news')
                        Winner_info_frame.grid_columnconfigure(i, weight=1)
                    Election_result_frame = tk.LabelFrame(self.frame, text='Total Result')
                    Election_result_frame.grid(row=3, column=0, sticky="news")
                    text_for_header = ["S. No", "Candidate", "faction", " Votes"]
                    Label_for_header = []
                    for i in range(len((text_for_header))):
                        Label_for_header.append(tk.Label(Election_result_frame, text=text_for_header[i]))
                        Label_for_header[i].grid(row=0, column=i)
                    Sno_label = []
                    Candidate_label = []
                    faction_label = []
                    Votes_Label = []
                    for i in range(len(Order)):
                        Sno_label.append(tk.Label(Election_result_frame, text=i))
                        Sno_label[i].grid(row=i + 1, column=0)
                        Candidate_label.append(tk.Label(Election_result_frame, text=Order[i][0]))
                        Candidate_label[i].grid(row=i + 1, column=1)
                        '''
                        for j in range(len(candidates)):
                            if candidates[j]['candidate_id'] == Order[j][0]:
                               print(candidates[j]['candidate_id'])
                               print(Order[j][0])
                            else:
                                pass
                        '''

                        try:
                            faction = candidates[i]['faction']
                            faction_label.append(tk.Label(Election_result_frame, text=faction))
                            faction_label[i].grid(row=i + 1, column=2)
                        except:
                            faction_label.append(tk.Label(Election_result_frame, text="NA"))
                            faction_label[i].grid(row=i + 1, column=2)

                        Votes_Label.append(tk.Label(Election_result_frame, text=Order[i][1]))
                        Votes_Label[i].grid(row=i + 1, column=3)

                    for i in range(len(Order) + 1):
                        Election_result_frame.grid_columnconfigure(i, weight=1)
                        Election_result_frame.grid_rowconfigure(i, weight=1)
                elif type  == 'runoff':
                    Winners = poll_result['winners']
                    Order = poll_result['order']
                    Eliminated = poll_result['eliminated']

                    for i in range(3):
                        self.grid_rowconfigure(i, weight=1)
                    self.grid_columnconfigure(0, weight=1)
                    self.frame = tk.Frame(self)
                    self.frame.grid()

                    self.title_label = tk.Label(self.frame, text="THE RESULT ARE")
                    self.title_label.grid(row=0, column=0)

                    User_info_frame = tk.LabelFrame(self.frame)
                    User_info_frame.grid(row=1, column=0, sticky="news")

                    label1 = tk.Label(User_info_frame, text="By : " + name_of_institution, font=12)
                    label1.grid(row=1, column=1, pady=10, padx=0)
                    #
                    label2 = tk.Label(User_info_frame, text=title, font=12)
                    label2.grid(row=0, column=1, pady=10, padx=0)
                    #
                    label3 = tk.Label(User_info_frame, text=title)
                    label3.grid(row=2, column=1, pady=10, padx=0)
                    #
                    label4 = tk.Label(User_info_frame, text="Type : " + type)
                    label4.grid(row=3, column=0, pady=10, padx=0)
                    #
                    label5 = tk.Label(User_info_frame, text="Voter_turnout :" + str(voter_turnout))
                    label5.grid(row=3, column=2, pady=10, padx=0)

                    Winner_info_frame = tk.LabelFrame(self.frame, text='The Winner is')
                    Winner_info_frame.grid(row=2, column=0, sticky="news")
                    Label_for_winner = []
                    for i in range(1):
                        Label_for_winner.append(
                            tk.Label(Winner_info_frame, text='Winner :- ' + Winners[0], font=12))
                        Label_for_winner[i].grid(row=i, column=0, sticky='news')
                        Winner_info_frame.grid_columnconfigure(i, weight=1)

                    Election_result_frame = tk.LabelFrame(self.frame, text='First Preference Vote')
                    Election_result_frame.grid(row=3, column=0, sticky="news")
                    text_for_header = ["S. No", "Candidate", "faction", " Votes"]
                    Label_for_header = []
                    for i in range(len((text_for_header))):
                        Label_for_header.append(tk.Label(Election_result_frame, text=text_for_header[i]))
                        Label_for_header[i].grid(row=0, column=i)
                    Sno_label = []
                    Candidate_label = []
                    faction_label = []
                    Votes_Label = []
                    for i in range(len(Order)):
                        Sno_label.append(tk.Label(Election_result_frame, text=i))
                        Sno_label[i].grid(row=i + 1, column=0)
                        Candidate_label.append(tk.Label(Election_result_frame, text=Order[i][0]))
                        Candidate_label[i].grid(row=i + 1, column=1)
                        '''
                        for j in range(len(candidates)):
                            if candidates[j]['candidate_id'] == Order[j][0]:
                               print(candidates[j]['candidate_id'])
                               print(Order[j][0])
                            else:
                                pass
                        '''

                        try:
                            faction = candidates[i]['faction']
                            faction_label.append(tk.Label(Election_result_frame, text=faction))
                            faction_label[i].grid(row=i + 1, column=2)
                        except:
                            faction_label.append(tk.Label(Election_result_frame, text="NA"))
                            faction_label[i].grid(row=i + 1, column=2)

                        Votes_Label.append(tk.Label(Election_result_frame, text=Order[i][1]))
                        Votes_Label[i].grid(row=i + 1, column=3)

                    for i in range(len(Order) + 1):
                        Election_result_frame.grid_columnconfigure(i, weight=1)
                        Election_result_frame.grid_rowconfigure(i, weight=1)

                    Elimination_result_frame = tk.LabelFrame(self.frame, text='Elimination order')
                    Elimination_result_frame.grid(row=4, column=0, sticky="news")
                    Round_Label=[]
                    Eliminated_Label=[]
                    text_for_header_2 = ["Eliminated in ","                 " ,"Candidate Eliminated"]
                    Label_for_header_2 = []
                    Empty_column=[]
                    for i in range(len((text_for_header_2))):
                        Label_for_header_2.append(tk.Label(Elimination_result_frame, text=text_for_header_2[i]))
                        Label_for_header_2[i].grid(row=0, column=i)
                    for i in range(len(Eliminated)):
                        Round_Label.append(tk.Label(Elimination_result_frame,text="Round_no." + str(i+1)))
                        Round_Label[i].grid(row=i+1 ,column=0)
                        Empty_column.append(tk.Label(Elimination_result_frame, text=''))
                        Empty_column[i].grid(row=i + 1, column=1)
                        Eliminated_Label.append(tk.Label(Elimination_result_frame, text= Eliminated[i]))
                        Eliminated_Label[i].grid(row=i + 1, column=2)
                elif type  == 'referendum':
                    Referendum_Reult = poll_result['referendum_result']
                    print(Referendum_Reult)
                    Result_Conversion_dictionary = {"app" : "Approve",
                                                    "dis" : "Disapprove",
                                                    "abs" : "Abstain"}


                    for i in range(3):

                        self.grid_rowconfigure(i, weight=1)
                    self.grid_columnconfigure(0, weight=1)
                    self.frame = tk.Frame(self)
                    self.frame.grid()

                    self.title_label = tk.Label(self.frame, text="THE RESULT ARE")
                    self.title_label.grid(row=0, column=0)

                    User_info_frame = tk.LabelFrame(self.frame)
                    User_info_frame.grid(row=1, column=0, sticky="news")
                    for i in range(5):
                        User_info_frame.grid_rowconfigure(i, weight=1)
                    for i in range(3):
                        User_info_frame.grid_columnconfigure(i, weight=1)

                    label1 = tk.Label(User_info_frame, text="By : " + name_of_institution, font=12)
                    label1.grid(row=1, column=1, pady=10, padx=0)
                    #
                    label2 = tk.Label(User_info_frame, text=title, font=12)
                    label2.grid(row=0, column=1, pady=10, padx=0)
                    #
                    label3 = tk.Label(User_info_frame, text=title)
                    label3.grid(row=2, column=1, pady=10, padx=0)
                    #
                    label4 = tk.Label(User_info_frame, text="Type : " + type)
                    label4.grid(row=3, column=0, pady=10, padx=0)
                    #
                    label5 = tk.Label(User_info_frame, text="Voter_turnout :" + str(voter_turnout))
                    label5.grid(row=3, column=2, pady=10, padx=0)
                    #
                    label6 = tk.Label(User_info_frame, text="Threshold :" + str(min_threshold))
                    label6.grid(row=4, column=0, pady=10, padx=0)

                    Result_info_frame = tk.LabelFrame(self.frame)
                    Result_info_frame.grid(row=2, column=0, sticky="news")

                    text_for_header = ["S. No", "Proposal_Name", "description", "Approve %" , "Dissaprove %" , "Abstain %" , "Result"]
                    Label_for_header = []
                    for i in range(len((text_for_header))):
                        Label_for_header.append(tk.Label(Result_info_frame, text=text_for_header[i]))
                        Label_for_header[i].grid(row=0, column=i,padx=5,pady=5)
                    Sno_Label_list=[]
                    name_Label_List = []
                    description_Label_List = []
                    approval_Label_List = []
                    disapproval_Label_List = []
                    abstention_Label_List = []
                    Result_Label_List = []
                    for i in range(len(Referendum_Reult)):
                        Sno_Label_list.append(tk.Label(Result_info_frame, text=str(i+1)))
                        name_Label_List.append(tk.Label(Result_info_frame, text=Referendum_Reult[i]['name']))
                        description_Label_List.append(tk.Label(Result_info_frame, text=Referendum_Reult[i]['description']))
                        approval_Label_List.append(tk.Label(Result_info_frame, text=Referendum_Reult[i]['approve_percent']))
                        disapproval_Label_List.append(tk.Label(Result_info_frame, text=Referendum_Reult[i]['disapprove_percent']))
                        abstention_Label_List.append(tk.Label(Result_info_frame, text=Referendum_Reult[i]['abstain_percent']))
                        Result_Label_List.append(tk.Label(Result_info_frame, text=Result_Conversion_dictionary[Referendum_Reult[i]['result']]))
                        Sno_Label_list[i].grid(row= i+1 , column=0 ,padx=5,pady=5)
                        name_Label_List[i].grid(row= i+1 , column=1,padx=5,pady=5)
                        description_Label_List[i].grid(row= i+1 , column=2,padx=5,pady=5)
                        approval_Label_List[i].grid(row= i+1 , column=3,padx=5,pady=5)
                        disapproval_Label_List[i].grid(row= i+1 , column=4,padx=5,pady=5)
                        abstention_Label_List[i].grid(row= i+1 , column=5,padx=5,pady=5)
                        Result_Label_List[i].grid(row= i+1 , column=6,padx=5,pady=5)

                print(poll_result)
        except Exception as exc:
            traceback.print_exc()
            tk.messagebox.showerror(message=str(exc))

        for i in range(1):
            self.grid_rowconfigure(i, weight=1)
        self.grid_columnconfigure(0, weight=1)
