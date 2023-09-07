import Libreriacomplejos as lc
import unittest

class TestStringMethods(unittest.TestCase):
    def test_adicion(self):
        vector1, vector2 = [(4,3),(1,2),(44,2)], [(1,4),(5,9),(4,3)]
        suma = lc.sumvectores(vector1,vector2)
        resultado =  [(5,7),(6,11),(48,5)]
        self.assertEqual(suma,resultado)
        vector1, vector2 = [(-4, 9), (5, 0), (3, 1)], [(5, 4), (3, 1), (2, 3)]
        suma = lc.sumvectores(vector1, vector2)
        resultado = [(1, 13), (8, 1), (5, 4)]
        self.assertEqual(suma, resultado)
    def test_inversovector(self):
        vector = [(-3,4),(5,4),(8,0)]
        inverso = lc.inversoaditivovec(vector)
        resultado = [(3,-4),(-5,-4),(-8,0)]
        self.assertEqual(inverso, resultado)
        vector = [(5, 1), (0, 4), (3, 5)]
        inverso = lc.inversoaditivovec(vector)
        resultado = [(-5, -1), (0, -4), (-3, -5)]
        self.assertEqual(inverso, resultado)
    def test_multvecesc(self):
        escalar = (2,3)
        vector = [(4,1),(1,0),(5,-3)]
        multplicacion = lc.escalarmulvec(escalar, vector)
        resultado = [(5,14),(2,3),(19,9)]

        self.assertEqual(multplicacion, resultado)
        escalar = (2, 0)
        vector = [(4, 1), (1, 0), (5, -3)]
        multplicacion = lc.escalarmulvec(escalar, vector)
        resultado = [(8, 2), (2, 0), (10, -6)]
        self.assertEqual(multplicacion, resultado)
    def test_sumamtrices(self):
        matriz1 = [[(3,1),(0,1)],
                   [(2,8),(3,2)]]
        matriz2 = [[(10,5),(4,3)],
                   [(3,-1),(4,6)]]
        resultado = [[(13, 6), (4, 4)],
                    [(5, 7), (7, 8)]]
        suma = lc.adicionmatrices(matriz1,matriz2)
        self.assertEqual(suma, resultado)
        matriz1 = [[(3, 1), (0, 1), (9, 2)],
                   [(2, 8), (3, 2), (4, 6)]]
        matriz2 = [[(10, 5), (4, 3), (0, -8)],
                   [(3, -1), (4, 6), (40, 3)]]
        resultado = [[(13, 6), (4, 4), (9, -6)],
                     [(5, 7), (7, 8), (44, 9)]]
        suma = lc.adicionmatrices(matriz1, matriz2)
        self.assertEqual(suma, resultado)
    def test_inversamatriz(self):
        matriz = [[(3,-5),(-5,4),(0,0)],
                  [(4,5),(1,-5),(4,6)],
                  [(3,1),(-5,4),(4,5)]]
        resultado = [[(-3,5),(5,-4),(0,0)],
                  [(-4,-5),(-1,5),(-4,-6)],
                  [(-3,-1),(5,-4),(-4,-5)]]
        inversa = lc.inversomatriz(matriz)
        self.assertEqual(inversa, resultado)
        matriz = [[(10, 4), (3, 2)],
                  [(0, 1), (3, 2)]]
        resultado = [[(-10, -4), (-3, -2)],
                     [(0, -1), (-3, -2)]]
        inversa = lc.inversomatriz(matriz)
        self.assertEqual(inversa, resultado)
    def test_multescmatriz(self):
        escalar = (2,3)
        matriz = [[(4,1),(1,0)],
                  [(4,0),(0,1)]]
        resultado = [[(5,14),(2,3)],
                     [(8,12),(-3,2)]]
        multiplicacion = lc.matrizporescalar(escalar,matriz)
        self.assertEqual(multiplicacion, resultado)
        escalar = (2, 0)
        matriz = [[(4, 1), (1, 0)],
                  [(4, 0), (0, 1)]]
        resultado = [[(8, 2), (2, 0)],
                     [(8, 0), (0, 2)]]
        multiplicacion = lc.matrizporescalar(escalar, matriz)
        self.assertEqual(multiplicacion, resultado)
    def test_transpuesta(self):
        matriz = [[(1,0),(4,5),(8,4)],
                  [(-5,4),(-4,3),(4,2)]]
        resultado = [[(1,0),(-5,4)],
                     [(4,5),(-4,3)],
                     [(8,4),(4,2)]]
        transpuesta = lc.transpuesta(matriz)
        self.assertEqual(transpuesta, resultado)
        matriz = [[(1,0),(4,5)],
                  [(-5,4),(-4,3)]]
        resultado = [[(1,0),(-5,4)],
                     [(4,5),(-4,3)]]
        transpuesta = lc.transpuesta(matriz)
        self.assertEqual(transpuesta, resultado)

    def test_conjugada(self):
        vector = [(1, -2), (2, 4), (7, 8)]
        resultado = [(1,2),(2,-4),(7,-8)]
        conjugado = lc.conjugadavecmat(vector)
        self.assertEqual(conjugado,resultado)
        matriz = [[(4,3),(4,8)],
                  [(54,11),(4,96)]]
        resultado = [[(4,-3),(4,-8)],
                     [(54,-11),(4,-96)]]
        conjugado = lc.conjugadavecmat(matriz)
        self.assertEqual(conjugado, resultado)
    def test_adjunta(self):
        vector = [(1, -2), (2, 4), (7, 8)]
        resultado = [(1, 2), (2, -4), (7, -8)]
        adjunta = lc.conjugadavecmat(vector)
        self.assertEqual(adjunta, resultado)
        matriz = [[(4, 3), (4, 8)],
                [(54, 11), (4, 96)]]
        resultado = [[(4, -3), (54, -11)],
                     [(4, -8), (4, -96)]]

        adjunta = lc.daga(matriz)
        self.assertEqual(adjunta, resultado)
    def test_productomatrices(self):
        matriz = [[(4, 1), (1, 0)],
                  [(4, 0), (0, 1)]]
        matriz2 = [[(4, 1), (1, 0)],
                  [(4, 0), (0, 1)]]
        resultado = [[(19,8),(4,2)],[(16,8),(3,0)]]
        mult = lc.multmatrices(matriz,matriz2)
        self.assertEqual(mult, resultado)
        matriz = [[(1, 1), (1, 5)],
                  [(5, 9), (4, 1)]]
        matriz2 = [[(4, 1), (1, 0)],
                   [(4, 0), (0, 1)]]
        resultado = [[(7,25),(-4,2)],[(27,45),(4,13)]]
        mult = lc.multmatrices(matriz, matriz2)
        self.assertEqual(mult, resultado)
    def test_accionvector(self):
        matriz = [[(1, 1), (1, 5)],
                  [(5, 9), (4, 1)]]
        vector = [(5,2),(3,0)]
        resultado = [(6,22),(19,58)]
        accion = lc.accionvecmat(matriz,vector)
        self.assertEqual(accion, resultado)
        matriz = [[(4, 1), (1, 0)],
                   [(4, 0), (0, 1)]]
        vector = [(5, 8), (4, 20)]
        resultado = [(16, 57), (0, 36)]
        accion = lc.accionvecmat(matriz, vector)
        self.assertEqual(accion, resultado)
    def test_productointerno(self):
        v1 = [(1,0),(2,3),(0,6)]
        v2 = [(0,0),(0,1),(2,4)]
        resultado = (27,-10)
        producto = lc.producintern(v1,v2)
        self.assertEqual(producto, resultado)
        v1 = [(1, 0), (0, 1), (1, -3)]
        v2 = [(2, 1), (0, 1), (2, 0)]
        resultado = (5, 7)
        producto = lc.producintern(v1, v2)
        self.assertEqual(producto, resultado)
    def test_norma(self):
        v1 = [(4,3),(6,-4),(12,-7),(0,13)]
        resultado = 439**(1/2)
        norma = lc.norma(v1)
        self.assertEqual(norma, resultado)
        v1 = [(2,5),(1,-4),(0,-7),(0,3)]
        resultado = 104 ** (1 / 2)
        norma = lc.norma(v1)
        self.assertEqual(norma, resultado)
    def test_distancia(self):
        v1 = [(0,2),(3,0),(0,4)]
        v2 = [(0,1),(-3,0),(0,-5)]
        resultado = 118**(1/2)
        distancia = lc.distancia(v1,v2)
        self.assertEqual(resultado,distancia)
        v1 = [(3,2),(4,0)]
        v2 = [(4,0),(3,2)]
        resultado = 10** (1 / 2)
        distancia = lc.distancia(v1, v2)
        self.assertEqual(resultado, distancia)
    def test_valorespropios(self):
       matriz = [[(0,0),(0,4)],[(0,-4),(0,0)]]
       vector = [(0,1),(1,0)]
       resultado = 4.0
       valor = lc.valorpropio(matriz,vector)
       self.assertEqual(resultado,valor)
       matriz = [[(0, 0), (0, 41)], [(0, -41), (0, 0)]]
       vector = [(0, 4), (4, 0)]
       resultado = 41.0
       valor = lc.valorpropio(matriz, vector)
       self.assertEqual(resultado, valor)
