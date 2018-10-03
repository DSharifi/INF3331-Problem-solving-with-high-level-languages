import unittest
from mandelbrot_1 import mandelbrot_python
from mandelbrot_2 import mandelbrot_numpy
from mandelbrot_3 import mandelbrot_numba
import numpy as np

# import mandelbrot_3


class TestStringMethods(unittest.TestCase):
    """
    This module provides a unittest of mandelbrot_1, mandelbrot_2 and mandelbrot_3
    """

    def test_is_nan(self):
        """
        Given mandelbrot_n() a rectangle outside of the mandelbrot set, it asserts that
        the output matrix' values are all less than iteration count.
        """

        def is_m_nan(m):
            for x in m:
                for y in x:
                    if y == iterations - 1:
                        return False
            return True

        #exaggareted values for rectangle 
        xmin = 999999
        xmax = 9999999
        ymin = 999999
        ymax = 9999999

        Nx = 30
        Ny = 30

        iterations = 1000

        m1 = mandelbrot_python(xmin, xmax, ymin, ymax,
                               Nx, Ny, iterations)
        self.assertTrue(is_m_nan(m1))

        m2 = mandelbrot_numpy(xmin, xmax, ymin, ymax,
                               Nx, Ny, iterations)
        self.assertTrue(is_m_nan(m2))

        m3 = mandelbrot_numba(xmin, xmax, ymin, ymax,
                               Nx, Ny, iterations)
        self.assertTrue(is_m_nan(m3))



    def test_is_zero(self):
        """
        Given mandelbrot_n() a rectangle inside the mandelbrot set, it asserts that
        the output matrix' values are equal to the iteration count - 1.
        """
        def is_m_zero(m):
            for x in m:
                for y in x:
                    if y != iterations-1:
                        return False
            return True

        xmin = -0.5
        xmax = 0
        ymin = -0.1
        ymax = 0.1
        Nx = 30
        Ny = 30
        iterations = 1000

        #test all implementations of mandelbrot

        m1 = mandelbrot_python(xmin, xmax, ymin, ymax,
                               Nx, Ny, iterations)
        self.assertTrue(is_m_zero(m1))

        m2 = mandelbrot_numpy(xmin, xmax, ymin, ymax,
                               Nx, Ny, iterations)
        self.assertTrue(is_m_zero(m2))

        m3 = mandelbrot_numba(xmin, xmax, ymin, ymax,
                               Nx, Ny, iterations)
        self.assertTrue(is_m_zero(m3))


#run unit test
if __name__ == "__main__":
    unittest.main()
