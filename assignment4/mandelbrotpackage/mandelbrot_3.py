from matplotlib import pyplot as plt
from math import pi, e, exp, cos, sin, tan
import numpy as np
import seaborn
import numba
from numba import jit


@jit(nopython=True)
def mandelbrot_scale(x, iterations):
    """
    Iterates a given count over x to see if it approaches infinity, using 
    the mandelbrot set.
    
    Z0 = x
    Z1 = Z0^2 + x
    Z2 = Z1^2 + x
    ...
    Zn = Z(n-1)^2 + x

    where max{n} = iteration input

    If the absolute value of Zn gets greater than 2, it means the number
    set will eventually reach infinity, the iteration count will be returned.

    
    Arguments:
        x {complex} -- x is checked for where on the mandelbrot scale it lies
        iterations {int} -- threshold for iteration count.
    
    Returns:
        int -- Scale value for where x lies in the mandelbrot set.
    """
    # start values for c and x
    c = x
    z = 0
    i = 0
    # iterate set
    for iter in range(iterations):
        z = z*z + c
        if abs(z) > 2:
            # z will reach infinity
            break
        i = iter
    return i


@jit(nopython=True)
def mandelbrot_numba(x_min, x_max, y_min, y_max, Nx, Ny, iterations=1000):
    """
    Returns a matrix represantation of the given rectangle in the complex plane.
    Each value in the matrix being ona scale from 0 to 'iterations' representing

    
    Arguments:
        x_min {float} -- real value of the left edge of the rectangle
        x_max {float} -- real value of the right edge of the rectangle
        y_min {float} -- imag value of the bottom edge of the rectangle
        y_max {float} -- imag value of the top edge of the rectangle

        Nx {int} -- horizontal point count 
        Ny {int} -- vertical point count 
        iterations {int} -- (optional, default is set to 1000) Threshold iteration 
                            count to check if a complex is in the mandelbrot set
    
    Returns:
        2D numpy.array, (dtype=int):

        Matrix representation of the rectangle with real and imag values represented 
        by columns and rows respectively.
    """

    # retrieve the intervals
    x_interval = np.linspace(x_min, x_max, Nx)
    y_interval = np.linspace(y_min, y_max, Ny)

    rectangle = np.empty((Nx, Ny), dtype=numba.types.int32)

    # iterate every point, and set its scale value
    for real in range(Nx):
        for imag in range(Ny):
            scale = mandelbrot_scale(
                (x_interval[real] + y_interval[imag]*1j), iterations)
            rectangle[real, imag] = scale
    # transpose the matrix
    return rectangle.T
