import tkinter as tk
from tkinter import ttk, messagebox
from ejercicio3.ejercicio3 import ColaCircularDoblementeLigada

class Interface3:
    def __init__(self, root):
        self.root = root
        self.root.title("Estacionamiento para Autos")
        self.root.geometry("600x400")
        
        self.estacionamiento = ColaCircularDoblementeLigada()

        # Widgets de entrada
        tk.Label(self.root, text="Placas:").pack()
        self.entry_placas = tk.Entry(self.root)
        self.entry_placas.pack()

        tk.Label(self.root, text="Propietario:").pack()
        self.entry_propietario = tk.Entry(self.root)
        self.entry_propietario.pack()

        # Botones para entrada y salida de autos
        tk.Button(self.root, text="Entrada de Auto", command=self.entrada_auto).pack(pady=10)
        tk.Button(self.root, text="Salida de Auto", command=self.salida_auto).pack(pady=10)

        # Tabla para mostrar autos en estacionamiento
        self.tree = ttk.Treeview(self.root, columns=("Placas", "Propietario", "Hora Entrada"), show='headings')
        self.tree.pack(pady=20)
        for col in ("Placas", "Propietario", "Hora Entrada"):
            self.tree.heading(col, text=col)

    def entrada_auto(self):
        placas = self.entry_placas.get()
        propietario = self.entry_propietario.get()

        if not placas or not propietario:
            messagebox.showwarning("Datos incompletos", "Por favor, ingrese placas y nombre del propietario.", parent=self.root)
            return

        self.estacionamiento.entrada_auto(placas, propietario)
        messagebox.showinfo("Entrada Confirmada", f"Auto con placas {placas} ingresado al estacionamiento.", parent=self.root)
        self.actualizar_tabla()
        self.root.lift()  # Traer la ventana del ejercicio al frente

    def salida_auto(self):
        if self.estacionamiento.estacionamiento_vacio():
            messagebox.showwarning(
                "Estacionamiento vacío",
                "No hay autos en el estacionamiento.",
                parent=self.root
            )
            self.root.lift()  # Mantener la ventana de ejercicio al frente
            return

        salida = self.estacionamiento.salida_auto()
        if salida:
            placas, propietario, hora_entrada, hora_salida, costo = salida
            messagebox.showinfo(
                "Salida de Auto",
                f"Placas: {placas}\nPropietario: {propietario}\nHora de entrada: {hora_entrada.strftime('%H:%M:%S')}\n"
                f"Hora de salida: {hora_salida.strftime('%H:%M:%S')}\nCosto: ${costo:.2f}",
                parent=self.root
            )
            self.root.lift()  # Mantener la ventana de ejercicio al frente
        self.actualizar_tabla()

    def actualizar_tabla(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for auto in self.estacionamiento.obtener_autos():
            self.tree.insert("", "end", values=(auto[0], auto[1], auto[2].strftime("%H:%M:%S")))
