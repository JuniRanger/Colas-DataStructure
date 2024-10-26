import tkinter as tk
from tkinter import ttk
from ejercicio1.window import Interface1  # Importar ventana del ejercicio 1
from ejercicio2.window import Interface2  # Importar ventana del ejercicio 2
from ejercicio3.window import Interface3  # Importar ventana del ejercicio 3

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ejercicio colas en Python")
        self.root.geometry("620x420")
        self.root.config(background="#292b2c")

        # Configuración de label principal
        self.label = tk.Label(self.root, text="Practica Colas en Python")
        self.label.pack(padx=10, pady=10)
        self.label.config(font=("Helvetica", 30), background="#292b2c", fg="#87CEEB")

        # Configuración de botones
        self.CrearBoton("Ventanilla de banco", self.AbrirEjercicio1).pack(pady=10, padx=20)
        self.CrearBoton("Pintar coches", self.AbrirEjercicio2).pack(pady=10, padx=20)
        self.CrearBoton("Estacionar autos", self.AbrirEjercicio3).pack(pady=10, padx=20)

    def CrearBoton(self, text, command):
        return tk.Button(
            self.root, 
            text=text, 
            font=("Helvetica", 16),
            width=20,
            height=3,
            bg="#87CEEB",
            fg="black",
            command=command
        )

    # Métodos para abrir las interfaces de cada ejercicio
    def AbrirEjercicio1(self):
        new_window = tk.Toplevel(self.root)
        Interface1(new_window)

    def AbrirEjercicio2(self):
        new_window = tk.Toplevel(self.root)
        Interface2(new_window)

    def AbrirEjercicio3(self):
        new_window = tk.Toplevel(self.root)
        Interface3(new_window)

# Crear la ventana principal
if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = MainApp(root)
        root.mainloop()
    except Exception as e:
        print(f"Ocurrió un error en la aplicación: {e}")
