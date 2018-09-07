from math import sqrt
import operator


class Complex:
    #z = a + ib
    def __init__(self, a = 0.0, b = 0):
        self._a = a
        self._b = b

    # Assignment 3.3
    def conjugate(self):
        return Complex(self._a, -self._b)

    def modulus(self):
        return (sqrt(self._a**2 + self._b**2))


    def __add__(self, other):
        return self.arithmetic_operation(other, operator.add)

    def __sub__(self, other):
        return self.arithmetic_operation(other, operator.sub)

    def __mul__(self, other):
        return self.arithmetic_operation(other, operator.mul)


    def __eq__(self, other):
        values = self.get_values(other)
        if values == None:
            return False
        if self._a == values[0] and self._b == values[1]:
            return True
        else:
            return False


    # Assignment 3.4
    def __radd__(self, other):
        return self.r_arithmetic_operation(other, operator.add)

    def __rsub__(self, other):
        return self.r_arithmetic_operation(other, operator.sub)

    def __rmul__(self, other):
        return self.r_arithmetic_operation(other, operator.mul)


    #assisting method
    def arithmetic_operation(self, other, operation):
        values = self.get_values(other)
        #raise error
        if values == None:
            self.unsupported_operand_types(other, operation)
        #multiply
        elif operation is operator.__mul__:
            return Complex((self._a * values[0] - self._b * values[1]),
                           (self._a * values[1] + self._b * values[0]))
        #add or sub
        else:
            return (Complex(operation(self._a, values[0]), operation(self._b, values[1])))

    def r_arithmetic_operation(self, other, operation):
        values = self.get_values(other)
        if values == None:
            self.unsupported_operand_types(other, operation)
        else:
            return Complex(*values).arithmetic_operation(self, operation)


    # Optional, possibly useful methods

    #toString

    #raises error when an unsupported operand is given
    def unsupported_operand_types(self, other, operation):
        instance = type(other).__name__
        if operation is operator.__add__:
            symbol = "+"
        elif operation is operator.__sub__:
            symbol = "-"
        else:
            symbol = "*"
        raise TypeError("unsupported operand type(s) for {}: Complex and '{}'".format(symbol, instance))

    #returns values
    def get_values(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return (other, 0)
        elif isinstance(other, complex):
            return (other.real, other.imag)
        elif isinstance(other, Complex):
            return (other._a, other._b)
        else:
            None

    # Allows you to write `-a`
    def __neg__(self):
        return Complex(-(self._a), -(self._b))

    # Make the `complex` function turn this into Python's version of a complex number
    def complex(self):
        return(self._a, self._b*1j)