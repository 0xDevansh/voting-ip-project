import tkinter as tk
import tkinter.ttk as ttk
from .opening_page import OpeningPageFrame
from .other_pages import CreditsFrame

class App(tk.Tk):
    frames_data = {
        'opening': {'title': 'Main Page', 'frame': OpeningPageFrame},
        'credits': {'title': 'Credits', 'frame': CreditsFrame}
    }

    def __init__(self):
        super().__init__()
        print('App created')
        self.title('Poll Pilot')
        self.geometry('500x450')
        self.loaded_frames = {}

        # instantiate all frames
        for (name, frame) in App.frames_data.items():
            self.loaded_frames[name] = frame['frame'](self)

        # show main page
        self.show_frame('opening')

    def show_frame(self, frame_name):
        print(f'Showing {frame_name}...')
        frame = self.loaded_frames[frame_name]
        frame.tkraise()

    def show_frame_factory(self, frame_name):
        def show():
            print(f'Showing {frame_name}...')
            frame = self.loaded_frames[frame_name]
            frame.reset()
            frame.tkraise()
        return show

def start_application():
    app = App()
    app.mainloop()