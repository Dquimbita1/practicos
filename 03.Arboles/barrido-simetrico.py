import sys
from pila import Pila
from leer_arbol import leer_arbol_txt


def barrido_simetrico(arreglo):
    if not arreglo:
        return

    pila = Pila(len(arreglo))
    raiz = [0, 0]  # [indice, estado]
    pila.push(raiz)

    while not pila.esta_vacia():
        indice, estado = pila.pop()

        hijo_izq = 2 * indice + 1
        hijo_der = hijo_izq + 1

        if estado == 0:
            pila.push([indice, 1])

            if hijo_izq < len(arreglo):
                pila.push([hijo_izq, 0])

        else:
            print(arreglo[indice])

            if hijo_der < len(arreglo):
                pila.push([hijo_der, 0])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(
            "Uso: python3 barrido-simetrico.py <archivo-origen>"
        )

    arreglo = leer_arbol_txt(sys.argv[1])
    barrido_simetrico(arreglo)