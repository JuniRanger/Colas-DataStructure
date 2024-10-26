import tkinter as tk
from tkinter import messagebox
import time  # Asegúrate de importar time para el manejo de tiempo
from ejercicio2.ejercicio2 import QueueLogic

class Interface2:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego de Pintado de Autos")
        self.root.geometry("1200x600")

        # Configuración de la interfaz
        self.color_buttons_frame = tk.Frame(self.root)
        self.color_buttons_frame.pack(pady=10)

        self.queue_frame = tk.Frame(self.root)
        self.queue_frame.pack(pady=20)

        self.stats_label = tk.Label(self.root, text="Pintados: 0")
        self.stats_label.pack()

        # Conectar la lógica del juego con los métodos de la interfaz
        self.queue_logic = QueueLogic(self.update_ui, self.end_game, self.root)

        self.game_over = False

        # Colores en formato hexadecimal para evitar errores en tkinter
        self.colors = {
            "Naranja": "#FFA500",
            "Rojo": "#FF0000",
            "Verde": "#00FF00",
            "Amarillo": "#FFFF00",
            "Rosado": "#FFC0CB",
            "Azul": "#0000FF",
            "Morado": "#800080",
            "Turquesa": "#40E0D0",
            "Gris": "#808080"
        }
        self.create_color_buttons()

        # Botón para iniciar el juego
        self.start_button = tk.Button(self.root, text="Iniciar Juego", command=self.start_game, font=("Arial", 14), width=20, height=2)
        self.start_button.pack(pady=10)

    def create_color_buttons(self):
        """Crea botones para cada color en la parte superior."""
        for color_name, hex_code in self.colors.items():
            btn = tk.Button(
                self.color_buttons_frame, text=color_name, bg=hex_code,
                command=lambda c=color_name: self.paint_car(c),
                font=("Arial", 12, "bold"), width=10, height=2
            )
            btn.pack(side="left", padx=5)

    def start_game(self):
        """Inicia el juego."""
        self.painted_count = 0
        self.queue_logic.start_game()
        self.start_button.config(state="disabled")
        self.game_over = False  # Reiniciar el estado del juego al inicio

    def update_ui(self, queue):
        """Actualiza la interfaz de usuario cuando cambia la cola de autos."""
        if not self.root.winfo_exists():
            return  # Salir si la ventana no está activa

        # Actualiza la interfaz eliminando y redibujando los widgets de la cola
        for widget in self.queue_frame.winfo_children():
            widget.destroy()

        # Muestra los autos en la cola actual con un estilo más atractivo
        for car in queue:
            hex_color = self.colors.get(car, "#FFFFFF")
            car_label = tk.Label(self.queue_frame, text="🚗", bg=hex_color, font=("Arial", 20, "bold"), width=10, height=2)
            car_label.pack(side="left", padx=5)

        # Actualiza el número de autos pintados
        self.stats_label.config(text=f"Pintados: {self.queue_logic.painted_count}")

    def paint_car(self, color):
        """Intenta pintar el auto al frente de la cola."""
        if self.game_over:
            return

        success = self.queue_logic.paint_car(color)
        if not success:
            self.game_over = True

    def end_game(self, painted_count, elapsed_time):
        """Finaliza el juego y muestra el puntaje."""
        self.game_over = True
        messagebox.showinfo("Fin del Juego", f"Autos pintados: {painted_count}\nTiempo total: {int(elapsed_time)} segundos")
        self.start_button.config(state="normal")
