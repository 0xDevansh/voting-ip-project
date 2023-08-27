import tkinter as tk
import tkinter.messagebox
import tkinter.ttk as ttk
from backend.db.Database import Database


# for easy access ref_entry is in referendum

class RefremdumEntryFrame(ttk.Frame):
    def __init__(self, app):
        super().__init__(app)
        num_refremdums = 5
        l1 = []

        l2 = []

        l3 = []
        def get_data():
            l4 = []
            l5 = []
            Data = {}
            for i in range(num_refremdums):
                if l2[i].get() and l3[i].get():
                   l4.append(l2[i].get())
                   l5.append(l3[i].get())
                   Data['refremdum ' + str(i+1)] = {"refremdum_name" : l4[i], "Party" : l5[i]}

                else:
                    tkinter.messagebox.showerror(title="Error", message='refremdum' + str(i+1) + 'data incomplete')
                    break

            print(l4)
            print(Data)



        self.frame = tk.Frame(self)
        self.frame.pack()

        ref_entry_frame = tk.LabelFrame(self.frame, text="refremdum Entry")
        ref_entry_frame.grid(row=0, column=0, sticky="news")


        for i in range(num_refremdums):
           l1.append(tk.Label(ref_entry_frame, text="refremdum" + str(i + 1)))
           l2.append(tk.Entry(ref_entry_frame))
           l3.append(tk.Entry(ref_entry_frame))

           l1[i].grid(row=i, column=0)
           l2[i].grid(row=i, column=1 , padx=50, pady=10)
           l3[i].grid(row=i, column=2, padx=50, pady=10)


        button = tk.Button(ref_entry_frame, text="Submit" , command= get_data)

        button.grid(row=num_refremdums, column=1)


