from complex import Complex

def test_addition():
    w = Complex(2, -4)
    z = Complex(-9, 4)

    assert w+z == Complex(-7, 0)

def test_subtraction():
    z = Complex(4, -2)
    w = Complex(-1, -3)

    assert z-w == Complex(5, 1)

def test_modulus():
    #3 : 4: 5 triangle
    z = Complex(3, -4)
    assert z.modulus() == 5
    

def test_multiplication():
    z = Complex(-5, -9)
    w = Complex(-2, 7)
    k = Complex(73, -17)

    assert w*z == k



def test_conjugate():
    z = Complex(1, -2)
    assert z.conjugate() == Complex(1, 2)

def test_eq():
    z = Complex(1, -2)
    w = Complex(1, -2)
    k = Complex(3, 4)

    assert z == w
    assert z != k



def test_implemented_complex_addition():
    assert Complex(2,3) + (2+2j) == Complex(4,5)
    assert (2+2j) + Complex(2, 3) == Complex(4, 5)
    assert 23 + Complex(5, 3) == Complex(28, 3)

def main():
    test_addition()
    test_subtraction()
    test_conjugate()
    test_eq()
    test_modulus()
    test_multiplication() 
    test_implemented_complex_addition()




if __name__ == "__main__":
    main()