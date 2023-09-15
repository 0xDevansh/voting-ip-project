import tkinter as tk
import tkinter.messagebox
import tkinter.ttk as ttk

from backend.db.Database import Database


class ElectionNavigationFrame(ttk.Frame):
    def __init__(self, app, context):
        super().__init__(app)

        self.frame = tk.Frame(self)
        self.frame.pack()

        db = Database.get_instance()
        polls = db.get_poll()
        print(polls)
       # election_nav_frame_1 = tk.LabelFrame(self.frame)
        #election_nav_frame_1.grid(row=0, column=0, sticky="news")
        election_nav_frame_2 = tk.LabelFrame(self.frame)
        election_nav_frame_2.grid(row=0, column=0, sticky="news")
        text_for_labels = ["Election  name","Type" ,"Status", "Commands"]
        Labels = []
        for i in range(len((text_for_labels))):
            Labels.append(tk.Label(election_nav_frame_2,text=text_for_labels[i]))
            Labels[i].grid(row = 0 , column= i, padx= 50)

        Ref_name_label=[]
        Ref_type_label=[]
        Ref_status_Label=[]

        Ref_command_button_1=[]
        for i, poll in enumerate(polls):

            Ref_name_label.append(tk.Label(election_nav_frame_2, text=poll['name']))
            Ref_type_label.append(tk.Label(election_nav_frame_2, text=poll['type']))
            Ref_status_Label.append(tk.Label(election_nav_frame_2,text=poll['status']))


            Ref_name_label[i].grid(row=i+1, column=0,padx=50)
            Ref_type_label[i].grid(row=i+1, column=1,padx=50)
            Ref_status_Label[i].grid(row=i+1, column=2, padx=50, pady=10)

            if poll['status'] == 'not_started':
                 Ref_command_button_1.append(tk.Button(election_nav_frame_2,text="Start Election", command= app.show_frame_factory("start_election", {'poll': poll})))
                 Ref_command_button_1[i].grid(row=i+1, column=3, padx=50, pady=10,sticky='news')
            elif poll['status'] == "running":
                Ref_command_button_1.append(tk.Button(election_nav_frame_2,text='Add vote/Terminate' , command=app.show_frame_factory('voting_security_check', {'poll': poll})))
                Ref_command_button_1[i].grid(row=i+1, column=3, padx=50, pady=10, sticky='news')
            elif poll['status'] == 'completed':
                Ref_command_button_1.append(tk.Button(election_nav_frame_2, text= 'See Result',
                                                      command=app.show_frame_factory('result_page', {'poll': poll})))
                Ref_command_button_1[i].grid(row=i+1, column=3, padx=50, pady=10,sticky='news')



