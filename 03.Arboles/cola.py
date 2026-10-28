
class Cola:
    def __init__(self, n):
        self.arr = [None] * n
        self.capacidad = n
        self.frente = 0
        self.final = 0
        self.cantidad = 0

    def esta_vacia(self):
        return self.cantidad == 0

    def esta_llena(self):
        return self.cantidad == self.capacidad

    def enqueue(self, x):
        if self.esta_llena():
            raise OverflowError("Cola llena")

        self.arr[self.final] = x
        self.final = (self.final + 1) % self.capacidad
        self.cantidad += 1

    def dequeue(self):
        if self.esta_vacia():
            raise IndexError("Cola vacía")

        res = self.arr[self.frente]
        self.arr[self.frente] = None
        self.frente = (self.frente + 1) % self.capacidad
        self.cantidad -= 1

        return res
