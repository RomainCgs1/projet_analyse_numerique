import math
from random import random

import numpy as np
from numpy import transpose as tr
import numpy.linalg as lng


def phi(A, y, b):
    return tr(y) * A * y - 2 * tr(y) * b


def g(A, y, b):
    return 2 * (np.dot(A, y) - b)


def norme(M):
    return lng.norm(M)


def matrInv(eups, m, A, b, n, y0):
    yK = y0
    yK1 = np.zeros(n)
    i = 0
    while norme(yK1 - yK) > eups and i < m:
        G = g(A, yK, b)
        if G.all() == 0:
            rhok = 0
        else:
            nom = norme(G) ** 2
            denom = 2 * np.dot(np.dot(G, A), G)
            rhok = nom / denom
        yK1, yK = yK - rhok * G, yK1
        i += 1
    return yK1


def q2(A, b, y0, n):
    y = matrInv(10 ** (-5), 120, A, b, n, y0)
    return y

def q3():
    n = int(input("Donner une valeur pour n : "))
    A = np.diag(2 * np.ones(n)) + np.diag(6 * np.ones(n - 1), -1) + np.diag(6 * np.ones(n - 1), 1)
    b = [int(random() * 100) for i in range(n)]
    y0 = [int(random() * 100) for i in range(n)]
    y = q2(A, b, y0, n)
    print(y)


if __name__ == "__main__":
    q3()
