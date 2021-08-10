# import required resources
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class main_win(Frame):

    def __init__(self, master):
        self.root = master

        Frame.__init__(self, master)

        self.root.resizable(0, 0)
        self.root.title("Tabla Periodica")


# Desarrollo del interfaz del programa.
root = Tk()  # Creación de la Ventana principal.
app = main_win(root)
app.mainloop()  # Espera a que se cierre la panatalla.
