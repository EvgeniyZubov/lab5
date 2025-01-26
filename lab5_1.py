import tkinter

class Window1(tkinter.Frame):
    def __init__(self, parent):


        super().__init__(parent)
        self.parent = parent
        self.pack(fill=tkinter.BOTH, expand=1)
        self.config(bg="#A43820")
        self.create_widgets()
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

    def create_widgets(self):

        self.lb1 = tkinter.Label(self, text = "Введіть число A", bg="#A43820", fg = "white")
        self.a_entr = tkinter.Entry(self)
        self.btn1 = tkinter.Button(self, text = "Возвести у степінь", command = self.PowerA234)
        self.square_str = tkinter.StringVar()
        self.third_str = tkinter.StringVar()
        self.fourth_str = tkinter.StringVar()
        self.lb2 = tkinter.Label(self, textvariable = self.square_str, bg="#A43820", fg = "white")
        self.lb3 = tkinter.Label(self, textvariable = self.third_str, bg="#A43820", fg = "white")
        self.lb4 = tkinter.Label(self, textvariable = self.fourth_str, bg="#A43820", fg = "white")


        self.lb1.grid(row=0, column=0, sticky=tkinter.NSEW)
        self.a_entr.grid(row=0, column=1, sticky=tkinter.NSEW)
        self.btn1.grid(row=1, column=0, sticky=tkinter.NSEW)
        self.lb2.grid(row=2, column=0, sticky=tkinter.NSEW)
        self.lb3.grid(row=3, column=0, sticky=tkinter.NSEW)
        self.lb4.grid(row=4, column=0, sticky=tkinter.NSEW)



    def PowerA234(self):
        a = float(self.a_entr.get())

        self.square_str.set(a**2)
        self.third_str.set(a**3)
        self.fourth_str.set(a**4)





