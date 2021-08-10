from elementos import elemento
from metodos import metodo
from tkinter import ttk
import tkinter as tk
from propiedades import propiedad


class elem:

    def __init__(self):
        self.con = 0
        self.con2 = 0
        self.listaa = []

    # Ventana
    global ventana
    ventana = tk.Tk()
    ventana.geometry("400x300")

    # Clase metodos
    global metod
    metod = metodo()
    # Variables
    global nombree
    nombree = ""
    global pesoo
    pesoo = ""
    global siglaa
    siglaa = ""
    global tipoo
    tipoo = ""
    global clasif
    clasif = ""
    global valenciaa
    valenciaa = ""

    # Metodos
    def esc():
        litio = propiedad()
        metod.esc(pesoo, siglaa, tipoo, clasif, valenciaa, Nom, pes, sig, tip, cla, val, ventana, litio.lit())

    def m2():
        boro = propiedad()
        metod.esc(pesoo, siglaa, tipoo, clasif, valenciaa, Nom, pes, sig, tip, cla, val, ventana, boro.bor())

    def m3():
        sodio = propiedad()
        metod.esc(pesoo, siglaa, tipoo, clasif, valenciaa, Nom, pes, sig, tip, cla, val, ventana, sodio.sod())

    def m4():
        hidrogeno = propiedad()
        metod.esc(pesoo, siglaa, tipoo, clasif, valenciaa, Nom, pes, sig, tip, cla, val, ventana, hidrogeno.hid())

    # Etiquetas
    global Nom
    Nom = ttk.Label(ventana, text="________________").grid(column=0, row=0)
    global pes
    pes = ttk.Label(ventana, text="________________").grid(column=0, row=1)
    global sig
    sig = ttk.Label(ventana, text="________________").grid(column=0, row=2)
    global tip
    tip = ttk.Label(ventana, text="________________").grid(column=0, row=3)
    global cla
    cla = ttk.Label(ventana, text="________________").grid(column=0, row=4)
    global val
    val = ttk.Label(ventana, text="________________").grid(column=0, row=5)

    # Botones
    Litio = ttk.Button(ventana, text="Litio", command=esc).grid(column=1, row=0)
    Boro = ttk.Button(ventana, text="Boro", command=m2).grid(column=2, row=0)
    sodio = ttk.Button(ventana, text="Sodio", command=m3).grid(column=3, row=0)
    hidrogeno = ttk.Button(ventana, text="Hidrogeno", command=m4).grid(column=4, row=0)

    ventana.mainloop()
