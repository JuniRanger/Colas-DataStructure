import tkinter as tk
from tkinter import ttk
from ejercicio2.ejercicio2 import ColaCoches

class Interface2:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego Pintar Coches")
        self.root.geometry("600x400")
        
        self.colaCoches = ColaCoches()

        # Botón para encolar y pintar coche
        tk.Button(self.root, text="Encolar Coche", command=self.encolar_coche).pack()
        tk.Button(self.root, text="Pintar Primer Coche", command=self.pintar_coche).pack()

        # Tabla para mostrar coches en cola
        self.tree = ttk.Treeview(self.root, columns=("Color"), show='headings')
        self.tree.pack()
        self.tree.heading("Color", text="Color")

    def encolar_coche(self):
        self.colaCoches.encolar_coche()
        self.actualizar_tabla()

    def pintar_coche(self):
        self.colaCoches.atender_coche()
        self.actualizar_tabla()

    def actualizar_tabla(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for color in self.colaCoches.obtener_coches():
            self.tree.insert("", "end", values=(color,))
