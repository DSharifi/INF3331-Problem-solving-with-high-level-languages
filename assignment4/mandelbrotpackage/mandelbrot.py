from .mandelbrot_1 import mandelbrot_python
from .mandelbrot_2 import mandelbrot_numpy
from .mandelbrot_3 import mandelbrot_numba
from matplotlib import pyplot as plt
import seaborn
import os
from sys import argv


def compute_mandelbrot(xmin, xmax, ymin, ymax, Nx, Ny, max_escape_time=1000, plot_filename=None, color_scale="magma"):
    """returns an Nx × Ny array of the escape times of evenly sampled points
        in the rectangle [xmin, xmax] × [ymin, ymax]. If plot filename is supplied,
        an image should be rendered and saved to the specified location
    
    Arguments:
        xmin {float} -- edge value
        xmax {float} -- edge value
        ymin {float} -- edge value
        ymax {float} -- edge value

        Nx {int} -- horizontal point count 
        Ny {int} -- vertical point count 

        filename {str} -- filename for output png file
        colorscale {str} -- Colorscale used to color the set
    
    Keyword Arguments:
        max_escape_time {int} -- iteration count for computation of mandelbrot (default: {1000})
        plot_filename {str} -- filename for output png file (default: {None})
        color_scale {str} --  Colorscale used to color the set (default: {"magma"})

    Returns:
        Nx × Ny array {int}
        Matrix representation of the mandelbrot set in the rectangle
    """
    dpi = 1000
    plots = "plots"
    if not os.path.exists(plots):
        os.makedirs(plots)

    # matrix representation of users rectangle
    matrix = mandelbrot_numba(
        xmin, xmax, ymin, ymax, Nx, Ny, max_escape_time)
    if plot_filename != None:
        # draw the rectangle
        draw(xmin, xmax, ymin, ymax, matrix, color_scale, dpi)
        # save drawn plt
        plt.savefig(plot_filename + ".png", dpi=dpi)
    return matrix

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
