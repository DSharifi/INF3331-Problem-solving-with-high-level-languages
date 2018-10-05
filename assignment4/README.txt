4.5
How to use mandelbrot.py:
    Commandline

    Run mandelbrot.py with following system arguments (all required).
    python3 mandelbrot.py function x_min x_max y_min y_max Nx Ny colorscale filename

    Where:

    mandelbrot.py 	->	 Name of file containing the script.

    function (str) 	->	 Function used to compute the mandelbrot set.
                            Use one of: python, numpy, numba.

    x_min(float) 	->	 real value of the left edge of the rectangle.

    x_max(float) 	->	 real value of the right edge of the rectangle.

    y_min(float) 	->	 imag value of the bottom edge of the rectangle.

    y_max(float) 	->	 imag value of the top edge of the rectangle.

    Nx(int) 	->	 horizontal point count.

    Ny(int) 	->	 vertical point count.

    colorscale(str) 	->	 color scale for the plot.
    				 Examples: magma, viridis, plasma.

    filename(str) 	->	 output filename of the picture.

    example:
    ~ python3 mandelbrot.py numba -2.5 0.8 -1.25 1.25 10000 10000 viridis contest_image


4.6 -- 'test_mandelbrot.py'
test_complex.py contains a main method, which will start the unit testing of the
three different implementations to calculate mandelbrot.
To run the test: run 'python3 test_mandelbrot.py'


Installing package:
pip install .

