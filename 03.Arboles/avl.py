"""Arbol AVL con insercion, recorridos y verificacion iterativos."""
from cola import Cola

class NodoAVL:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None
        self.altura = 1

class ArbolAVL:
    def __init__(self):
        self.raiz = None
        self.cantidad = 0

    def altura(self, nodo):
        return 0 if nodo is None else nodo.altura

    def factor_balanceo(self, nodo):
        if nodo is None:
            return 0
        return self.altura(nodo.izquierda) - self.altura(nodo.derecha)

    def actualizar_altura(self, nodo):
        nodo.altura = 1 + max(self.altura(nodo.izquierda),
                              self.altura(nodo.derecha))

    def rotar_izquierda(self, x):
        y = x.derecha
        subarbol = y.izquierda
        y.izquierda = x
        x.derecha = subarbol
        self.actualizar_altura(x)
        self.actualizar_altura(y)
        return y

    def rotar_derecha(self, y):
        x = y.izquierda
        subarbol = x.derecha
        x.derecha = y
        y.izquierda = subarbol
        self.actualizar_altura(y)
        self.actualizar_altura(x)
        return x

    def insertar(self, valor):
        """Devuelve True si se inserto y False si era repetido."""
        if self.raiz is None:
            self.raiz = NodoAVL(valor)
            self.cantidad = 1
            return True

        camino = []
        actual = self.raiz
        padre = None
        while actual is not None:
            if actual.valor == valor:
                return False
            camino.append(actual)
            padre = actual
            actual = actual.izquierda if valor < actual.valor else actual.derecha

        nuevo = NodoAVL(valor)
        if valor < padre.valor:
            padre.izquierda = nuevo
        else:
            padre.derecha = nuevo
        self.cantidad += 1

        # Subir desde el padre recien modificado, sin recursividad.
        for i in range(len(camino) - 1, -1, -1):
            nodo = camino[i]
            self.actualizar_altura(nodo)
            balance = self.factor_balanceo(nodo)
            if balance > 1:
                if self.factor_balanceo(nodo.izquierda) < 0:
                    nodo.izquierda = self.rotar_izquierda(nodo.izquierda)
                nueva_raiz = self.rotar_derecha(nodo)
            elif balance < -1:
                if self.factor_balanceo(nodo.derecha) > 0:
                    nodo.derecha = self.rotar_derecha(nodo.derecha)
                nueva_raiz = self.rotar_izquierda(nodo)
            else:
                continue

            if i == 0:
                self.raiz = nueva_raiz
            else:
                antecesor = camino[i - 1]
                if antecesor.izquierda is nodo:
                    antecesor.izquierda = nueva_raiz
                else:
                    antecesor.derecha = nueva_raiz
            return True
        return True

    def en_orden(self):
        resultado = []
        pila = []
        actual = self.raiz
        while actual is not None or pila:
            while actual is not None:
                pila.append(actual)
                actual = actual.izquierda
            actual = pila.pop()
            resultado.append(actual.valor)
            actual = actual.derecha
        return resultado

    def por_niveles(self):
        if self.raiz is None:
            return []
        niveles = []
        cola = Cola(self.cantidad)
        cola.enqueue(self.raiz)
        while not cola.esta_vacia():
            cantidad_nivel = cola.cantidad
            valores_nivel = []
            for _ in range(cantidad_nivel):
                nodo = cola.dequeue()
                valores_nivel.append(nodo.valor)
                if nodo.izquierda is not None:
                    cola.enqueue(nodo.izquierda)
                if nodo.derecha is not None:
                    cola.enqueue(nodo.derecha)
            niveles.append(valores_nivel)
        return niveles

    def es_avl(self):
        """Verifica orden de ABB, alturas y balance sin recursion."""
        if self.raiz is None:
            return self.cantidad == 0
        pila = [(self.raiz, 0, None, None)]
        alturas = {}
        cantidad_visitada = 0
        while pila:
            nodo, estado, minimo, maximo = pila.pop()
            if estado == 0:
                if minimo is not None and nodo.valor <= minimo:
                    return False
                if maximo is not None and nodo.valor >= maximo:
                    return False
                pila.append((nodo, 1, minimo, maximo))
                if nodo.derecha is not None:
                    pila.append((nodo.derecha, 0, nodo.valor, maximo))
                if nodo.izquierda is not None:
                    pila.append((nodo.izquierda, 0, minimo, nodo.valor))
            else:
                hi = alturas.get(nodo.izquierda, 0)
                hd = alturas.get(nodo.derecha, 0)
                altura_real = 1 + max(hi, hd)
                if abs(hi - hd) > 1 or nodo.altura != altura_real:
                    return False
                alturas[nodo] = altura_real
                cantidad_visitada += 1
        return cantidad_visitada == self.cantidad
