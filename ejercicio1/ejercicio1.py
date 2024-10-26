from collections import deque
from datetime import datetime

class Cola:
    def __init__(self, max_size=10):  # Definir el tamaño máximo de la cola para control de sobreflujo
        self.cola = deque()
        self.max_size = max_size

    def AgregarCliente(self, turno, cliente, movimiento):
        try:
            if self.ColaLlena():
                print("La cola está llena, no se puede agregar más clientes.")
                return False
            horaLlegada = datetime.now()
            self.cola.append((turno, cliente, movimiento, horaLlegada))
            return True
        except Exception as e:
            print(f"Error al agregar cliente: {e}")
            return False

    def AtenderCliente(self):
        try:
            if not self.ColaVacia():
                cliente = self.cola.popleft()
                hora_llegada = cliente[3]
                tiempo_espera = (datetime.now() - hora_llegada).total_seconds()
                return cliente, tiempo_espera
            print("La cola está vacía, no hay clientes para atender.")
            return None, None
        except Exception as e:
            print(f"Error al atender cliente: {e}")
            return None, None

    def ObtenerClientes(self):
        return [(turno, cliente, movimiento, hora_llegada.strftime("%H:%M:%S")) for turno, cliente, movimiento, hora_llegada in self.cola]

    def ColaLlena(self):
        return len(self.cola) >= self.max_size

    def ColaVacia(self):
        return len(self.cola) == 0

    def ObtenerPrimerTurno(self):
        if not self.ColaVacia():
            return self.cola[0][0]  # Número del primer turno
        return None

    def ObtenerUltimoTurno(self):
        if not self.ColaVacia():
            return self.cola[-1][0]  # Número del último turno
        return None
