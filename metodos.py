from tkinter import ttk
import tkinter as tk


class metodo:

    def __init_(self):
        pass

    def esc(nombree, pesoo, siglaa, tipoo, clasif, valenciaa, Nom, pes, sig, tip, cla, val, ventana, obj):
        nombree = obj.nombre
        pesoo = obj.pesoAtomico
        siglaa = obj.siglas
        tipoo = obj.tipo
        clasif = obj.clasificacion
        valenciaa = str(obj.valencia)

        # Limpiar etiqueta
        Nom = ttk.Label(ventana, text="________________").grid(column=0, row=0)
        pes = ttk.Label(ventana, text="________________").grid(column=0, row=1)
        sig = ttk.Label(ventana, text="________________").grid(column=0, row=2)
        tip = ttk.Label(ventana, text="________________").grid(column=0, row=3)
        cla = ttk.Label(ventana, text="________________").grid(column=0, row=4)
        val = ttk.Label(ventana, text="________________").grid(column=0, row=5)

        # Reescribir
        Nom = ttk.Label(ventana, text=nombree).grid(column=0, row=0)
        pes = ttk.Label(ventana, text=pesoo).grid(column=0, row=1)
        sig = ttk.Label(ventana, text=siglaa).grid(column=0, row=2)
        tip = ttk.Label(ventana, text=tipoo).grid(column=0, row=3)
        cla = ttk.Label(ventana, text=clasif).grid(column=0, row=4)
        val = ttk.Label(ventana, text=valenciaa).grid(column=0, row=5)
