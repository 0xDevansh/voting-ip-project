import tkinter as tk
import tkinter.messagebox
import tkinter.ttk as ttk
import traceback

from backend.db.Database import Database


class TreeViewNavigationFrame(ttk.Frame):
    def __init__(self, app, context):
        super().__init__(app)
        self.selected_poll = None

        polls = []
        try:
            db = Database.get_instance()
            polls = db.get_poll()
        except Exception as exc:
            traceback.print_exc()
            tk.messagebox.showerror(message=str(exc))

        poll_types = {
            'fptp': 'First past the post',
            'runoff': 'Runoff',
            'referendum': 'Referendum',
            'approval': 'Approval voting',
        }
        poll_status = {
            'not_started': 'Not started',
            'running': 'In progress',
            'completed': 'Completed',
        }

        columns = ['id', 'name', 'type', 'status']
        for i in range(1):
            self.grid_columnconfigure(i, weight=1)
            self.grid_rowconfigure(i,weight=0)

        Treeview_labelframe = ttk.LabelFrame(self)
        Treeview_labelframe.grid(row=0, column=0)
        Treeview_labelframe2 = ttk.LabelFrame(self)
        Treeview_labelframe2.grid(row=1, column=0)
        Text_Box_1 = ttk.Label(Treeview_labelframe, text="Created Elections")
        Text_Box_1.grid(row =0 , column=0)
        treeview = ttk.Treeview(Treeview_labelframe, columns=columns, show='headings', selectmode='browse')
        treeview.heading('id', text='Poll ID')
        treeview.heading('name', text='Name')
        treeview.heading('type', text='Type')
        treeview.heading('status', text='Status')

        for poll in polls:
            data = (poll['id'], poll['name'], poll_types[poll['type']], poll_status[poll['status']])
            
            treeview.insert('', tk.END, values=data)

        treeview.grid(row=1, column=0)

        # add a scrollbar
        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=treeview.yview)
        treeview.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')

        def item_selected(event):
            for selected in treeview.selection():
                item = treeview.item(selected)
                poll_id = item['values'][0]
                for poll in polls:
                    if poll['id'] == poll_id:
                        self.selected_poll = poll
                        print(self.selected_poll)
                Elec_command_button = ttk.Button(Treeview_labelframe, text="Select an Election")
                Elec_command_button.grid(row=2, column=0, padx=50, pady=10, sticky='news')

                if self.selected_poll['status'] == 'not_started':

                    Elec_command_button.destroy()
                    Elec_command_button= ttk.Button(Treeview_labelframe, text="Start Election",
                                                               command=app.show_frame_factory("start_election",
                                                                                              {'poll': self.selected_poll}))
                    Elec_command_button.grid(row=2, column=0, padx=50, pady=10, sticky='news')
                elif self.selected_poll['status'] == "running":

                    Elec_command_button.destroy()

                    Elec_command_button=ttk.Button(Treeview_labelframe, text='Add vote/Terminate',
                                                               command=app.show_frame_factory('voting_security_check',
                                                                                              {'poll': self.selected_poll}))
                    Elec_command_button.grid(row=2, column=0, padx=50, pady=10, sticky='news')
                elif self.selected_poll['status'] == 'completed':
                    Elec_command_button.destroy()
                    Elec_command_button = ttk.Button(Treeview_labelframe, text='See Result',
                                                               command=app.show_frame_factory('result_page',
                                                                                              {'poll': self.selected_poll}))
                    Elec_command_button.grid(row=2, column=0, padx=50, pady=10, sticky='news')

        treeview.bind('<<TreeviewSelect>>', item_selected)
       # Button_frame = ttk.LabelFrame(self)
        #Button_frame.grid(row=1, column=0, sticky="news")
        #for i in range(3):
        #    Button_frame.grid_columnconfigure(i, weight=1)

        def Help():
            tkinter.messagebox.showinfo(title="Help", message="Take Data from Documentation")

        navigation_frame = ttk.Frame(self)
        button1 = ttk.Button(navigation_frame, text="Help", command=Help)
        button1.grid(row=3, column=0, sticky='news', padx=10
                     , pady=10)
        button1 = ttk.Button(navigation_frame, text="Go Home", command=app.show_frame_factory('opening'))
        button1.grid(row=3, column=1, sticky='news', padx=10
                     , pady=10)
        navigation_frame.grid(row=3, column=0)

