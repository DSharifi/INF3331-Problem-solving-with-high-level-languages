from matplotlib import pyplot as plt
from math import pi, e, exp, cos, sin, tan
import numpy as np
import seaborn
from numba import jit



def mandelbrot_scale(x, iterations):
    """
    Iterates a given count over x to see if it approaches infinity, using 
    the mandelbrot set.
    
    Z0 = x
    Z1 = Z0^2 + x
    Z2 = Z1^2 + x
    ...
    Zn = Z(n-1)^2 + x

    If the absolute value of Zn reaches nan then n will be returned.
    Else, iterations argument will be returned

    
    Arguments:
        x {complex} -- x is checked for where on the mandelbrot scale it lies
        iterations {int} -- threshold for iteration count.
    
    Returns:
        int -- Scale value for x lies in the mandelbrot set.
    """

    c = x
    z = 0
    for iter in range(iterations):
        z = z*z + c
       
        if np.isnan(z):
            # z is reaching infinity, thus not in the set
            break
    return iter


def mandelbrot_numpy(x_min, x_max, y_min, y_max, Nx, Ny, iterations=1000):
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

    #create grid, and turn it into complex plane matrix
    xv, yv = np.meshgrid(x_interval, y_interval)
    rectangle = xv + yv*1j 

    # iterate every point, and set its scale value
    myfunc = np.vectorize(mandelbrot_scale)

    return myfunc(rectangle, iterations)
