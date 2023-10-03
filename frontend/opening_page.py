import tkinter as tk
import tkinter.ttk as ttk

class OpeningPageFrame(ttk.Frame):
    def __init__(self, app, context):
        super().__init__(app)

        '''
        main_frame = tk.Frame(self)
        main_frame.pack(fill=tk.BOTH, expand=1)

        # Create Frame for X Scrollbar
        sec = tk.Frame(main_frame)
        sec.pack(fill=tk.X, side=tk.BOTTOM)

        # Create A Canvas
        my_canvas = tk.Canvas(main_frame)
        my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

        # Add A Scrollbars to Canvas
        x_scrollbar = ttk.Scrollbar(sec, orient=tk.HORIZONTAL, command=my_canvas.xview)
        x_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        y_scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=my_canvas.yview)
        y_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Configure the canvas
        my_canvas.configure(xscrollcommand=x_scrollbar.set)
        my_canvas.configure(yscrollcommand=y_scrollbar.set)
        my_canvas.bind("<Configure>", lambda e: my_canvas.config(scrollregion=my_canvas.bbox(tk.ALL)))

        # Create Another Frame INSIDE the Canvas
        second_frame = tk.Frame(my_canvas)

        # Add that New Frame a Window In The Canvas
        my_canvas.create_window((0, 0), window=second_frame, anchor="nw")
        '''

        self.grid_columnconfigure(0, weight=1)
        for i in range(8):
            self.grid_rowconfigure(i, weight=1)

        self.head1 = ttk.Label(self, text="POLL PILOT", font=('Times', 20))
        self.head1.grid(row=0, column=0, padx= 50 )
        self.head2 = ttk.Label(self, text=" A simple tool to conduct elections", font=('Helvetica', 10))
        self.head2.grid(row=1, column=0, padx= 50 )

        self.btn1 = ttk.Button(self, text="Create An Election", command=app.show_frame_factory('cre_elec'))
        self.btn1.grid(row=2, column=0, padx= 50 , pady= 10)
        self.btn2 = ttk.Button(self, text="Create A Referendum", command=app.show_frame_factory('create_ref'))
        self.btn2.grid(row=3, column=0, padx= 50 , pady= 10)
        self.btn2 = ttk.Button(self, text="Show Elections", command=app.show_frame_factory('elec_navigation'))
        self.btn2.grid(row=4, column=0, padx= 50 , pady= 10)
        self.btn3 = ttk.Button(self, text="Help", command=app.show_frame_factory('help'))
        self.btn3.grid(row=5, column=0, padx= 50 , pady= 10)
        self.btn4 = ttk.Button(self, text="Credits", command=app.show_frame_factory('credits'))
        self.btn4.grid(row=6, column=0, padx= 50 , pady= 10)

        #self.btn5 = ttk.Button(self, text="TESTS", command=app.show_frame_factory('result_page'))
        #self.btn5.grid(row=7, column=0, padx= 50 , pady= 10)