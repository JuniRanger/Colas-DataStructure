import random
import time
from threading import Timer

class QueueLogic:
    def __init__(self, update_ui_callback, end_game_callback):
        self.queue = []
        self.colors =["Rojo", "Naranja", "Verde", "Amarillo", "Rosado", "Azul", "Morado", "Turquesa", "Gris"]
        self.update_ui_callback = update_ui_callback
        self.end_game_callback = end_game_callback
        self.painted_count = 0
        self.start_time = time.time()
        self.queueing_interval = 10
        self.queue_timer = None
        
    def StartGame(self):
        self.painted_count = 0
        self.queue = []
        self.start_game = time.time()
        self.queueing_interval = 10
        self.EnqueueCar()
        
    def EnqueueCar(self):
        if len(self.queue) >= 5:
            self.EndGame()
            return
        color = random.choice(self.colors)
        self.queue.append(color)
        self.update_ui_callback(self.queue)
        
        #Iniciar el temporizador para el siguiente coche
        self.queue_timer = Timer(self.queueing_interval, self.EnqueueCar)
        self.queue_timer.start()
        
        #Aumentar la velocidad despues de cada 3 autos pintados
        if self.painted_count % 3 == 0 and self.painted_count > 0:
            self.queueing_interval = max(5, self.queueing_interval - 5)
            
    def PaintCar(self):
        if not self.queue:
            return False
        #pintar solo si el colo coincide con el primer auto de la cola
        if self.queue[0] == color:
            self.queue.pop(0)
            self.painted_count += 1
            self.update_ui_callback(self.queue)
            return True
        return False
    
    def EndGame(self):
        if self.queue_timer:
            self.queue_timer.cancel()


