"""Ejercicio 2: python3 crear-avl.py <archivo-origen>"""
import json
import sys
from avl import ArbolAVL

def leer_inserciones(nombre_archivo):
    if nombre_archivo.lower().endswith(".json"):
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
        if isinstance(datos, dict):
            datos = datos["inserciones"]
        if not isinstance(datos, list):
            raise ValueError("El JSON debe contener una lista de inserciones")
        return [int(valor) for valor in datos]

    resultado = []
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea = linea.split("#", 1)[0]
            linea = (linea.replace(",", " ").replace(";", " ")
                          .replace("[", " ").replace("]", " "))
            for valor in linea.split():
                resultado.append(int(valor))
    return resultado

def main(nombre_archivo):
    valores = leer_inserciones(nombre_archivo)
    arbol = ArbolAVL()
    for valor in valores:
        arbol.insertar(valor)
    print("Inserciones leidas:", len(valores))
    print("Nodos distintos:", arbol.cantidad)
    print("Altura:", arbol.altura(arbol.raiz))
    print("AVL valido:", "SI" if arbol.es_avl() else "NO")
    print("Inorden:", " ".join(str(v) for v in arbol.en_orden()))
    print("Por niveles:")
    for numero, nivel in enumerate(arbol.por_niveles(), start=1):
        print(f"Nivel {numero}:", " ".join(str(v) for v in nivel))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Uso: python3 crear-avl.py <archivo-origen>")
    main(sys.argv[1])
