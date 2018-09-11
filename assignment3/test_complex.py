from complex import Complex
import unittest

class TestStringMethods(unittest.TestCase):
    """
    This module provides a unittest of Complex

    All test functions have a pre-computed correct value for the method they call with the
    provided arguments. The methods are tested by asserting that 
    """

    def test_eq(self):
        """
        Tests Complex's equalness operator.
        Implementation:
            asserts that:
            - two differenect Complex objects with equal .real and .imag are asserted as equal.
            - Complex(1, -2) and Complex(3, 0) are not equal
            - a float 3.0 is equal to Complex(3, 0)
            - Complex(1, -2) is equal to complex(1, 2)a
        Raises: AssertionError
        """
        z = Complex(1, -2)
        w = Complex(1, -2)

        k = Complex(3, 0)
        i = 3.0
        j = (1 - 2j)

        self.assertEqual(z, w)
        self.assertNotEqual(z, k)
        self.assertEqual(k, i)
        self.assertEqual(z, j)

    """
    following test functions has a prerequisite such that __eq__ of Complex is correctly
    implemented
    """
    def test_addition(self):
        """
        tests Complex's addition operator.
        
        Implementation:
            asserts the following:
            z = Complex(-9, 4)
            w = Complex(2, -3)

            assert z + w == Complex(-7, 1)

        Raises: AssertionError
        """
        z = Complex(-9, 4)
        w = Complex(2, -3)
        self.assertEqual(z + w, Complex(-7, 1))
        self.assertNotEqual(z + w, Complex())

    def test_subtraction(self):
        """
        testing Complex's addition operator.
        Implementation:
            asserts the following:
            z = Complex(4, -2)
            w = Complex(-1, -3)

            assert z - w == Complex(-7, 1)
            assert z - w != Complex(1, -2)

        Raises: AssertionError
        """
        z = Complex(4, -2)
        w = Complex(-1, -3)
        self.assertEqual(z - w, Complex(5, 1))
        self.assertNotEqual(z - w, Complex(1, -2))

    def test_modulus(self):
        """
        testing Complex's modulus method
        Implementation:
            assert the following:
            z = Complex(3, -4)
            w = Complex(1, 5)

            assert z.modulus() == 5
            assert w..modulus() != 5 

        Raises: AssertionError

        Raises: AssertionError
        """
        #3 : 4: 5 triangle
        z = Complex(3, -4)
        w = Complex(1, 5)
        self.assertEqual(z.modulus(), 5)
        self.assertNotEqual(w.modulus(), 5)


    def test_multiplication(self):
        """
        testing Complex's __mul__
        Implementation:

            z = Complex(-5, -9)
            w = Complex(-2, 7)
            k = Complex(73, -17)
            assert that z * w == k
            assert that z * w == Complex(3, 21)

        Raises: AssertionError
        """
        z = Complex(-5, -9)
        w = Complex(-2, 7)
        k = Complex(73, -17)
        self.assertEqual(z*w, k)
        self.assertNotEqual(z*w, Complex(3, 21))


    def test_conjugate(self):
        """
        Test whether b

        Implementation:
            assert that conjugate returns a complex with imag negated.
            Complex(real, imag).conjugate() == Complex(real, -imag)

        z = Complex(1, -2)
        w = Complex(1, 2)

        assert z.conjugate() == w 
        Raises: AssertionError
        """
        z = Complex(1, -2)
        w = Complex(1, 2)
        self.assertEqual(z.conjugate(), w)



    def test_implemented_complex_addition(self):
        """
        tests Complex's radd operator.
        
        Implementation:
            asserts that an int, float or complex can be added to Complex, with Complex on
            the right side of the plus sign.

            z = 23
            w = Complex(5, -3)
            assert z + w == Complex(28, -3)

            k = (2 -9j)
            i = Complex(2, 4)
            assert k + i == Comlex(0, -13)

        Raises: AssertionError
        """
        self.assertEqual(23 + Complex(5, 3), Complex(28, 3))
        self.assertEqual((2 - 9j) - Complex(2, 4), Complex(0, -13))
        #assert (28, 0*1j)  == complex(28)

    def test_str(self):
        """
        tests Complex's __str__

        Implementation:
            denominatior of i is removed if it is equal to 1 or -1.
            assert str(Complex(2, -3)) == '2-3i'

            str returns '0', if both imag and real is equal to 0.
            assert str(Complex(0, 0)) == '0'

            if real == 0 and imag > 0, the string should not include "+".
            if real == 0 and imag < 0, the string should include "-" as a prefix.
            assert str(Complex(0, 3)) == '3i'
            assert str(Complex(0, -3)) == '-3i'

            assert str(Complex(2)) == '2'


        Raises: AssertionError
        """
        self.assertEqual(str(Complex(2, -3)), "2-3i")
        self.assertEqual(str(Complex(5, 9)), "5+9i")
        self.assertEqual(str(Complex(0, 3)), "3i")
        self.assertEqual(str(Complex(0, -3)), "-3i")
        self.assertEqual(str(Complex()), "0")
        self.assertEqual(str(Complex(2)), "2")

    def test_mul_complex_im(self):
        """
        Implementation:
            This function asserts that mul is correctly implemented for Complex.

            complex(2, 2) + Complex(2, 3) == Complex(4, 5)
            6 - Complex(2, 3) == Complex(4, 3)

        Raises:
            AssertionError
        """
        z = Complex(2, 1)
        w = Complex(0, 5)
        self.assertEqual(z*w, Complex(-5,10))


    def test_reverse_arithmetic(self):
        """
        Tests radd, rsub, rmul.
        Implementation:
            This function asserts that the reverse arithmetic funtions are implemented
            correctly for Complex.

            complex(2, 2) + Complex(2, 3) == Complex(4, 5)
            6 - Complex(2, 3) == Complex(4, 3)
            complex(7, 2) - Complex(4, 2) == Complex(3, 0)

        Raises:
            AssertionError
        """
        self.assertEqual((2+2j) + Complex(2, 3), Complex(4, 5))
        self.assertEqual(6 - Complex(2, 3), Complex(4, -3))
        self.assertEqual(complex(7, 2) - Complex(4, 2), Complex(3, 0))

        


#run main
if __name__ == "__main__":
    unittest.main()
    