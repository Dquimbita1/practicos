"""Pruebas del AVL: python3 -m unittest -v test_avl.py"""
import random
import tempfile
import unittest
from pathlib import Path
from avl import ArbolAVL
import importlib.util

SPEC = importlib.util.spec_from_file_location(
    "crear_avl", Path(__file__).with_name("crear-avl.py"))
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)

class PruebasAVL(unittest.TestCase):
    def crear(self, numeros):
        arbol = ArbolAVL()
        for numero in numeros:
            arbol.insertar(numero)
            self.assertTrue(arbol.es_avl(), f"Desbalance al insertar {numero}")
        self.assertEqual(arbol.en_orden(), sorted(set(numeros)))
        self.assertEqual(arbol.cantidad, len(set(numeros)))
        return arbol

    def test_vacio(self):
        a = ArbolAVL()
        self.assertTrue(a.es_avl())
        self.assertEqual(a.en_orden(), [])
        self.assertEqual(a.por_niveles(), [])

    def test_ll(self):
        a = self.crear([30, 20, 10])
        self.assertEqual(a.raiz.valor, 20)
        self.assertEqual(a.por_niveles(), [[20], [10, 30]])

    def test_rr(self):
        self.assertEqual(self.crear([10, 20, 30]).raiz.valor, 20)

    def test_lr(self):
        self.assertEqual(self.crear([30, 10, 20]).raiz.valor, 20)

    def test_rl(self):
        self.assertEqual(self.crear([10, 30, 20]).raiz.valor, 20)

    def test_rotaciones_internas(self):
        a = self.crear([100, 50, 150, 25, 75, 125, 175, 60, 55, 140, 145])
        self.assertEqual(a.en_orden(),
                         [25, 50, 55, 60, 75, 100, 125, 140, 145, 150, 175])

    def test_duplicados_y_negativos(self):
        a = self.crear([0, -10, 10, -20, 20, -10, 10, 0])
        self.assertEqual(a.cantidad, 5)
        self.assertFalse(a.insertar(-10))

    def test_mil_ascendentes(self):
        a = self.crear(range(1000))
        self.assertLessEqual(a.altura(a.raiz), 12)

    def test_mil_descendentes(self):
        a = self.crear(range(999, -1, -1))
        self.assertLessEqual(a.altura(a.raiz), 12)

    def test_aleatorios(self):
        valores = random.Random(2026).sample(range(-10000, 10000), 1500)
        self.crear(valores)

    def test_txt(self):
        with tempfile.TemporaryDirectory() as carpeta:
            ruta = Path(carpeta) / "datos.txt"
            ruta.write_text("30, 10; 20\n# comentario\n40 -5\n", encoding="utf-8")
            self.assertEqual(MOD.leer_inserciones(str(ruta)),
                             [30, 10, 20, 40, -5])

    def test_json(self):
        with tempfile.TemporaryDirectory() as carpeta:
            ruta = Path(carpeta) / "datos.json"
            ruta.write_text('{"inserciones":[30,10,20]}', encoding="utf-8")
            self.assertEqual(MOD.leer_inserciones(str(ruta)), [30, 10, 20])

if __name__ == "__main__":
    unittest.main()
