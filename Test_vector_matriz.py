import Libreriacomplejos as lc
import unittest

class TestStringMethods(unittest.TestCase):
    def test_adicion(self):
        vector1, vector2 = [(4,3),(1,2),(44,2)], [(1,4),(5,9),(4,3)]
        suma = lc.sumvectores(vector1,vector2)
        resultado =  [(5,7),(6,11),(48,5)]
        for i in range(len(resultado)):
            self.assertAlmostEqual(suma[i],resultado[i])
        vector1, vector2 = [(-4, 9), (5, 0), (3, 1)], [(5, 4), (3, 1), (2, 3)]
        suma = lc.sumvectores(vector1, vector2)
        resultado = [(1, 13), (8, 1), (5, 4)]
        for i in range(len(resultado)):
            self.assertAlmostEqual(suma[i], resultado[i])
    def test_inversovector(self):
        vector = [(-3,4),(5,4),(8,0)]
        inverso = lc.inversoaditivovec(vector)
        resultado = [(3,-4),(-5,-4),(-8,0)]
        for i in range(len(resultado)):
            self.assertAlmostEqual(inverso[i], resultado[i])
        vector = [(5, 1), (0, 4), (3, 5)]
        inverso = lc.inversoaditivovec(vector)
        resultado = [(-5, -1), (0, -4), (-3, -5)]
        for i in range(len(resultado)):
            self.assertAlmostEqual(inverso[i], resultado[i])
    def test_multvecesc(self):
        escalar = (2,3)
        vector = [(4,1),(1,0),(5,-3)]
        multplicacion = lc.escalarmulvec(escalar, vector)
        resultado = [(5,14),(2,3),(19,9)]
        for i in range(len(resultado)):
            self.assertAlmostEqual(multplicacion[i], resultado[i])
        escalar = (2, 0)
        vector = [(4, 1), (1, 0), (5, -3)]
        multplicacion = lc.escalarmulvec(escalar, vector)
        resultado = [(8, 2), (2, 0), (10, -6)]
        for i in range(len(resultado)):
            self.assertAlmostEqual(multplicacion[i], resultado[i])
    def test_sumamtrices(self):
        matriz1 = [[(3,1),(0,1)],
                   [(2,8),(3,2)]]
        matriz2 = [[(10,5),(4,3)],
                   [(3,-1),(4,6)]]
        resultado = [[(13, 6), (4, 4)],
                    [(5, 7), (7, 8)]]
        suma = lc.adicionmatrices(matriz1,matriz2)
        for j in range(len(matriz1)):
            for k in range(len(matriz1[0])):
                self.assertAlmostEqual(suma[j][k], resultado[j][k])
        matriz1 = [[(3, 1), (0, 1), (9, 2)],
                   [(2, 8), (3, 2), (4, 6)]]
        matriz2 = [[(10, 5), (4, 3), (0, -8)],
                   [(3, -1), (4, 6), (40, 3)]]
        resultado = [[(13, 6), (4, 4), (9, -6)],
                     [(5, 7), (7, 8), (44, 9)]]
        suma = lc.adicionmatrices(matriz1, matriz2)
        for j in range(len(matriz2)):
            for k in range(len(matriz2[0])):
                self.assertAlmostEqual(suma[j][k], resultado[j][k])
    def test_inversamatriz(self):
        matriz = [[(3,-5),(-5,4),(0,0)],
                  [(4,5),(1,-5),(4,6)],
                  [(3,1),(-5,4),(4,5)]]
        resultado = [[(-3,5),(5,-4),(0,0)],
                  [(-4,-5),(-1,5),(-4,-6)],
                  [(-3,-1),(5,-4),(-4,-5)]]
        inversa = lc.inversomatriz(matriz)
        for j in range(len(matriz)):
            for k in range(len(matriz[0])):
                self.assertAlmostEqual(inversa[j][k], resultado[j][k])
        matriz = [[(10, 4), (3, 2)],
                  [(0, 1), (3, 2)]]
        resultado = [[(-10, -4), (-3, -2)],
                     [(0, -1), (-3, -2)]]
        inversa = lc.inversomatriz(matriz)
        for j in range(len(matriz)):
            for k in range(len(matriz[0])):
                self.assertAlmostEqual(inversa[j][k], resultado[j][k])
    def test_multescmatriz(self):
        escalar = (2,3)
        matriz = [[(4,1),(1,0)],
                  [(4,0),(0,1)]]
        resultado = [[(5,14),(2,3)],
                     [(8,12),(-3,2)]]
        multiplicacion = lc.matrizporescalar(escalar,matriz)
        for j in range(len(matriz)):
            for k in range(len(matriz[0])):
                self.assertAlmostEqual(multiplicacion[j][k], resultado[j][k])
        escalar = (2, 0)
        matriz = [[(4, 1), (1, 0)],
                  [(4, 0), (0, 1)]]
        resultado = [[(8, 2), (2, 0)],
                     [(8, 0), (0, 2)]]
        multiplicacion = lc.matrizporescalar(escalar, matriz)
        for j in range(len(matriz)):
            for k in range(len(matriz[0])):
                self.assertAlmostEqual(multiplicacion[j][k], resultado[j][k])
    def test_transpuesta(self):
        matriz = [[(1,0),(4,5),(8,4)],
                  [(-5,4),(-4,3),(4,2)]]
        resultado = [[(1,0),(-5,4)],
                     [(4,5),(-4,3)],
                     [(8,4),(4,2)]]
        transpuesta = lc.transpuesta(matriz)
        for j in range(len(transpuesta)):
            for k in range(len(transpuesta[0])):
                self.assertAlmostEqual(transpuesta[j][k], resultado[j][k])
        matriz = [[(1,0),(4,5)],
                  [(-5,4),(-4,3)]]
        resultado = [[(1,0),(-5,4)],
                     [(4,5),(-4,3)]]
        transpuesta = lc.transpuesta(matriz)
        for j in range(len(transpuesta)):
            for k in range(len(transpuesta[0])):
                self.assertAlmostEqual(transpuesta[j][k], resultado[j][k])
    def test_conjugada(self):
        vector = [(1, -2), (2, 4), (7, 8)]
        resultado = [(1,2),(2,-4),(7,-8)]
        conjugado = lc.conjugadavecmat(vector)
        for j in range(len(conjugado)):
            self.assertAlmostEqual(conjugado,resultado)
        matriz = [[(4,3),(4,8)],
                  [(54,11),(4,96)]]
        resultado = [[(4,-3),(4,-8)],
                     [(54,-11),(4,-96)]]
        conjugado = lc.conjugadavecmat(matriz)
        for j in range(len(matriz)):
            for k in range(len(matriz[0])):
                self.assertAlmostEqual(conjugado[j][k], resultado[j][k])


