from random import random

from matplotlib import pyplot as plt

from part_D import codePartD
import numpy.linalg as alg
import numpy as np

def q1(n, a, b):
    An = np.diag(2*np.ones(n), 0) + np.diag(-1*np.ones(n-1), -1) + np.diag(-1*np.ones(n-1), 1)
    Yn = np.zeros(n)
    Yn[0] = a
    Yn[-1] = b
    eups = 10**(-5)
    m = 120
    y0 = np.ones(n)


    dx = 1 / (n + 1)
    approx = alg.solve(An, Yn)
    print("Approx de np :", approx)
    x = [i*dx for i in range(1, n+1)]
    #plt.plot(x, approx)
    #plt.show()


    Tn = codePartD.matrInv(eups, m, An, Yn, n, [int(random() * 100) for i in range(n)])
    print(Tn)

if __name__ == "__main__":
    q1(2, 500, 350)