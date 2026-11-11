def leer_arbol_txt(nombre_archivo):
    with open(nombre_archivo, "r", encoding="utf-8") as f:
        return [
            int(linea.strip())
            for linea in f
            if linea.strip()
        ]