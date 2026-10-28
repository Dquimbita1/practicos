import sys
from pila import Pila
from leer_arbol import leer_arbol_txt


def post_orden(arreglo, grado):
    if not arreglo:
        return

    pila = Pila(len(arreglo))
    raiz = [0, 0]  # [indice, estado]
    pila.push(raiz)

    while not pila.esta_vacia():
        indice, estado = pila.pop()

        if estado == 0:
            pila.push([indice, 1])

            indice_primer_hijo = grado * indice + 1

            for i in range(grado):
                reversa = grado - i - 1
                indice_hijo = indice_primer_hijo + reversa

                if indice_hijo < len(arreglo):
                    pila.push([indice_hijo, 0])

        else:
            print(arreglo[indice])


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit(
            "Uso: python3 barrido-post-orden.py <grado> <archivo-origen>"
        )

    grado = int(sys.argv[1])
    arreglo = leer_arbol_txt(sys.argv[2])

    post_orden(arreglo, grado)