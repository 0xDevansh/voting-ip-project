import tkinter as tk
import tkinter.ttk as ttk
from .opening_page import OpeningPageFrame
from .credits import CreditsFrame
from .help import Helpframe
from .create_election import CreateElectionFrame
from .cand_entry import CandidateEntryFrame
from .start_election_frame import StartElection
from .ftpt_election_window import VotingWindow
from .voting_security_check import VotingSecurityCheck
from .result_page import Result
class App(tk.Tk):
    # destruct_on_switch should be True for frames
    # that hold data or are entry forms
    frames_data = {
        'opening': {'title': 'Main Page', 'frame': OpeningPageFrame},
        'credits': {'title': 'Credits', 'frame': CreditsFrame},
        'help' : {'title' : 'Help??', 'frame' : Helpframe},
        'cre_elec': {'title' : 'Create election' , 'frame' : CreateElectionFrame},
        'cand_entry' : {'title' : 'Enter Candidates' , 'frame' : CandidateEntryFrame},
        'start_election': {'title': 'Start Election', 'frame': StartElection},
        'voting_window' : {'title': 'Voting Window', 'frame': VotingWindow},
        'voting_security_check' : {'title': 'Security check', 'frame': VotingSecurityCheck},
        'result_page': {'title': 'Result', 'frame': Result},

    }

    def __init__(self):
        super().__init__()
        print('App created')
        self.title('Poll Pilot')
        # self.geometry('500x450')
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.current_frame_name = 'opening'
        self.current_frame = None

        # show main page
        self.show_frame('opening')

    def show_frame(self, frame_name, context = None):
        function = self.show_frame_factory(frame_name, context)
        function()

    def show_frame_factory(self, frame_name, context=None):
        def show_function():
            print(f'Showing {frame_name}...')
            # Remove current frame
            self.current_frame = None

            frame = App.frames_data[frame_name]['frame'](self, context)
            frame.grid(row=0, column=0, sticky='news')
            self.current_frame = frame

            self.title('Poll Pilot - ' + App.frames_data[frame_name]['title'])
            self.current_frame_name = frame_name
        return show_function

def start_application():
    app = App()
    app.mainloop()