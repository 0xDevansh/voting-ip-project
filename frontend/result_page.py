import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from backend.utils import get_keys_with_value
from backend.approval import calculate_approval
from backend.fptp import calculate_fptp

class Result(ttk.Frame):
    def __init__(self, app, context):
        super().__init__(app)
        candidates = ['modi', 'lakshman-singh', 'trump', 'CAK']
        votes = [ 'trump', 'lakshman-singh', 'CAK' , 'modi' , 'trump']
        num_voters = 100
        name_of_institution = "GVN"
        title = "The Big Dumb"
        type = 'fptp'
        max_approved =  3
        min_threshold = 1
        voter_turnout = round(((len(votes))/(num_voters))*100,1)
        def Generate():
            if type  == 'approval':
                   result = calculate_approval(votes , candidates , max_approved = max_approved, min_threshold = min_threshold)
                   Winners = result['winners']
                   Order = result['order']
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
                   for i in range(len(candidates)):
                       l1.append('')
                       l1[i] = tk.Label(       User_info_frame, text= str(Order[i]) )
                       l1[i].grid(row=7+i, column=1, pady=10, padx=0)
                   print(result)

            elif type  == 'fptp':
                   result = calculate_fptp(votes , candidates)
                   Winners = result['winners']
                   Order = result['order']
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
                   for i in range(len(candidates)):
                       l1.append('')
                       l1[i] = tk.Label(       User_info_frame, text= str(Order[i]) )
                       l1[i].grid(row=6+i, column=1, pady=10, padx=0)






                   print(result)

        for i in range(1):
            self.grid_rowconfigure(i, weight=1)
        self.grid_columnconfigure(0, weight=1)

        btn1 =tk.Button(self, text="Generate Result" , command = Generate)
        btn1.grid(row = 0 , column= 0)
