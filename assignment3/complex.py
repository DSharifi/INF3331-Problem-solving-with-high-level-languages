from math import sqrt
import operator


class Complex:
    """
    This module is an implementation of complex numbers.
    """

    def __init__(self, real = 0, imag = 0):
        """
        Default constructor for Complex.
        
        Arguments:
            real: First parameter (optional). Supported types: int, float.
            imag: Second parameter (optional). Supported types: int, float.
        
        Implementation:
            set self.real = real, and self.imag
        
        Returns:
            Complex(real, imag)
        """
    
        self.real = real
        self.imag = imag

    # Assignment 3.3
    def conjugate(self):
        """
        Returns:
            Returns Complex conjugate of self. 

        Implementation:
            Creates a new Complex with a negated imaginary part.
            Complex(3, -4).conjugate() == Complex(3, 4)
        """
        return Complex(self.real, -self.imag)

    def modulus(self):
        """
        Returns:
            self's modulus as a float.
        
        Implementation:
            For any Complex z, where z = Complex(a, b)
            >>> z.modulus()
            sqrt(a**2 + b**2)
        """

        return sqrt(self.imag**2 + self.real**2)

    def __add__(self, other):
        """
        Arguments:
            other: First parameter. Supported types: int, float, complex and Complex

        Returns:
            Returns the sum of self added by other, as a Complex.

        Raises:
            TypeError: if an unsupported type is given as first argument.

        Implementation:
            The sum is calculated by self._arithmetic_operation(other, operator.mul), 
            which does the heavy lifting by calculating the output.
        """

        return self._arithmetic_operation(other, operator.add)

    def __sub__(self, other):
        """
        Arguments:
            other: First parameter. Supported types: int, float, complex and Complex

        Returns:
            Returns the remainder of self subtracted by other, as a Complex.

        Raises:
            TypeError: if an unsupported type is given as first argument.

        Implementation:
            The difference is calculated by self._arithmetic_operation(other, operator.mul), which 
            does the heavy lifting by calculating the output.
        """

        return self._arithmetic_operation(other, operator.sub)

    def __mul__(self, other):
        """
        mul operator for Complex.
        Arguments:
            other: First parameter. Supported types: int, float, complex and Complex

        Returns:
            Returns the product of self multiplied by other, as a Complex.

        Raises:
            TypeError: if an unsupported type is given as first argument.

        Implementation:
            The product is calculated by self._arithmetic_operation(other, operator.mul), which 
            does the heavy lifting by calculating the output.
        """
        return self._arithmetic_operation(other, operator.mul)

    def __eq__(self, other):
        """
        Arguments:
            other: First parameter. Supported types: int, float, complex and Complex

        Return type: 
            boolean: True for equalness, False otherwise.

        Implementation:
            Checks whether the real and imaginary part of both self and other are equal.
            If they are it will return True, else False.
            This function will always return False if an unsupported argument is given.
        """
        #if its a non supported operand
        if not self._is_supported_operand(other):
            return False
        #self and other are equal
        if self.real == other.real and self.imag == other.imag:
            return True
        else:
            return False

    def __str__(self):
        """ 
        return value: 
            string: self formatted as a string.

        Implementation:
            Returns a string interpretation of self. "'real' + 'imag'i".
            The multipliers of either is stripped if it is equal to 0.
            Imaginay is also formatted just as 'i', if it is equal to 1.
        """
        #base case
        if self.imag == 0: 
            return str(self.real)

        imag, symbol = abs(self.imag), ""
        if imag == 1: imag = ""
        if self.imag < 0: symbol = "-"
        if self.real == 0:
            return symbol+str(imag)+"i"
        
        if self.imag > 0:
            symbol = "+"
        return str(self.real) + symbol + str(imag)+"i"


    # Assignment 3.4
    def __radd__(self, other):
        """
        Arguments:
            other: First parameter. Supported types: int, float, complex.

        Returns:
            Returns the sum of other added by self, as a Complex.

        Raises:
            TypeError: if an unsupported type is given as first argument.

        Implementation:
            The sum is calculated by r_self._arithmetic_operation(other, operator.add), which 
            does the heavy lifting by calculating the output.
        """
        return self._r_arithmetic_operation(other, operator.add)

    def __rsub__(self, other):
        """
        Arguments:
            other: First parameter. Supported types: int, float, and complex.

        Returns:
            Returns the remainder of other subtracted by self, as a Complex.

        Raises:
            TypeError: if an unsupported type is given as first argument.

        Implementation:
            The difference is calculated by r_arithmetic_operation(other, operator.sub), which 
            does the heavy lifting by calculating the output.
        """
        return self._r_arithmetic_operation(other, operator.sub)

    def __rmul__(self, other):
        """
        Arguments:
            other: First argument. Supported types: int, float, complex.

        Returns:
            Returns the product of other multiplied by self, as a Complex.

        Raises:
            TypeError: if an unsupported type is given as first argument.

        Implementation:
            The product is calculated by self._arithmetic_operation(other, operator.mul), which 
            does the heavy lifting by calculating the output.
        """
        return self._r_arithmetic_operation(other, operator.mul)


    #assisting method
    def _arithmetic_operation(self, other, operation):
        """
        Higher order proccedure, assisting __add__, __sub__, __mul__.

        Arguments:
            other: First argument. Supported types: int, float, complex and Complex.
            operation:  Second argument. Supported functions: add, sub and mul. 
        
        Implementation:
            Check if other is a supported operand. (self._is_supported_operand()). If other is
            unsupported, a TypeError will be raised.

            Returns the result of performing the operation, operation self on other.

            proccedure for add and sub:
            z = a + bi
            w = c + di
            
            k = z + w
            k == (a + c) + (b + d)i

            y = z - w
            y == (a - c) + (b - d)i

            proccedure for mul:
            z = a + bi
            w = c + di
            k = z * w

            k == (a*c - b*d) + (a*d + b*d)i

        
        Raises:
            TypeError: If other is an unsupported type.
        """

        #raise error if other is not supported
        if not self._is_supported_operand(other):
            self._unsupported_operand_types(other, operation)
       
        #multiply
        elif operation is operator.__mul__:
            return Complex(self.real * other.real - self.imag * other.imag,
                           self.real * other.imag + self.imag * other.real)
        #add or sub
        else:
            return Complex(operation(self.real, other.real), operation(self.imag, other.imag))

    def _r_arithmetic_operation(self, other, operation):
        """
        Higher order assisting proccedure for __radd__, __rsub__, __rmul__.

        Arguments:
            other: First argument. Supported types: int, float, complex and Complex.
            operation:  Second argument. Supported functions: add, sub, mul. 
        
        Implementation:
            Returns the result of performing arithmetic_operationration() other on self.

        Raises:
            TypeError: if an unsupported type is given as first argument. 
        """
        if not self._is_supported_operand(other):
            self._unsupported_operand_types(other, operation)
        else:
            return Complex(other.real, other.imag)._arithmetic_operation(self, operation)

    # Optional, possibly useful methods
    def _unsupported_operand_types(self, other, operation):
        """
        Function used to raise a TypeError if an unsupported operand is used in an arithmetic expression.
        The function should only be used if it is asserted that the operand is not supported.  
        
        Arguments:
            other: first argument: Supported types: any operand
            (the unsupported operand)

            operation: second argument: Supported types: __add__, __sub__, __mul__.
            (the operator used, raising the TypeError)

        Implementation:
            if, elif else block is used to get operation's operator symbol (+, - or *).
            type of other is retrieved with type(other).__name__. 
            raise TypeError with an explanation string.

        Raises:
            TypeError("unsupported operand type(s) for {}: Complex and '{}'".format(symbol, instance)).

        """

        instance = type(other).__name__
        if operation is operator.__add__:
            symbol = "+"
        elif operation is operator.__sub__:
            symbol = "-"
        else:
            symbol = "*"
        raise TypeError("unsupported operand type(s) for {}: Complex and '{}'".format(symbol, instance))

    #returns values
    def _is_supported_operand(self, other):
        """
        Check whether other is a supported operand for Complex in arithmetic operations. 
        Arguments:
            other: First parameter: Supported types: int, float, complex and Complex 
            can be used to 
        
        Returns:
            boolean: True if the operand is supported, False if not.
        
        Implementation:
            The test is done by using isinstance on (int, float, complex and Complex).
        """
        #supported operand
        if isinstance(other, (int, float, complex, Complex)):
            return True
        #unsupported operand
        else:
            return False


    # Allows you to write `-a`
    def __neg__(self):
        """
        Returns negated version of the Complex, by creating
        a new complex with negated values of real and imaginary part of self.
        """
        return Complex(-(self.real), -(self.imag))

    # Make the `complex` function turn this into Python's version of a complex number
    def __complex__(self):
        """
        Returns complex version of Complex. 
        """
        return(self.real + self.imag*1j)