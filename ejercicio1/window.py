import tkinter as tk
from tkinter import ttk

from ejercicio1.ejercicio1 import Cola
class Interface1:
    def __init__(self, root):
        self.root = root
        self.root.title("Colas - Ventanilla de banco")
        self.root.geometry("900x600")
        self.root.config(background="#f0f0f0")

        self.cola = Cola()  # Instancia de la clase Cola

        # Frame para los datos del cliente
        cliente_frame = tk.LabelFrame(self.root, text="Datos del Cliente", padx=10, pady=10)
        cliente_frame.grid(row=0, column=0, padx=20, pady=20, columnspan=2, sticky="ew")

        # Widgets dentro del frame
        tk.Label(cliente_frame, text="No. Turno:", font=("Helvetica", 12)).grid(row=0, column=0, sticky="w")
        self.entry_turno = tk.Entry(cliente_frame, font=("Helvetica", 12), width=10)
        self.entry_turno.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(cliente_frame, text="Cliente:", font=("Helvetica", 12)).grid(row=1, column=0, sticky="w")
        self.entry_cliente = tk.Entry(cliente_frame, font=("Helvetica", 12), width=30)
        self.entry_cliente.grid(row=1, column=1, padx=10, pady=5)

        # Dropdown para el tipo de movimiento
        tk.Label(cliente_frame, text="Movimiento:", font=("Helvetica", 12)).grid(row=2, column=0, sticky="w")
        self.movimiento = ttk.Combobox(cliente_frame, font=("Helvetica", 12), 
        values=["Pago de servicio", "Depósito", "Retiro", "Compra de tiempo-aire", "Consulta de saldo"],
        state='readonly'
        )  
        self.movimiento.grid(row=2, column=1, padx=10, pady=5)
        self.movimiento.current(0)  # Seleccionar el primer valor por defecto

        # Etiquetas para mostrar el primer y último turno, inicializamos en "N/A"
        self.label_primer_turno = tk.Label(cliente_frame, text="Primer Turno: N/A", font=("Helvetica", 12))
        self.label_primer_turno.grid(row=3, column=0, sticky="w", pady=5)

        self.label_ultimo_turno = tk.Label(cliente_frame, text="Último Turno: N/A", font=("Helvetica", 12))
        self.label_ultimo_turno.grid(row=3, column=1, sticky="w", pady=5)
        # Botones de acción
        btnAgregarCola = tk.Button(self.root, text="Agregar a la Cola", font=("Helvetica", 12), width=20, bg="#87CEEB", command=self.agregar_cola)
        btnAgregarCola.grid(row=1, column=0, padx=10, pady=10)

        btnAtenderVentanilla = tk.Button(self.root, text="Atender en Ventanilla", font=("Helvetica", 12), width=20, bg="#87CEEB", command=self.atender_ventanilla)
        btnAtenderVentanilla.grid(row=1, column=1, padx=10, pady=10)

        btnSalir = tk.Button(self.root, text="Salida del sistema", font=("Helvetica", 12), width=20, bg="#ff6961", command=self.root.quit)
        btnSalir.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        # Tabla para mostrar datos
        self.tree = ttk.Treeview(self.root, columns=("No. Turno", "Cliente", "Tipo Movimiento", "Hora Llegada"), show='headings', height=5)
        self.tree.grid(row=3, column=0, columnspan=2, padx=20, pady=20)

        # Configurar encabezados de la tabla
        self.tree.heading("No. Turno", text="No. Turno")
        self.tree.heading("Cliente", text="Cliente")
        self.tree.heading("Tipo Movimiento", text="Tipo Movimiento")
        self.tree.heading("Hora Llegada", text="Hora Llegada")

        # Agregar una barra de desplazamiento a la tabla
        scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=self.tree.yview)
        scrollbar.grid(row=3, column=2, sticky="ns")
        self.tree.configure(yscroll=scrollbar.set)
        
    # Función para agregar datos a la cola y mostrar en la tabla
    def agregar_cola(self):
        turno = self.entry_turno.get()
        cliente = self.entry_cliente.get()
        movimiento = self.movimiento.get()
        self.cola.AgregarCliente(turno, cliente, movimiento)
        
        # Actualizar la tabla
        self.actualizar_tabla()

    # Función para atender en ventanilla y actualizar la tabla
    def atender_ventanilla(self):
        cliente_atendido = self.cola.AtenderCliente()
        if cliente_atendido:
            self.actualizar_tabla()
        else:
            print("No hay clientes en la cola.")

    # Función para actualizar la tabla con los clientes actuales en la cola
    def actualizar_tabla(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for cliente in self.cola.ObtenerClientes():
            self.tree.insert("", "end", values=cliente)
            
        # Función para actualizar los turnos mostrados
    def actualizar_turnos(self):
        primer_turno = self.cola.ObtenerPrimerTurno()
        ultimo_turno = self.cola.ObtenerUltimoTurno()

        # Mostrar el primer turno
        if primer_turno:
            self.label_primer_turno.config(text=f"Primer Turno: {primer_turno[0]} - {primer_turno[1]}")
        else:
            self.label_primer_turno.config(text="Primer Turno: Ninguno")

        # Mostrar el último turno
        if ultimo_turno:
            self.label_ultimo_turno.config(text=f"Último Turno: {ultimo_turno[0]} - {ultimo_turno[1]}")
        else:
            self.label_ultimo_turno.config(text="Último Turno: Ninguno")