import tkinter as tk
import tkinter.messagebox
import tkinter.ttk as ttk
class ElectionNavigationFrame(ttk.Frame):
    def __init__(self, app, context):
        super().__init__(app)

        self.frame = tk.Frame(self)
        self.frame.pack()
        Election_name_list=["Elec_1" ,"Elec_2" ,"Elec_3","Elec_4"]
        Election_Status_List = ["Not_Started" , "Completed" , 'Running' , 'Not_Started']
       # election_nav_frame_1 = tk.LabelFrame(self.frame)
        #election_nav_frame_1.grid(row=0, column=0, sticky="news")
        election_nav_frame_2 = tk.LabelFrame(self.frame)
        election_nav_frame_2.grid(row=0, column=0, sticky="news")
        text_for_labels = ["Election  name", "Status", "Commands"]
        Labels = []
        for i in range(len((text_for_labels))):
            Labels.append(tk.Label(election_nav_frame_2,text=text_for_labels[i]))
            Labels[i].grid(row = 0 , column= i, padx= 50)

        Ref_name_label=[]
        Ref_status_Label=[]
        Ref_command_button_1=[]
        for i in range(len(Election_Status_List)):

            Ref_name_label.append(tk.Label(election_nav_frame_2, text=Election_name_list[i]))
            Ref_status_Label.append(tk.Label(election_nav_frame_2,text=Election_Status_List[i]))


            Ref_name_label[i].grid(row=i+1, column=0,padx=50)
            Ref_status_Label[i].grid(row=i+1, column=1, padx=50, pady=10)

            if Election_Status_List[i] == 'Not_Started':
                 Ref_command_button_1.append(tk.Button(election_nav_frame_2,text="Start Election", command= app.show_frame_factory("start_election")))
                 Ref_command_button_1[i].grid(row=i+1, column=2, padx=50, pady=10,sticky='news')
            elif Election_Status_List[i] == "Running":
                Ref_command_button_1.append(tk.Button(election_nav_frame_2,text='Add vote/Terminate' , command=app.show_frame_factory('voting_security_check')))
                Ref_command_button_1[i].grid(row=i+1, column=2, padx=50, pady=10, sticky='news')
            elif Election_Status_List[i] == 'Completed':
                Ref_command_button_1.append(tk.Button(election_nav_frame_2, text= 'See Result',
                                                      command=app.show_frame_factory('result_page')))
                Ref_command_button_1[i].grid(row=i+1, column=2, padx=50, pady=10,sticky='news')



