import tkinter
import tkinter as tk
import tkinter.ttk as ttk
import traceback
from tkinter import messagebox

from backend.db.Database import Database

class ResultFrame(ttk.Frame):
    def __init__(self, app, context):
        super().__init__(app)
        #Database Data Retrival
        poll = context['poll']
        try:
            db = Database.get_instance()
            candidates = db.get_poll_candidates(poll['id'])
            actual_num_votes = db.get_num_votes(poll['id'])
            if poll['type'] == 'referendum':
                candidates = db.get_poll_proposals(poll['id'])
            # to switch between id and name
            candidate_id_name = {}
            for cand in candidates:
                candidate_id_name[cand['candidate_id']] = cand['name']

            num_voters = poll['num_voters']
            name_of_institution = poll['inst_name']
            title = poll['name']
            description = poll['description']
            type = poll['type']
            max_approved =  poll['max_approved']
            min_threshold = poll['min_threshold']
            voter_turnout = round((actual_num_votes/(num_voters))*100,1)

            poll_result = db.get_result(poll['id'])
            if poll['type'] != 'referendum' and len(poll_result['winners']) == 0:
                poll_result['winners'] = ['nota']
                candidates.append({'candidate_id': 'nota', 'name': 'No candidate cleared the minimum vote threshold.', 'faction': 'NA'})
            if not poll_result:
                raise Exception('Result not found')
            # Switch candidate ids with names
            candidate_id_name = {}
            for cand in candidates:
                candidate_id_name[cand['candidate_id']] = cand['name']
            if 'winners' in poll_result and poll_result['winners'] != None:
                poll_result['winners'] = list(map(lambda w:candidate_id_name[w], poll_result['winners']))
            if 'eliminated' in poll_result and poll_result['eliminated'] != None:
                poll_result['eliminated'] = list(map(lambda w:candidate_id_name[w], poll_result['eliminated']))
            if 'order' in poll_result and poll_result['order'] != None and poll['type'] != 'runoff':
                poll_result['order'] = list(map(lambda o:[candidate_id_name[o[0]], o[1]], poll_result['order']))


            # Result page for election voting through approval voting
            if type  == 'approval':
                Winners = poll_result['winners']
                Order = poll_result['order']

                for i in range(3):
                    self.grid_rowconfigure(i, weight=1)
                self.grid_columnconfigure(0, weight=1)
                self.frame = ttk.Frame(self)
                self.frame.grid()

                self.title_label = ttk.Label(self.frame, text= "THE RESULT ARE")
                self.title_label.grid(row=0, column=0)
                # Display frame Setup

                User_info_frame = ttk.LabelFrame(self.frame)
                User_info_frame.grid(row=1, column=0, sticky="news")

                label1 = ttk.Label(       User_info_frame, text = "By : " + name_of_institution , font=12)
                label1.grid(row=1,column=1 ,pady= 10 , padx=0)
                #
                label2 = ttk.Label(       User_info_frame, text= title , font= 12)
                label2.grid(row=0, column=1, pady=10, padx=0)
                #
                label3 = ttk.Label(User_info_frame, text=description)
                label3.grid(row=2, column=1, pady=10, padx=0)
                #
                label4 = ttk.Label(       User_info_frame, text="Type : "  +  type)
                label4.grid(row=3, column=0, pady=10, padx=0)
                #
                label5 = ttk.Label(       User_info_frame, text="Voter% :" + str(voter_turnout) + '%')
                label5.grid(row=3, column=2, pady=10, padx=0)
                #
                label6 = ttk.Label(       User_info_frame, text="max approved : " + str(max_approved))
                label6.grid(row=4, column=0, pady=10, padx=0)
                #
                label7 = ttk.Label(       User_info_frame, text='min_threshold :' + str(min_threshold))
                label7.grid(row=4, column=2, pady=10, padx=0)
                # Winner Info frame Setup
                Winner_info_frame = ttk.LabelFrame(self.frame, text = 'The Winner is')
                Winner_info_frame.grid(row=2, column=0, sticky="news")
                Label_for_winner = []
                for i in range(len(Winners)):
                    Label_for_winner.append(ttk.Label(Winner_info_frame,text= 'Winner :- ' + Winners[i] ,font= 12))
                    Label_for_winner[i].grid(row =i , column = 0 ,sticky= 'news')
                    Winner_info_frame.grid_columnconfigure(i, weight=1)
                Election_result_frame = ttk.LabelFrame(self.frame, text = 'Total Result')
                Election_result_frame.grid(row=3, column=0, sticky="news")
                text_for_header=["S. No" , "Candidate" , "faction" , " Votes"]
                Label_for_header=[]
                for i in range(len((text_for_header))):
                    Label_for_header.append(ttk.Label(Election_result_frame,text= text_for_header[i]))
                    Label_for_header[i].grid(row =0 , column= i)
                # Setting basic variable and placing labels

                Rno_label=[]
                Candidate_label=[]
                faction_label=[]
                Votes_Label=[]
                for i in range(len(Order)):
                    Rno_label.append(ttk.Label(Election_result_frame, text= i))
                    Rno_label[i].grid(row=i+1, column=0)
                    Candidate_label.append(ttk.Label(Election_result_frame, text=Order[i][0]))
                    Candidate_label[i].grid(row=i + 1, column=1)
                    try:
                        faction = 'None'
                        for cand in candidates:
                            if cand['name'] == Order[i][0]:
                                faction = cand['faction']
                                break
                        faction_label.append(ttk.Label(Election_result_frame, text=faction))
                        faction_label[i].grid(row=i + 1, column=2)
                    except:
                        faction_label.append(ttk.Label(Election_result_frame, text="NA"))
                        faction_label[i].grid(row=i + 1, column=2)


                    Votes_Label.append(ttk.Label(Election_result_frame, text=Order[i][1]))
                    Votes_Label[i].grid(row=i + 1, column=3)

                for i in range(len(Order) + 1):
                    Election_result_frame.grid_columnconfigure(i, weight=1)
                    Election_result_frame.grid_rowconfigure(i, weight=1)




            #electiong result for election through FTPT
            elif type  == 'fptp':
                Winners = poll_result['winners']
                Order = poll_result['order']

                for i in range(3):
                    self.grid_rowconfigure(i, weight=1)
                self.grid_columnconfigure(0, weight=1)
                self.frame = ttk.Frame(self)
                self.frame.grid()

                self.title_label = ttk.Label(self.frame, text= "THE RESULT ARE")
                self.title_label.grid(row=0, column=0)
                # Heading frame Setup
                User_info_frame = ttk.LabelFrame(self.frame)
                User_info_frame.grid(row=1, column=0, sticky="news")

                label1 = ttk.Label(User_info_frame, text="By : " + name_of_institution, font=12)
                label1.grid(row=1, column=1, pady=10, padx=0)
                #
                label2 = ttk.Label(User_info_frame, text=title, font=12)
                label2.grid(row=0, column=1, pady=10, padx=0)
                #
                label4 = ttk.Label(User_info_frame, text="Type : " + type)
                label4.grid(row=3, column=0, pady=10, padx=0)
                #
                label5 = ttk.Label(User_info_frame, text="Voter turnout%:" + str(voter_turnout))
                label5.grid(row=3, column=2, pady=10, padx=0)
                # Winner Info frame Setup
                Winner_info_frame = ttk.LabelFrame(self.frame, text='The Winner is')
                Winner_info_frame.grid(row=2, column=0, sticky="news")
                Label_for_winner = []
                for i in range(len(Winners)):
                    Label_for_winner.append(
                        ttk.Label(Winner_info_frame, text='Winner :- ' + Winners[i], font=12))
                    Label_for_winner[i].grid(row=i, column=0, sticky='news')
                    Winner_info_frame.grid_columnconfigure(i, weight=1)
                Election_result_frame = tk.LabelFrame(self.frame, text='Total Result')
                Election_result_frame.grid(row=3, column=0, sticky="news")
                text_for_header = ["S. No", "Candidate", "Faction", " Votes"]
                Label_for_header = []
                for i in range(len((text_for_header))):
                    Label_for_header.append(tk.Label(Election_result_frame, text=text_for_header[i]))
                    Label_for_header[i].grid(row=0, column=i)
                #Setting Basic Variable and Place Label
                Rno_label = []
                Candidate_label = []
                faction_label = []
                Votes_Label = []
                for i in range(len(Order)):
                    Rno_label.append(tk.Label(Election_result_frame, text=i+1))
                    Rno_label[i].grid(row=i + 1, column=0)
                    Candidate_label.append(tk.Label(Election_result_frame, text=Order[i][0]))
                    Candidate_label[i].grid(row=i + 1, column=1)
                    try:
                        faction = 'None'
                        for cand in candidates:
                            if cand['name'] == Order[i][0]:
                                faction = cand['faction']
                                break
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
            #Election result for Runoff election
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
                # Heading frame Setup

                User_info_frame = tk.LabelFrame(self.frame)
                User_info_frame.grid(row=1, column=0, sticky="news")

                for i in range(4):
                    User_info_frame.grid_rowconfigure(i, weight=1)
                for i in range(3):
                    User_info_frame.grid_columnconfigure(0, weight=1)

                label1 = tk.Label(User_info_frame, text="By : " + name_of_institution, font=12)
                label1.grid(row=1, column=1, pady=10, padx=0)
                #
                label2 = tk.Label(User_info_frame, text=title, font=12)
                label2.grid(row=0, column=1, pady=10, padx=0)
                #
                label4 = tk.Label(User_info_frame, text="Type : " + type)
                label4.grid(row=3, column=0, pady=10, padx=0)
                #
                label5 = tk.Label(User_info_frame, text="Voter_turnout :" + str(voter_turnout))
                label5.grid(row=3, column=2, pady=10, padx=0)
                # Winner Info frame Setup

                Winner_info_frame = tk.LabelFrame(self.frame, text='The Winner is')
                Winner_info_frame.grid(row=2, column=0, sticky="news")
                Label_for_winner = []
                for i in range(1):
                    Label_for_winner.append(
                        tk.Label(Winner_info_frame, text='Winner :- ' + Winners[0], font=12))
                    Label_for_winner[i].grid(row=i, column=0, sticky='news')
                    Winner_info_frame.grid_columnconfigure(i, weight=1)
                # Election frame Setup

                Election_result_frame = tk.LabelFrame(self.frame, text='First Preference Votes')
                Election_result_frame.grid(row=3, column=0, sticky="news")
                text_for_header = ["Round Number"]
                for i in range(1):
                    Candidate_Order = Order[i]
                    for j in Order[i].keys():
                        text_for_header.append(candidate_id_name[j])

                Label_for_header = []
                for i in range(len((text_for_header))):
                    Label_for_header.append(tk.Label(Election_result_frame, text=text_for_header[i]))
                    Label_for_header[i].grid(row=0, column=i)
                #Setting Basic Variable and placing label

                Rno_label = []
                Round_score_Label=[]
                faction_label = []
                Votes_Label = []

                for i in range(len(Order)):
                    k=0
                    Rno_label.append(tk.Label(Election_result_frame, text=str(i+1)))
                    Rno_label[i].grid(row=i + 1, column=0)
                    Round_score_Label.append([])
                    for j in Order[i].keys():
                        Round_score_Label[i].append(tk.Label(Election_result_frame, text=str(Order[i][j])))
                        Round_score_Label[i][k].grid(row = i+1 ,column = k+1)
                        k+=1

                for i in range(len(Order) + 1):
                    Election_result_frame.grid_columnconfigure(i, weight=1)
                    Election_result_frame.grid_rowconfigure(i, weight=1)
                # Roundwise Result frame Setup

                if len(Eliminated) > 0:
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

            #Election result page for referendum election
            elif type  == 'referendum':
                Referendum_Reult = poll_result['referendum_result']
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
                # Main Heading frame Setup
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
                # Election result frame Setup

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

        except Exception as exc:
            traceback.print_exc()
            tk.messagebox.showerror(message=str(exc))

        for i in range(1):
            self.grid_rowconfigure(i, weight=1)
        self.grid_columnconfigure(0, weight=1)

        Button_frame = ttk.LabelFrame(self.frame)
        Button_frame.grid(row=10, column=0, sticky="news")
        for i in range(3):
            Button_frame.grid_columnconfigure(i, weight=1)
        #Help Section Setup

        def Help():
            tkinter.messagebox.showinfo(title="Help", message="Take Data from Documentation")

        button1 = ttk.Button(Button_frame, text="Help", command=Help)
        button1.grid(row=0, column=0, sticky='news', padx=10
                     , pady=10)
        button1 = ttk.Button(Button_frame, text="Go Back", command=app.show_frame_factory('elec_navigation'))
        button1.grid(row=0, column=2, sticky='news', padx=10
                     , pady=10)
