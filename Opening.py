import tkinter as tk
from tkinter import ttk


def switch_to_help():
    if help.state() == 'withdrawn':
        help.deiconify()
        window.withdraw()
    else:
        help.withdraw()
        window.deiconify()
def switch_to_help_2():
    if help.state() == 'withdrawn':
        help.deiconify()
        createelec.withdraw()
    else:
        help.withdraw()
        createelec.deiconify()
def switch_to_credits():
    if credits.state() == 'withdrawn':
        credits.deiconify()
        window.withdraw()
    else:
        credits.withdraw()
        window.deiconify()


def switch_to_createref():
    if createref.state() == 'withdrawn':
        createref.deiconify()
        window.withdraw()
    else:
        createref.withdraw()
        window.deiconify()

def switch_to_createelec():
    if createelec.state() == 'withdrawn':
        createelec.deiconify()
        window.withdraw()
    else:
        createelec.withdraw()
        window.deiconify()
root = tk.Tk()

window = tk.Toplevel(root)
window.geometry('500x300')
window.title('POLL PILOT')

Head1 = tk.Label(window, text="POLL PILOT", font=('Times', 12))
Head1.place(x=170, y=10, height=20)
Head2 = tk.Label(window, text=" A simple tool to conduct election", font=('Helvetica', 10))
Head2.place(x=120, y=30, height=20)

btn1 = ttk.Button(window, text="      Create An Election        ", command= switch_to_createelec)
btn1.place(x=130, y=100, height=30)
btn2 = ttk.Button(window, text="        Create A Refrendum       " , command= switch_to_createref)
btn2.place(x=150, y=150, height=30)
btn3 = ttk.Button(window, text="            HELP??              ", command=switch_to_help)
btn3.place(x=130, y=200, height=30)
btn4 = ttk.Button(window, text="            Credits                  ", command=switch_to_credits)
btn4.place(x=150, y=250, height=30)

# NEW createelec WINDOW 
createelec = tk.Toplevel(root)
createelec.geometry('500x300')
createelec.title('createelec')
#Text to be added to info label from the Documentation
info = tk.Label(createelec, text="Please Select The system of Election")
info.pack()
btn1 = ttk.Button(createelec, text="      First Past the Post      ")
btn1.place(x=160, y=50, height=30)
btn2 = ttk.Button(createelec, text="        Instant Runoff         ")
btn2.place(x=160, y=125, height=30)
btn3 = ttk.Button(createelec, text="         Approval Voting       ")
btn3.place(x=160, y=200, height=30)
btn4 = tk.Button(createelec, text="    Help   ", command= switch_to_help_2)
btn4.place(x=100, y=250, height=20)
btn5 = tk.Button(createelec, text="    Back   ", command= switch_to_createelec)
btn5.place(x=400, y=250, height=20)

createelec.withdraw()


# A WINDOW TO CREATE REFRENDUM
createref = tk.Toplevel(root)
createref.geometry('500x300')
createref.title('createref')
#Text to be added to info label from the Documentation
info = tk.Label(createref, text="To be built latter")
info.pack()
btn4 = tk.Button(createref, text="    Back   ", command=switch_to_createref)
btn4.place(x=400, y=250, height=20)

createref.withdraw()
# NEW HELP WINDOW 
help = tk.Toplevel(root)
help.geometry('500x300')
help.title('Help')
#Text to be added to info label from the Documentation
info = tk.Label(help, text="Will be updated soon")
info.pack()
btn4 = tk.Button(help, text="    Back   ", command=switch_to_help)
btn4.place(x=400, y=250, height=20)

help.withdraw()


# NEW credits WINDOW 
credits = tk.Toplevel(root)
credits.geometry('500x300')
credits.title('credits')
#Text to be added to info label from the Documentation
info1 = tk.Label(credits, text="By:")
info1.pack()
info2 = tk.Label(credits, text="Atharv Dubey &")
info2.pack()
info3 = tk.Label(credits, text="Devansh Kandpal")
info3.pack()
btn4 = tk.Button(credits, text="    Back   ", command=switch_to_credits)
btn4.place(x=400, y=250, height=20)

credits.withdraw()
root.withdraw()
root.mainloop()
