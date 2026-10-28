import sys
from pila import Pila
from leer_arbol import leer_arbol_txt


def pre_orden(arreglo, grado):
    if not arreglo:
        return

    pila = Pila(len(arreglo))
    raiz = [arreglo[0], 0]  # [valor, indice]
    pila.push(raiz)

    while not pila.esta_vacia():
        valor, indice = pila.pop()
        print(valor)

        indice_primer_hijo = grado * indice + 1

        for i in range(grado):
            reversa = grado - i - 1
            indice_hijo = indice_primer_hijo + reversa

            if indice_hijo < len(arreglo):
                elemento = [
                    arreglo[indice_hijo],
                    indice_hijo
                ]
                pila.push(elemento)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit(
            "Uso: python3 barrido-pre-orden.py <grado> <archivo-origen>"
        )

    grado = int(sys.argv[1])
    arreglo = leer_arbol_txt(sys.argv[2])

    pre_orden(arreglo, grado)