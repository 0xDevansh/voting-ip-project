import tkinter as tk
import tkinter.messagebox
import tkinter.ttk as ttk
import traceback

from backend.db.Database import Database


class ElectionNavigationFrame(ttk.Frame):
    def __init__(self, app, context):
        super().__init__(app)

        self.frame = tk.Frame(self)
        self.frame.pack()

        try:
            db = Database.get_instance()
            polls = db.get_poll()
        except Exception as exc:
            traceback.print_exc()
            tk.messagebox.showerror(message=str(exc))

        election_nav_frame = tk.LabelFrame(self.frame)
        election_nav_frame.grid(row=0, column=0, sticky="news")
        text_for_labels = ["Election  name","Type" ,"Status", "Commands"]
        Labels = []
        for i in range(len((text_for_labels))):
            Labels.append(tk.Label(election_nav_frame,text=text_for_labels[i]))
            Labels[i].grid(row = 0 , column= i, padx= 50)
        Elec_Label_frame = [tk.LabelFrame(self.frame)]
        Elec_name_label=[]
        Elec_type_label=[] 
        Elec_status_Label=[] 

        Elec_command_button_1=[]
        for i, poll in enumerate(polls):
            Elec_Label_frame.append(tk.LabelFrame(self.frame))
            Elec_Label_frame[i].grid(row=i+1 ,column=0,sticky='news' ,pady=10)

            Elec_name_label.append(tk.Label(Elec_Label_frame[i], text=poll['name']))
            Elec_type_label.append(tk.Label(Elec_Label_frame[i], text=poll['type']))
            Elec_status_Label.append(tk.Label(Elec_Label_frame[i],text=poll['status']))


            Elec_name_label[i].grid(row=0, column=0,padx=50,sticky='news')
            Elec_type_label[i].grid(row=0, column=1,padx=50,sticky='news')
            Elec_status_Label[i].grid(row=0, column=2, padx=50,sticky='news')

            if poll['status'] == 'not_started':
                 Elec_command_button_1.append(tk.Button(Elec_Label_frame[i],text="Start Election", command= app.show_frame_factory("start_election", {'poll': poll})))
                 Elec_command_button_1[i].grid(row=0, column=3, padx=50, pady=10,sticky='news')
            elif poll['status'] == "running":
                Elec_command_button_1.append(tk.Button(Elec_Label_frame[i],text='Add vote/Terminate' , command=app.show_frame_factory('voting_security_check', {'poll': poll})))
                Elec_command_button_1[i].grid(row=0, column=3, padx=50, pady=10, sticky='news')
            elif poll['status'] == 'completed':
                Elec_command_button_1.append(tk.Button(Elec_Label_frame[i], text= 'See Result',
                                                      command=app.show_frame_factory('result_page', {'poll': poll})))
                Elec_command_button_1[i].grid(row=0, column=3, padx=50, pady=10,sticky='news')



