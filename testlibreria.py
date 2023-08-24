import Libreriacomplejos as lc
import unittest

class TestStringMethods(unittest.TestCase):

    def test_suma(self):
        suma = lc.sumacomplejos((3,4),(4,-3.5))  # (3+4i) + (4-3.5i) = (7+0.5i)
        self.assertAlmostEqual(suma[0], 7)
        self.assertAlmostEqual(suma[1],0.5)
        suma = lc.sumacomplejos((-7,4),(4.2,-3)) # (-7+4i) + (4.2-3i) = (-2.8+i)
        self.assertAlmostEqual(suma[0], -2.8)
        self.assertAlmostEqual(suma[1], 1)
    def test_producto(self):
        producto = lc.multiplicacion((4,5),(3,-2)) #(4+5i)(3-2i) = (22 + 7i)
        self.assertAlmostEqual(producto[0],22)
        self.assertAlmostEqual(producto[1], 7)
        producto = lc.multiplicacion((2, -5), (-4, -3))  # (2-5i)(-4-3i) = (-23 + 14i)
        self.assertAlmostEqual(producto[0], -23)
        self.assertAlmostEqual(producto[1], 14)
    def test_resta(self):
        resta = lc.resta((4,3),(4,-5)) # (4+3i) - (4-5i) = (0+8i)
        self.assertAlmostEqual(resta[0], 0)
        self.assertAlmostEqual(resta[1], 8)
        resta = lc.resta((-8, -4), (10, 4))  # (-8-4i) - (10+4i) = (-18-8i)
        self.assertAlmostEqual(resta[0], -18)
        self.assertAlmostEqual(resta[1], -8)
    def test_division(self):
        div = lc.division((5,-2),(0,4)) # (5-2i)/(0+4i) = -0.5 - 1.25i
        self.assertAlmostEqual(div[0], -0.5)
        self.assertAlmostEqual(div[1], -1.25)
        div = lc.division((4,3),(2,4)) # (4+3i)/(2+4i) = 1 - 0.5i
        self.assertAlmostEqual(div[0], 1)
        self.assertAlmostEqual(div[1], -0.5)
    def test_modulo(self):
        modulo = lc.modulo((4,-3)) # (4-3i) = 5
        self.assertAlmostEqual(modulo, 5)
        modulo = lc.modulo((0,9)) # (0+9i) = 9
        self.assertAlmostEqual(modulo, 9)
    def test_conjugado(self):
        conju = lc.conjudado((4,5)) # (4 + 5i) = (4 - 5i)
        self.assertAlmostEqual(conju[0], 4)
        self.assertAlmostEqual(conju[1], -5)
        conju = lc.conjudado((3, -4))  # (3 - 4i) = (3 + 4i)
        self.assertAlmostEqual(conju[0], 3)
        self.assertAlmostEqual(conju[1], 4)
    def test_fase(self):
        fase = lc.fase((5,4)) #(5+4i) = arctan(5/4) = 0.0.67474094222355
        self.assertAlmostEqual(fase, 0.67474094222355)
        fase = lc.fase((8,4)) # (8+4i) = arctan(4/8) = 0.46364760900081
        self.assertAlmostEqual(fase, 0.46364760900081)
    def test_polar(self):
        polar = lc.polar((4,4)) #(4+4i) = (5.656854249492381, 0.7853981633974483)
        self.assertAlmostEqual(polar[0], 5.656854249492381)
        self.assertAlmostEqual(polar[1],  0.7853981633974483)
        polar = lc.polar((3,-   4)) #(3-4i) = (5,-0.9272952180016122)
        self.assertAlmostEqual(polar[0], 5)
        self.assertAlmostEqual(polar[1], -0.9272952180016122)
    def test_complejo(self):
        comp = lc.complejo((4,50)) #4e**50i = (3.8598641139684533 -1.049499414815715i)
        self.assertAlmostEqual(comp[0], 3.8598641139684533)
        self.assertAlmostEqual(comp[1], -1.049499414815715)
        comp = lc.complejo((1,90)) #e**90i = (-0.4480736161291701 +0.8939966636005579i)
        self.assertAlmostEqual(comp[0], -0.4480736161291701)
        self.assertAlmostEqual(comp[1], 0.8939966636005579)
if __name__ == '__main__':
    unittest.main()