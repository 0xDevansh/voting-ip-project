import tkinter as tk
import tkinter.messagebox
import tkinter.ttk as ttk

# StartElectionFrame: Frame for starting the election
class StartElectionFrame(ttk.Frame):
    def __init__(self, app, context):
        super().__init__(app)
        poll = context['poll']
        sec_key = poll['security_key']

        # Function to start the election
        def start_election():
            ent_password = entry1.get()

            if ent_password == sec_key:
                app.show_frame('voting_window', context={'poll': poll})
            else:
                tkinter.messagebox.showerror(title="Error", message="Security key is incorrect")

        # Configure row and column weights
        for i in range(4):
            self.grid_rowconfigure(i, weight=1)
        for i in range(1):
            self.grid_columnconfigure(i, weight=1)

        # Create frame
        self.frame = ttk.Frame(self)
        self.frame.grid()

        # Election created message
        label1 = ttk.Label(self, text="Your election has been created", font=20)
        label1.grid(row=0, column=0, pady=10)

        # Security Key entry
        label2 = ttk.Label(self, text="Enter Security Key to Start")
        label2.grid(row=1, column=0, pady=10)
        entry1 = tk.Entry(self, show='*')
        entry1.grid(row=2, column=0)

        # Checkbox to show/hide password
        checked = tk.BooleanVar(value=False)

        def show_and_hide():
            if checked.get():
                entry1['show'] = ''
            else:
                entry1['show'] = '*'

        checkBox_showPassword = ttk.Checkbutton(
            self, text="Show password", command=show_and_hide, variable=checked, onvalue=True, offvalue=False
        )
        checkBox_showPassword.grid(row=3, column=0)

        # Start and Back buttons
        start_button = tk.Button(self, text="Start", command=start_election)
        start_button.grid(row=4, column=0, pady=10)

        back_button = tk.Button(self, text="Back", command=app.show_frame_factory('elec_navigation'))
        back_button.grid(row=5, column=0, pady=10)
