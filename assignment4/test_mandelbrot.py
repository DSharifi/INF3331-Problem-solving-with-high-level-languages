import unittest
from mandelbrot_1 import mandelbrot_python
from mandelbrot_2 import mandelbrot_numpy
from mandelbrot_3 import mandelbrot_numba
import numpy as np


class TestStringMethods(unittest.TestCase):
    """
    This module provides a unittest of mandelbrot_1, mandelbrot_2 and mandelbrot_3
    """

    def test_is_not_mandelbrot(self):
        """
        Given a rectangle outside of the mandelbrot set, it asserts that
        the functions output matrix' values are all equal to 0.
        """

        # iterate every point
        def is_m_nan(m):
            for x in m:
                for y in x:
                    if y != 0:
                        return False
            return True

        # rectangle completely outside of the mandelbrot set
        xmin = 3
        xmax = 4
        ymin = 3
        ymax = 4

        Nx = 1000
        Ny = 1000

        iterations = 10

        # test all implementations of mandelbrot
        # and assert its values
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
        Given a rectangle outside of the mandelbrot set, it asserts that
        the functions output matrix' values are all equal to the iteration count - 1.
        """

        # iterate every point
        def is_m_zero(m):
            for x in m:
                for y in x:
                    if y != iterations-1:
                        return False
            return True

        # rectangle completely within the mandelbrot set
        xmin = -0.5
        xmax = 0
        ymin = -0.1
        ymax = 0.1
        Nx = 10
        Ny = 10
        iterations = 1000

        # test all implementations of mandelbrot
        # and assert its values
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
