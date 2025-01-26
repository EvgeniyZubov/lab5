import tkinter
from tkinter import messagebox

from pylab import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Window2(tkinter.Frame):
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
        self.grid_rowconfigure(5, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(4, weight=1)

    def create_widgets(self):

        self.lb1 = tkinter.Label(self, text = "Введіть число N", bg="#A43820", fg = "white")
        self.lb2 = tkinter.Label(self, text="Введіть число K", bg="#A43820", fg="white")
        self.lb3 = tkinter.Label(self, text="Введіть число ξ", bg="#A43820", fg="white")
        self.lb4 = tkinter.Label(self, text="Введіть число U", bg="#A43820", fg="white")
        self.lb5 = tkinter.Label(self, text="Введіть число T", bg="#A43820", fg="white")

        self.N_entr = tkinter.Entry(self)
        self.K_entr = tkinter.Entry(self)
        self.Xi_entr = tkinter.Entry(self)
        self.U_entr = tkinter.Entry(self)
        self.T_entr = tkinter.Entry(self)

        self.create_btn = tkinter.Button(self, text="Создать файл", command=self.create_file,background="#A43820", fg = "white")


        self.lb1.grid(row=0, column=0)
        self.lb2.grid(row=0, column=1)
        self.lb3.grid(row=0, column=2)
        self.lb4.grid(row=0, column=3)
        self.lb5.grid(row=0, column=4)
        self.N_entr.grid(row=1, column=0)
        self.K_entr.grid(row=1, column=1)
        self.Xi_entr.grid(row=1, column=2)
        self.U_entr.grid(row=1, column=3)
        self.T_entr.grid(row=1, column=4)
        self.create_btn.grid(row=2, column=0)





    def create_file(self):
        try:
            self.N = int(self.N_entr.get())
            if self.N < 20:
                raise ValueError
        except ValueError:
            messagebox.showerror("Ошибка", "N >= 20!")
        else:
            try:
                self.K = float(self.K_entr.get())
            except ValueError:
                messagebox.showerror("Ошибка", "K(!=0)")
            else:
                try:
                    self.Xi = float(self.Xi_entr.get())
                except ValueError:
                    messagebox.showerror("Ошибка", "ξ(!=0)")
                else:
                    try:
                        self.U = float(self.U_entr.get())
                    except ValueError:
                        messagebox.showerror("Ошибка", " U(!=0)")
                    else:
                        try:
                            self.T = float(self.T_entr.get())
                        except ValueError:
                            messagebox.showerror("Ошибка", "T(!=0)")
                        else:
                            x, y = self.solve(self.N, self.K, self.Xi, self.U, self.T)
                            self.data_save(x, y, "graph_data.txt")
                            self.plot_data(x, y)

    def solve(self, N, K, Xi, U, T):
        T0 = 2 * T / N
        x = np.linspace(0, N * T0, N)
        y = np.zeros(N)

        for k in range(2, N-2):
            y[k+2] =  (2 - ((2*Xi * T0) / T)) * y[k - 1] + (((2 * Xi * T0) / T) - 1 - (T0 ** 2 / T ** 2)) * y[k] + (
                        (K * (T0 ** 2)) / T ** 2) * U
        return x, y

    def plot_data(self, x, y):
        self.figure = plt.Figure(figsize=(5, 4), dpi=100)
        self.ax = self.figure.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.parent)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack(side=tkinter.RIGHT, fill=tkinter.BOTH, expand=True)
        self.canvas.get_tk_widget().place(x=500, y=300)

        self.ax.clear()
        self.ax.plot(x, y)
        self.ax.set_title("Завдання №14")
        self.ax.set_xlabel('Час')
        self.ax.set_ylabel('Значення функции')
        self.ax.grid(True)
        self.ax.legend()
        self.canvas.draw()

    def data_save(self, x, y, filename):
        with open(filename, "w") as f:
            for x_vals, y_vals in zip(x, y):
                f.write(f"Крок: {x_vals} | Значення Y: {y_vals}\n")
