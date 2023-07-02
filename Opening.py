import tkinter as tk


def switch():
    if wis.state() == 'withdrawn':
        wis.deiconify()
        window.withdraw()
    else :
        wis.withdraw()
        window.deiconify()


root = tk.Tk()

window = tk.Toplevel(root)
window.geometry('500x300')
window.title('ELECTION SOLUTION')

Head1 = tk.Label(window, text="ELECTION SOLUTION", font=('Helvetica', 12))
Head1.place(x=170, y=10, height=20)
Head2 = tk.Label(window, text=" A simple tool to conduct election", font=('Helvetica', 10))
Head2.place(x=150, y=30, height=20)
Head3 = tk.Label(window, text="BY - Atharv", font=('Helvetica', 12))
Head3.place(x=300, y=250, height=20)

btn1 = tk.Button(window, text="    Create 1V1 ELECTION    ")
btn1.place(x=200, y=100, height=30)
btn2 = tk.Button(window, text="    Create STV ELECTION    ")
btn2.place(x=200, y=150, height=30)
btn3 = tk.Button(window, text="        WHAT IS STV?            ", command=switch )
btn3.place(x=200, y=200, height=30)


wis = tk.Toplevel(root)
wis.geometry('500x300')
wis.title('What is STV')
info = tk.Label(wis, text="STV IS A VOTING SYSTEM")
info.pack()
btn4 = tk.Button(wis, text="    Back   " , command=switch )
btn4.place(x=200, y=100, height=30)

wis.withdraw()
root.withdraw()
root.mainloop()