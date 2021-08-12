from tkinter import *
from tkinter import ttk
import draft
import random
# Creates and Initiates class 'App'


class App(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent

        self.winfo_toplevel().title("Periodic Table of the Elements")

        self.create_widgets()

    def create_widgets(self):
        self.elementos = draft.elementos

        self.colores = {'Alcalino': 'red',
                        'Alcalinotérreo': 'yellow',
                        'Lantánido': 'blue',
                        'Actínido': 'green',
                        'De Transición': 'gray',
                        'Metal': 'purple',
                        'Metaloide': 'orange',
                        'No Metal': 'white',
                        'Halógeno': 'pink',
                        'Gas Noble': 'brown',
                        'Metales del bloque p': 'light blue'}

        self.topLabel = Label(self, text="Click the element you would like information about.", font=20)
        self.topLabel.grid(row=0, column=0, columnspan=18)

        for e in self.elementos:
            i = self.elementos[e]

            Button(self, text=i.siglas, width=5, height=2, bg=self.colores[i.tipo],
                   command=lambda n=i.nombre: self.info(n)).grid(row=i.posicion[0], column=i.posicion[1])

        self.fillerLine = Label(self, text="")
        self.fillerLine.grid(row=10, column=0)

        Button(self, text='Reset', width=5, height=2, bg="black", fg="white",
               command=self.comb_reacciones).grid(row=13, column=0)

        Button(self, text='Reacción', width=5, height=2, bg="black", fg="white",
               command=self.comb_reacciones).grid(row=13, column=1)

        Button(self, text='Random', width=5, height=2, bg="black", fg="white",
               command=self.random).grid(row=13, column=2)

        self.infoLine = Label(self, text="", justify='left')
        self.infoLine.grid(row=1, column=3, columnspan=10, rowspan=4)

        self.fillerLine = Label(self, text="")
        self.fillerLine.grid(row=14, column=19, columnspan=1)

        Button(self, text='Óxidos Metálicos', width=20, height=2, command=lambda m=['OM', 0, 20]: self.reaccion(m)).grid(row=0, column=20)
        Button(self, text='Óxidos No Metálicos', width=20, height=2, command=lambda m=['ONM', 1, 20]: self.reaccion(m)).grid(row=1, column=20)
        Button(self, text='Hidruros Metálicos', width=20, height=2, command=lambda m=['HM', 2, 20]: self.reaccion(m)).grid(row=2, column=20)
        Button(self, text='Hidruros No Metálicos', width=20, height=2, command=lambda m=['HNM', 3, 20]: self.reaccion(m)).grid(row=3, column=20)
        Button(self, text='Hidroxilo', width=20, height=2, command=lambda m=['H', 4, 20]: self.reaccion(m)).grid(row=4, column=20)
        Button(self, text='Oxacido', width=20, height=2, command=lambda m=['O', 5, 20]: self.reaccion(m)).grid(row=5, column=20)
        Button(self, text='Sales Neutras', width=20, height=2, command=lambda m=['SN', 6, 20]: self.reaccion(m)).grid(row=6, column=20)
        Button(self, text='Sales Acidas', width=20, height=2, command=lambda m=['SA', 7, 20]: self.reaccion(m)).grid(row=7, column=20)
        Button(self, text='Sales Básicas', width=20, height=2, command=lambda m=['SB', 8, 20]: self.reaccion(m)).grid(row=8, column=20)
        Button(self, text='Sales Mixtas', width=20, height=2, command=lambda m=['SM', 9, 20]: self.reaccion(m)).grid(row=9, column=20)

        self.v1 = StringVar()  # a string variable to hold user selection
        self.v2 = StringVar()  # a string variable to hold user selection
        self.v3 = StringVar()  # a string variable to hold user selection

        self.nombre_reaccion = ''

        self.combobox1 = ttk.Combobox(self, textvariable=self.v1, height=2)
        self.combobox2 = ttk.Combobox(self, textvariable=self.v2, height=2)
        self.combobox3 = ttk.Combobox(self, textvariable=self.v3, height=2)

    # Displays information on the element of whichever element tk.Button was pressed
    def info(self, e):
        elemento = self.elementos[e]

        texto = "Nombre: %s\nTipo: %s\nSigla: %s\nPeso Atómico: %f\nClasificación: %s\nValencia: %s\nOxidación: %s" % \
                (elemento.nombre, elemento.tipo, elemento.siglas, elemento.pesoAtomico, elemento.clasificacion,
                 ','.join(str(x) for x in elemento.valencia), elemento.oxidacion)

        self.topLabel.config(text=elemento.nombre)
        self.infoLine.config(text=texto)

    def reaccion(self, boton):
        self.combobox1['state'] = 'enable'
        self.combobox2['state'] = 'enable'
        self.combobox3['state'] = 'enable'

        self.combobox1.grid_forget()
        self.combobox2.grid_forget()
        self.combobox3.grid_forget()

        self.v1.set('')
        self.v2.set('')
        self.v3.set('')

        self.nombre_reaccion = boton[0]

        if boton[0] == 'OM':
            self.combobox1['values'] = ['Oxígeno']
            self.combobox1.current(0)
            self.combobox1['state'] = 'disable'
            self.combobox1.grid(row=boton[1], column=boton[2]+1)

            self.combobox2['values'] = self.get_elementos_clasificacion('Metal')
            self.combobox2.grid(row=boton[1], column=boton[2] + 2)
            self.combobox3.pack_forget()
        elif boton[0] == 'ONM':
            self.combobox1['values'] = ['Oxígeno']
            self.combobox1.current(0)
            self.combobox1['state'] = 'disable'
            self.combobox1.grid(row=boton[1], column=boton[2] + 1)

            self.combobox2['values'] = self.get_elementos_clasificacion('No Metal')
            self.combobox2.grid(row=boton[1], column=boton[2] + 2)
        elif boton[0] == 'HM':
            self.combobox1['values'] = ['Hidrógeno']
            self.combobox1.current(0)
            self.combobox1['state'] = 'disable'
            self.combobox1.grid(row=boton[1], column=boton[2] + 1)

            self.combobox2['values'] = self.get_elementos_clasificacion('Metal')
            self.combobox2.grid(row=boton[1], column=boton[2] + 2)
        elif boton[0] == 'HNM':
            self.combobox1['values'] = ['Hidrógeno']
            self.combobox1.current(0)
            self.combobox1['state'] = 'disable'
            self.combobox1.grid(row=boton[1], column=boton[2] + 1)

            self.combobox2['values'] = self.get_elementos_clasificacion('No Metal')
            self.combobox2.grid(row=boton[1], column=boton[2] + 2)
        elif boton[0] == 'H':
            self.combobox1['values'] = ['Oxígeno']
            self.combobox1.current(0)
            self.combobox1['state'] = 'disable'
            self.combobox1.grid(row=boton[1], column=boton[2] + 1)

            self.combobox2['values'] = self.get_elementos_clasificacion('Metal')
            self.combobox2.grid(row=boton[1], column=boton[2] + 2)

            self.combobox3['values'] = ['H2O']
            self.combobox3.current(0)
            self.combobox3['state'] = 'disable'
            self.combobox3.grid(row=boton[1], column=boton[2] + 3)
        elif boton[0] == 'O':
            self.combobox1['values'] = self.get_elementos_clasificacion('No Metal')
            self.combobox1.grid(row=boton[1], column=boton[2] + 1)

            self.combobox2['values'] = ['Oxígeno']
            self.combobox2.current(0)
            self.combobox2['state'] = 'disable'
            self.combobox2.grid(row=boton[1], column=boton[2] + 2)

            self.combobox3['values'] = ['Hidrógeno']
            self.combobox3.current(0)
            self.combobox3['state'] = 'disable'
            self.combobox3.grid(row=boton[1], column=boton[2] + 3)

    def get_elementos_clasificacion(self, clasificacion):
        lista_elementos = []

        for x in self.elementos:
            if self.elementos[x].clasificacion == clasificacion:
                lista_elementos.append(x)

        return lista_elementos

    def comb_reacciones(self):
        if self.nombre_reaccion == 'OM':
            print(self.v1.get())
            print(self.v2.get())
        elif self.nombre_reaccion == 'ONM':
            print(self.v1.get())
            print(self.v2.get())
        elif self.nombre_reaccion == 'HM':
            print(self.v1.get())
            print(self.v2.get())
        elif self.nombre_reaccion == 'HNM':
            print(self.v1.get())
            print(self.v2.get())
        elif self.nombre_reaccion == 'H':
            print(self.v1.get())
            print(self.v2.get())
            print(self.v3.get())
        elif self.nombre_reaccion == 'O':
            print(self.v1.get())
            print(self.v2.get())
            print(self.v3.get())

    def random(self):
        reacciones = ['OM', 'ONM', 'HM', 'HNM', 'H', 'O']

        self.nombre_reaccion = random.choice(reacciones)

        print(self.nombre_reaccion)

        if self.nombre_reaccion == 'OM':
            self.v1.set('Oxígeno')
            self.v2.set(random.choice(self.get_elementos_clasificacion('Metal')))
        elif self.nombre_reaccion == 'ONM':
            self.v1.set('Oxígeno')
            self.v2.set(random.choice(self.get_elementos_clasificacion('No Metal')))
        elif self.nombre_reaccion == 'HM':
            self.v1.set('Hidrógeno')
            self.v2.set(random.choice(self.get_elementos_clasificacion('Metal')))
        elif self.nombre_reaccion == 'HNM':
            self.v1.set('Hidrógeno')
            self.v2.set(random.choice(self.get_elementos_clasificacion('No Metal')))
        elif self.nombre_reaccion == 'H':
            self.v1.set('Oxígeno')
            self.v2.set(random.choice(self.get_elementos_clasificacion('Metal')))
            self.v3.set('H2O')
        elif self.nombre_reaccion == 'O':
            self.v1.set(random.choice(self.get_elementos_clasificacion('No Metal')))
            self.v2.set('Oxígeno')
            self.v3.set('Hidrógeno')

        self.comb_reacciones()

        self.combobox1.grid_forget()
        self.combobox2.grid_forget()
        self.combobox3.grid_forget()

        self.v1.set('')
        self.v2.set('')
        self.v3.set('')


# Creates an instance of 'app' class
def main():
    root = Tk()
    a = App(root)
    a.grid(row=0, column=0, sticky='nsew')
    a.mainloop()


# runs main function
if __name__ == "__main__": 
    main()
