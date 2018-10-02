from matplotlib import pyplot as plt
from math import pi, e, exp, cos, sin, tan
import numpy as np
import seaborn

i = 0
def myfunc(x):
    print("x = ", x)
    return x**2

def myfunx(x):
    print("x = ", x)


def myfuni(x, b):
    if x != 10:
        return 0
    return x


if __name__ == "__main__":
    vfunx = np.vectorize(myfuni)
    a = np.linspace(1, 10, 6)
    b = np.linspace(1, 5, 6)
    xv, yv = np.meshgrid(a, b)
    c = xv + yv*1j
    print(c)
    print("\n\n\n")
    d = vfunx(c, 10)
    print(d)


    # c = np.array([a, b])
    # print (c)
    # print (myfuni(c))
    
    # np.vectorize(np.vectorize(myfunx))(c)

    # twoFunx = np.vectorize(myfuni)

    # print("\n\n\n\n")

    # d = myfuni(c)

    # np.vectorize(np.vectorize(myfunx))(d)

    # #myfunx(d)
