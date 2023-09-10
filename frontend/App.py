import tkinter as tk
import tkinter.ttk as ttk
from .opening_page import OpeningPageFrame
from .credits import CreditsFrame
from .help import Helpframe
from .data_entry import ElectionDataEntryFrame
from .cand_entry import CandidateEntryFrame
from .start_election_frame import StartElection
from .ftpt_election_window import VotingWindow
from .Voting_security_check import VotingSecurityCheck
from .result_page import Result
class App(tk.Tk):
    # destruct_on_switch should be True for frames
    # that hold data or are entry forms
    frames_data = {
        'opening': {'title': 'Main Page', 'frame': OpeningPageFrame, 'destruct_on_switch': False},
        'credits': {'title': 'Credits', 'frame': CreditsFrame,  'destruct_on_switch': False},
        'help' : {'title' : 'Help??', 'frame' : Helpframe,  'destruct_on_switch': False},
        'cre_elec': {'title' : 'Create election' , 'frame' : ElectionDataEntryFrame,  'destruct_on_switch': True},
        'cand_entry' : {'title' : 'Enter Candidates' , 'frame' : CandidateEntryFrame,  'destruct_on_switch': True},
        'start_election': {'title': 'Start Election', 'frame': StartElection,  'destruct_on_switch': True},
        'voting_window' : {'title': 'Voting Window', 'frame': VotingWindow,  'destruct_on_switch': True},
        'voting_security_check' : {'title': 'Security check', 'frame': VotingSecurityCheck,  'destruct_on_switch': True},
        'result_page': {'title': 'Result', 'frame': Result,  'destruct_on_switch': True}

    }

    def __init__(self):
        super().__init__()
        print('App created')
        self.title('Poll Pilot')
        # self.geometry('500x450')
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.loaded_frames = {}
        self.current_frame = 'opening'

        # show main page
        self.show_frame('opening')

    def show_frame(self, frame_name, context = None):
        function = self.show_frame_factory(frame_name, context)
        function()

    def show_frame_factory(self, frame_name, context=None):
        def show_function():
            print(f'Showing {frame_name}...')
            # Remove current frame if it needs to be destructed
            if App.frames_data[self.current_frame]['destruct_on_switch']:
                del self.loaded_frames[self.current_frame]

            # Look for existing in loaded_frames
            if frame_name in self.loaded_frames.keys():
                frame = self.loaded_frames[frame_name]
                frame.tkraise()
            else:
                frame = App.frames_data[frame_name]['frame'](self, context)
                frame.grid(row=0, column=0, sticky='news')
                self.loaded_frames[frame_name] = frame

            self.title('Poll Pilot - ' + App.frames_data[frame_name]['title'])
            self.current_frame = frame_name
        return show_function

def start_application():
    app = App()
    app.mainloop()