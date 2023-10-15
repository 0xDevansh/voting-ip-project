import tkinter as tk
import tkinter.ttk as ttk

class OpeningPageFrame(ttk.Frame):
    def __init__(self, app, context):
        super().__init__(app)

        OpeningPagelabelframe=ttk.LabelFrame(self)
        OpeningPagelabelframe.grid(row=0,column=0)
        for i in range(3):
            self.grid_columnconfigure(i, weight=1)
        for i in range(8):
            self.grid_rowconfigure(i, weight=1)
        empty_label1=[]
        empty_label2=[]
        for i in range(8):
            empty_label1.append(ttk.Label(self))
            empty_label1[i].grid(row=i ,column=0)
            empty_label2.append(ttk.Label(self))
            empty_label2[i].grid(row=i, column=2)

        self.head1 = ttk.Label(self, text="POLL PILOT", font=('Times', 40))
        self.head1.grid(row=0, column=1, padx= 10 )
        self.head2 = ttk.Label(self, text=" A simple tool to conduct elections", font=('Times', 20))
        self.head2.grid(row=1, column=1, padx= 10)

        self.btn1 = ttk.Button(self, text="Create An Election", command=app.show_frame_factory('cre_elec'))
        self.btn1.grid(row=2, column=1, padx= 50 , pady= 20 ,sticky='news')
        self.btn2 = ttk.Button(self, text="Create A Referendum", command=app.show_frame_factory('create_ref'))
        self.btn2.grid(row=3, column=1, padx= 50 , pady= 20,sticky='news')
        self.btn2 = ttk.Button(self, text="Show Elections", command=app.show_frame_factory('elec_navigation'))
        self.btn2.grid(row=4, column=1, padx= 50 , pady= 20,sticky='news')

        self.help_cred_holder = ttk.Frame(self)
        self.help_cred_holder.columnconfigure(0, weight=1)
        self.help_cred_holder.columnconfigure(1, weight=1)
        self.help_cred_holder.grid(row=5, column=1, sticky='news')
        self.btn3 = ttk.Button(self.help_cred_holder, text="Help", command=app.show_frame_factory('help'))
        self.btn3.grid(row=0, column=0, padx= 50 , pady= 50,sticky='news')
        self.btn4 = ttk.Button(self.help_cred_holder, text="Credits", command=app.show_frame_factory('credits'))
        self.btn4.grid(row=0, column=1, padx= 50 , pady= 50,sticky='news')

        #self.btn5 = ttk.Button(self, text="TESTS", command=app.show_frame_factory('result_page'))
        #self.btn5.grid(row=7, column=0, padx= 50 , pady= 10)