from collections import deque
from datetime import datetime

class Cola:
    def __init__(self):
        self.cola = deque()
        
    def AgregarCliente(self, turno, cliente, movimiento):
        horaLlegada = datetime.now().strftime("%H:%M:%S")
        self.cola.append((turno, cliente, movimiento, horaLlegada))
        
    def AtenderClinte(self):
        if self.cola:
            return self.cola.popleft() # Elimina y retorna el primer cliente de la cola
        return None
    
    def ObtenerClientes(self):
        return list(self.cola)
    
    def ObtenerPrimerTurno(self):
        if self.cola:
            return self.cola[0][0]  # Retorna el número del primer turno
        return None

    def ObtenerUltimoTurno(self):
        if self.cola:
            return self.cola[-1][0]  # Retorna el número del último turno
        return None

