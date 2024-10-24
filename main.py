import tkinter as tk
from tkinter import ttk

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ejercicio colas en python")
        self.root.geometry("620x420")
        self.root.config(background="#292b2c")

        # Configuración de label
        self.label = tk.Label(self.root, text="Practica Colas en Python")
        self.label.pack(padx=10, pady=10)
        self.label.config(font=("Helvetica", 30), background="#292b2c", fg="#ffcc00")

        # Configuración de botones
        self.CrearBoton("Ventanilla de banco", self.AbrirEjercicio1).pack(pady=10, padx=20)
        self.CrearBoton("Pintar coches", self.AbrirEjercicio2).pack(pady=10, padx=20)
        self.CrearBoton("Estacionar autos", self.AbrirEjercicio3).pack(pady=10, padx=20)

    def CrearBoton(self, text, command):
        return tk.Button(
            self.root, 
            text=text, 
            font=("Helvetica", 16),  # Aumentar tamaño de fuente
            width=20,                # Ancho del botón
            height=3,                # Altura del botón
            bg="#ffcc00",            # Color de fondo
            fg="black",              # Color del texto
            command=command          # Llama a la función correspondiente
        )

    # Métodos para cada ejercicio
    def AbrirEjercicio1(self):
        self.AbrirVentana("Ejercicio 1", "Este es el Ejercicio 1")

    def AbrirEjercicio2(self):
        self.AbrirVentana("Ejercicio 2", "Este es el Ejercicio 2")

    def AbrirEjercicio3(self):
        self.AbrirVentana("Ejercicio 3", "Este es el Ejercicio 3")

    # Función para abrir una nueva ventana con el texto del ejercicio
    def AbrirVentana(self, titulo, texto):
        nueva_ventana = tk.Toplevel(self.root)
        nueva_ventana.title(titulo)
        label = ttk.Label(nueva_ventana, text=texto)
        label.pack(padx=20, pady=20)

# Crear la ventana principal
if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
