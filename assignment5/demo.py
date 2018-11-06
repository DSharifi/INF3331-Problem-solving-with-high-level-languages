from mandelbrot_1 import mandelbrot_python
from mandelbrot_2 import mandelbrot_numpy
from mandelbrot_3 import mandelbrot_numba
from matplotlib import pyplot as plt
import seaborn
import os
from sys import argv



def menu(f, x_min, x_max, y_min, y_max, Nx, Ny, colorscale, filename):
    """
    Main menu for command line based user interface.

    Given function rectangle infromation: region, resolution, filename and colorscale, a
    picture represntation of a mandelbrot set in the rectangle is returned
    
    Arguments:
        func {str} -- chosen function to compute mandelbrot set from the given rectangle
                            Valid args: Python, NumPy, Numba
        x_min {float} -- edge value
        x_max {float} -- edge value
        y_min {float} -- edge value
        y_max {float} -- edge value

        Nx {int} -- horizontal point count 
        Ny {int} -- vertical point count 

        filename {str} -- filename for output png file
        colorscale {str} -- Colorscale used to color the set
    """
    dpi = 1000
    maxiter = 1000
    # matrix representation of users rectangle
    matrix = get_matrix(f, x_min, x_max, y_min, y_max,
                        Nx, Ny, maxiter)
    # draw the rectangle
    draw(x_min, x_max, y_min, y_max, matrix, colorscale, dpi)
    # save drawn plt
    plt.savefig(filename + ".png", dpi=dpi)


def get_matrix(f, x_min, x_max, y_min, y_max, Nx, Ny, iterations):
    """
    Wrapper function for mandelbrot_python(), mandelbrot_numpy() and mandelbrot_numba().

    Arguments:
        func {str} -- chosen function to compute mandelbrot set from the given rectangle
                        Valid args: Python, NumPy, Numba
        x_min {float} -- edge value
        x_max {float} -- edge value
        y_min {float} -- edge value
        y_max {float} -- edge value

        Nx {int} -- horizontal point count 
        Ny {int} -- vertical point count 
        region          -- {tuple {float}} -- (x_min, x_max, y_min, y_max)
        resolution      -- {tuple {int}} -- (Nx, Ny)
        iterations {int} -- max iteration

    Returns:
    2D numpy.array(dtype=int):
        Matrix representation of the rectangle with real and imag values represented 
        by columns and rows respectively
    """
    # ru
    if f.lower() == "python":
        return mandelbrot_python(x_min, x_max, y_min, y_max, Nx, Ny, iterations)
    elif f.lower() == "numpy":
        return mandelbrot_numpy(x_min, x_max, y_min, y_max, Nx, Ny, iterations)
    elif f.lower() == "numba":
        return mandelbrot_numba(x_min, x_max, y_min, y_max, Nx, Ny, iterations)
    else:
        #  no valid input. Try again
        print("Please provide a proper \n function as first parameter, such as: numba, numpy or python")
        exit()

def draw(x_min, x_max, y_min, y_max, matrix, colorscale, dpi=1000):
    """
    plots the mandelbrot set given the rectangle on p, edges and colorscale.
    through plt.imshow()
    
    Arguments:
        x_min {float} -- edge value
        x_max {float} -- edge value
        y_min {float} -- edge value
        y_max {float} -- edge value
        matrix {2D numpy.array(dtype = int)} -- [description]
        colorscale {str} -- [description]
    
    Keyword Arguments:
        dpi {int} -- [optional, sets the plot's dpi] (default: {1000})
    """

    # plot with imshow()
    plt.figure(dpi=dpi)
    plt.imshow(matrix, cmap=colorscale,
               interpolation='gaussian',
               extent=[x_min, x_max, y_min, y_max])

    # name cordinates
    plt.xlabel('Re')
    plt.ylabel('Im')

def evaluate_args(args):
    """
    Casts system arg x_min, x_max, y_min, y_max to float,
    and Nx and Ny to int.
    
    Arguments:
        args {list} -- input args, where all values are strings
    
    Returns:
        list -- casted version of list
    """

    for i, arg in enumerate(args):
        if 2 <= i < 6:
            try:
                args[i] = (float(arg))
            except ValueError:
                print("{} is not a float!".format(arg))
                help()
        elif 5 <= i < 8:
            try:
                args[i] = int(arg)
            except ValueError:
                print("{} is not an int!".format(arg))
                help()
    return args[1:]


def help():
    """
    Prints out a  a helpful message explaining how to use mandelbrot.py
    """

    print("""Manual:
    This commandline script calculates the mandelbrot set within
    a given rectangle in the complex plane.
    
    Call:
    python3 {0} {1} {2} {3} {4} {5} {6} {7} {8} {9}

    Where:
    {0} \t->\t Name of file containing the script.\n
    {1} (str) \t->\t Function used to compute the mandelbrot set.
    \t\t\t\t Use one of: python, numpy, numba.\n
    {2}(float) \t->\t real value of the left edge of the rectangle.\n
    {3}(float) \t->\t real value of the right edge of the rectangle.\n
    {4}(float) \t->\t imag value of the bottom edge of the rectangle.\n
    {5}(float) \t->\t imag value of the top edge of the rectangle.\n
    {6}(int) \t->\t horizontal point count.\n
    {7}(int) \t->\t vertical point count.\n
    {8}(str) \t->\t color scale for the plot.
    \t\t\t\t Examples: magma, viridis, plasma.\n
    {9}(str) \t->\t output filename of the picture.\n


    """.format(os.path.basename(__file__), "function", "x_min", "x_max", "y_min", "y_max",
                                            "Nx", "Ny", "colorscale", "filename"))


if __name__ == "__main__":   
    # --help flag is used
    if len(argv) == 2 and argv[1] == "--help":
        help()
    # correct number of args
    elif len(argv) == 10:
        # cast int and float values from sys.argv
        args = evaluate_args(argv)
        menu(*args)
        
    # wrong number of args
    else:
        print("wrong number of arguments")
        help()
        2 25 53 

import highlighter from highlighter as lop
import True;
False
@Override #hello @Override

class python 
"hello"