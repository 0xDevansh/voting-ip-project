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
        treeview = ttk.Treeview(self, columns=columns, show='headings', selectmode='browse')
        treeview.heading('id', text='Poll ID')
        treeview.heading('name', text='Name')
        treeview.heading('type', text='Type')
        treeview.heading('status', text='Status')

        for poll in polls:
            data = (poll['id'], poll['name'], poll_types[poll['type']], poll_status[poll['status']])
            treeview.insert('', tk.END, values=data)

        treeview.grid(row=0, column=0, sticky='news')

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

        treeview.bind('<<TreeviewSelect>>', item_selected)