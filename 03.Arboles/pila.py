##representacion de pila sobre arreglo
class Pila:
    def __init__(self, n):
        self.arr = [None] * n
        self.tos = -1

    def esta_vacia(self):
        return self.tos < 0

    def esta_llena(self):
        return self.tos == len(self.arr) - 1

    def push(self, x):
        if self.esta_llena():
            raise OverflowError("Pila llena")

        self.tos += 1
        self.arr[self.tos] = x

    def pop(self):
        if self.esta_vacia():
            raise IndexError("Pila vacía")

        res = self.arr[self.tos]
        self.arr[self.tos] = None
        self.tos -= 1

        return res