import math

NOMBRE_ARCHIVO = "arbol-prueba.txt"


def leer_arbol_txt(nombre_archivo):
    with open(nombre_archivo , 'r', encoding="utf-8") as f:
        contenido = f.readlines()
        contenido = [int(item.strip()) for item in contenido]

    return contenido

def altura_arbol(arreglo, grado):
    cantidad_elementos = len(arreglo)
    x = cantidad_elementos*grado - cantidad_elementos + 1
    altura = math.ceil(math.log(x, grado))
    return altura


arreglo = leer_arbol_txt(NOMBRE_ARCHIVO)
print(altura_arbol(arreglo,2))




