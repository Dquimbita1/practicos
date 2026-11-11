import sys
from cola import Cola
from leer_arbol import leer_arbol_txt


def barrido_por_niveles(arreglo, grado):
    if not arreglo:
        return

    cola = Cola(len(arreglo))
    raiz = 0  # indice
    cola.enqueue(raiz)

    while not cola.esta_vacia():
        indice = cola.dequeue()
        print(arreglo[indice])

        indice_primer_hijo = grado * indice + 1

        for i in range(grado):
            indice_hijo = indice_primer_hijo + i

            if indice_hijo < len(arreglo):
                cola.enqueue(indice_hijo)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit(
            "Uso: python3 barrido-por-nievles.py <grado> <archivo-origen>"
        )

    grado = int(sys.argv[1])
    arreglo = leer_arbol_txt(sys.argv[2])

    barrido_por_niveles(arreglo, grado)