import random
from collections import deque

class ColaCoches:
    def __init__(self):
        self.cola = deque()
        self.colores = ["Rojo", "Azul", "Verde", "Amarillo", "Negro"]

    def encolar_coche(self):
        color = random.choice(self.colores)
        self.cola.append(color)
    
    def atender_coche(self):
        if self.cola:
            return self.cola.popleft()
        return None

    def obtener_coches(self):
        return list(self.cola)
