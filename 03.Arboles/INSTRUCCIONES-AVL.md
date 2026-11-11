# TP3 — Árbol AVL iterativo

La solución de **ejercicio 2** está en `avl.py` y `crear-avl.py`.
No emplea recursividad. Reutiliza la `Cola` del ejercicio 1.

## Ejecutar
```bash
python3 crear-avl.py datos-avl-ejemplo.txt
python3 -m unittest -v test_avl.py
```

Para el archivo de inserciones de la cátedra:
```bash
python3 crear-avl.py ruta/al/archivo.txt
```

Admite enteros TXT (líneas, espacios, comas y punto y coma) o JSON con lista
de números / objeto `{"inserciones":[...]}`. Los repetidos se ignoran.

## Verificaciones
- Rotaciones simples LL y RR, dobles LR y RL.
- Inserción iterativa con seguimiento de antecesores y actualización de alturas.
- Recorrido inorden y por niveles; verificación iterativa del balance AVL.
- 12 pruebas unitarias. El formato de salida del inciso 2 no está especificado
  en el Readme de la cátedra; se da una salida explicativa.

Pendiente: contrastar el resultado concreto con las inserciones oficiales,
que no estaban incluidas en el Readme consultado.

No se modificaron los archivos entregados por la cátedra.
