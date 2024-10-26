from collections import deque
from datetime import datetime

class ColaCircularDoblementeLigada:
    def __init__(self):
        self.cola = deque()
        
    def entrada_auto(self, placas, propietario):
        try:
            hora_entrada = datetime.now()
            self.cola.append((placas, propietario, hora_entrada))
        except Exception as e:
            print(f"Error al ingresar auto: {e}")

    def salida_auto(self):
        try:
            if self.cola:
                placas, propietario, hora_entrada = self.cola.popleft()
                hora_salida = datetime.now()
                costo = (hora_salida - hora_entrada).seconds * 2
                return placas, propietario, hora_entrada, hora_salida, costo
            return None
        except Exception as e:
            print(f"Error al salir auto: {e}")
            return None

    def obtener_autos(self):
        return list(self.cola)

    def estacionamiento_vacio(self):
        return len(self.cola) == 0
