import tkinter as tk
from tkinter import ttk, messagebox
from ejercicio1.ejercicio1 import Cola

class Interface1:
    def __init__(self, root):
        self.root = root
        self.root.title("Colas - Ventanilla de banco")
        self.root.geometry("900x600")
        
        self.cola = Cola(max_size=5)  # Inicializar la cola con un tamaño máximo

        # Frame y widgets de entrada
        cliente_frame = tk.LabelFrame(self.root, text="Datos del Cliente", padx=10, pady=10)
        cliente_frame.grid(row=0, column=0, padx=20, pady=20, columnspan=2, sticky="ew")

        tk.Label(cliente_frame, text="No. Turno:").grid(row=0, column=0)
        self.entry_turno = tk.Entry(cliente_frame)
        self.entry_turno.grid(row=0, column=1)

        tk.Label(cliente_frame, text="Cliente:").grid(row=1, column=0)
        self.entry_cliente = tk.Entry(cliente_frame)
        self.entry_cliente.grid(row=1, column=1)

        tk.Label(cliente_frame, text="Movimiento:").grid(row=2, column=0)
        self.movimiento = ttk.Combobox(cliente_frame, values=["Pago de servicio", "Depósito", "Retiro", "Consulta"])
        self.movimiento.grid(row=2, column=1)
        self.movimiento.current(0)

        # Botones
        tk.Button(self.root, text="Agregar a la Cola", command=self.agregar_cola).grid(row=1, column=0, pady=10)
        tk.Button(self.root, text="Atender en Ventanilla", command=self.atender_ventanilla).grid(row=1, column=1, pady=10)

        # Tabla para mostrar los clientes
        self.tree = ttk.Treeview(self.root, columns=("No. Turno", "Cliente", "Movimiento", "Hora Llegada"), show='headings')
        self.tree.grid(row=2, column=0, columnspan=2)
        for col in ("No. Turno", "Cliente", "Movimiento", "Hora Llegada"):
            self.tree.heading(col, text=col)

        # Mostrar el primer y último turno en etiquetas
        self.label_primer_turno = tk.Label(self.root, text="Primer Turno: N/A")
        self.label_primer_turno.grid(row=3, column=0, pady=10, sticky="w")

        self.label_ultimo_turno = tk.Label(self.root, text="Último Turno: N/A")
        self.label_ultimo_turno.grid(row=3, column=1, pady=10, sticky="e")

    def agregar_cola(self):
        try:
            turno = self.entry_turno.get()
            cliente = self.entry_cliente.get()
            movimiento = self.movimiento.get()

            if not turno or not cliente:
                messagebox.showwarning("Datos incompletos", "Por favor, complete todos los campos.")
                return

            if self.cola.AgregarCliente(turno, cliente, movimiento):
                self.actualizar_tabla()
                self.actualizar_turnos()
            else:
                messagebox.showwarning("Cola llena", "No se puede agregar más clientes, la cola está llena.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al agregar a la cola: {e}")

    def atender_ventanilla(self):
        try:
            cliente, tiempo_espera = self.cola.AtenderCliente()
            if cliente:
                messagebox.showinfo(
                    "Cliente atendido",
                    f"Cliente {cliente[1]} atendido.\nTiempo de espera: {tiempo_espera:.2f} segundos",
                    parent=self.root
                )
                self.actualizar_tabla()
                self.actualizar_turnos()
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al atender al cliente: {e}")

    def actualizar_tabla(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for cliente in self.cola.ObtenerClientes():
            self.tree.insert("", "end", values=cliente)

    def actualizar_turnos(self):
        primer_turno = self.cola.ObtenerPrimerTurno()
        ultimo_turno = self.cola.ObtenerUltimoTurno()

        if primer_turno:
            self.label_primer_turno.config(text=f"Primer Turno: {primer_turno}")
        else:
            self.label_primer_turno.config(text="Primer Turno: N/A")

        if ultimo_turno:
            self.label_ultimo_turno.config(text=f"Último Turno: {ultimo_turno}")
        else:
            self.label_ultimo_turno.config(text="Último Turno: N/A")
