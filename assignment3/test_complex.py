from complex import Complex
import unittest

class TestStringMethods(unittest.TestCase):

    def test_addition(self):
        z = Complex(-9, 4)
        w = Complex(2, -3)
        self.assertEqual(z + w, Complex(-7, 1))
        self.assertNotEqual(z + w, Complex())

    def test_subtraction(self):
        z = Complex(4, -2)
        w = Complex(-1, -3)
        self.assertEqual(z - w, Complex(5, 1))
        self.assertNotEqual(z - w, Complex(1, -2))

    def test_modulus(self):
        #3 : 4: 5 triangle
        z = Complex(3, -4)
        self.assertEqual(z.modulus(), 5)
        self.assertNotEqual(z.modulus(), 3.0)


    def test_multiplication(self):
        z = Complex(-5, -9)
        w = Complex(-2, 7)
        k = Complex(73, -17)
        self.assertEqual(z*w, k)
        self.assertNotEqual(z*w, Complex(3, 21))


    def test_conjugate(self):
        z = Complex(1, -2)
        self.assertEqual(z.conjugate(), Complex(1, 2))

    def test_eq(self):
        z = Complex(1, -2)
        w = Complex(1, -2)
        k = Complex(3, 4)

        self.assertEqual(z, w)
        self.assertNotEqual(z, k)

    def test_mult(self):
        k = Complex(3, 4)
        self.assertEqual(k*5, Complex(15, 20))

    def test_implemented_complex_addition(self):
        self.assertEqual(Complex(2,3) + (2+2j), Complex(4,5))
        self.assertEqual(23 + Complex(5, 3), Complex(28, 3))
        #assert (28, 0*1j)  == complex(28)


    def test_reverse_arithmetic(self):
        self.assertEqual((2+2j) + Complex(2, 3), Complex(4, 5))



if __name__ == "__main__":
    unittest.main()