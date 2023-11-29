import tkinter.ttk as ttk


class OpeningPageFrame(ttk.Frame):
    def __init__(self, app, context):
        super().__init__(app)

        # Main label frame for the opening page
        OpeningPageLabelFrame = ttk.LabelFrame(self)
        OpeningPageLabelFrame.grid(row=0, column=0)

        # Configuring row and column weights for proper layout
        for i in range(3):
            self.grid_columnconfigure(i, weight=1)
        for i in range(8):
            self.grid_rowconfigure(i, weight=1)

        # Headings and labels
        self.head1 = ttk.Label(self, text="POLL PILOT", font=('Times', 40))
        self.head1.grid(row=0, column=1, padx=10)
        self.head2 = ttk.Label(self, text=" A simple tool to conduct elections", font=('Times', 20))
        self.head2.grid(row=1, column=1, padx=10)

        # Buttons for different actions
        self.btn1 = ttk.Button(self, text="Create An Election", command=app.show_frame_factory('cre_elec'))
        self.btn1.grid(row=2, column=1, padx=50, pady=20, sticky='news')
        self.btn2 = ttk.Button(self, text="Create A Referendum", command=app.show_frame_factory('create_ref'))
        self.btn2.grid(row=3, column=1, padx=50, pady=20, sticky='news')
        self.btn2 = ttk.Button(self, text="Show Elections", command=app.show_frame_factory('elec_navigation'))
        self.btn2.grid(row=4, column=1, padx=50, pady=20, sticky='news')

        # Frame for help and credits buttons
        self.help_cred_holder = ttk.Frame(self)
        self.help_cred_holder.columnconfigure(0, weight=1)
        self.help_cred_holder.columnconfigure(1, weight=1)
        self.help_cred_holder.grid(row=5, column=1, sticky='news')

        # Help and Credits buttons
        self.btn3 = ttk.Button(self.help_cred_holder, text="Help", command=app.show_frame_factory('help'))
        self.btn3.grid(row=0, column=0, padx=50, pady=50, sticky='news')
        self.btn4 = ttk.Button(self.help_cred_holder, text="Credits", command=app.show_frame_factory('credits'))
        self.btn4.grid(row=0, column=1, padx=50, pady=50, sticky='news')
