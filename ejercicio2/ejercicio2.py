# queue_logic.py

import random
import time

class QueueLogic:
    def __init__(self, update_ui_callback, end_game_callback, root):
        self.queue = []
        self.colors = ["Naranja", "Rojo", "Verde", "Amarillo", "Rosado", "Azul", "Morado", "Turquesa", "Gris"]
        self.update_ui_callback = update_ui_callback
        self.end_game_callback = end_game_callback
        self.painted_count = 0
        self.start_time = time.time()
        self.queuing_interval = 2000  # Empieza en 4 segundos (4000 ms)
        self.root = root  # Referencia a la raíz de Tkinter para usar 'after'
        self.queue_job = None  # Controlar la tarea de 'after'

    def start_game(self):
        self.painted_count = 0
        self.queue = []
        self.start_time = time.time()
        self.queuing_interval = 2000
        self.enqueue_car()

    def enqueue_car(self):
        if len(self.queue) >= 5:
            self.end_game()
            return
        color = random.choice(self.colors)
        self.queue.append(color)
        self.update_ui_callback(self.queue)
        
        # Incrementar la velocidad tras cada coche pintado
        self.queue_job = self.root.after(self.queuing_interval, self.enqueue_car)
        
        # Reducir la velocidad gradualmente (mínimo 1000 ms = 1 segundo)
        if self.painted_count > 0:
            self.queuing_interval = max(600, self.queuing_interval - 200)

    def paint_car(self, color):
        if not self.queue:
            return False
        if self.queue[0] == color:
            self.queue.pop(0)
            self.painted_count += 1
            self.update_ui_callback(self.queue)
            return True
        else:
            self.end_game()
            return False

    def end_game(self):
        if self.queue_job:
            self.root.after_cancel(self.queue_job)  # Cancelar la tarea de 'after' si está activa
        elapsed_time = time.time() - self.start_time
        self.end_game_callback(self.painted_count, elapsed_time)

