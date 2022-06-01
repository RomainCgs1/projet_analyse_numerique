from matplotlib import pyplot as plt

from part_D import codePartD
import numpy.linalg as alg
import numpy as np


def ajoutCI(a, b, V):
    V = list(V)
    V.insert(0, a)
    V.append(b)
    return V


def q1(n, a, b):
    An = np.diag(2 * np.ones(n), 0) + np.diag(-1 * np.ones(n - 1), -1) + np.diag(-1 * np.ones(n - 1), 1)
    Yn = np.zeros(n)
    Yn[0] = a
    Yn[-1] = b

    eups = 10 ** (-5)
    m = 120
    y0 = np.ones(n)

    dx = 1 / (n + 1)
    Tn = codePartD.matrInv(eups, m, An, Yn, n, y0)
    Tn = ajoutCI(a, b, Tn)
    print('Calcul : ', Tn)

    x = [i * dx for i in range(1, n + 1)]
    x = ajoutCI(0, 1, x)

    approx = alg.solve(An, Yn)
    approx = ajoutCI(a, b, approx)
    print("Approximation de np :", approx)

    plt.plot(x, approx, marker="+")
    plt.plot(x, Tn)
    plt.show()


def q2(n, a, b):
    An = np.diag(2 * np.ones(n), 0) + np.diag(-1 * np.ones(n - 1), -1) + np.diag(-1 * np.ones(n - 1), 1)
    Yn = np.zeros(n)
    Yn[0] = a
    Yn[-1] = b

    eups = 10 ** (-5)
    m = 120
    y0 = np.ones(n)

    dx = 1 / (n + 1)
    bn = 1 / (dx ** 2) * Yn + 3000 * np.ones(n)
    Xn = 1 / (dx ** 2) * An + np.diag(10 * np.ones(n), 0)
    Tn = codePartD.matrInv(eups, m, Xn, bn, n, y0)

    x = [i * dx for i in range(1, n + 1)]
    x = ajoutCI(0, 1, x)

    approx = list(alg.solve(Xn, bn))
    approx = ajoutCI(a, b, approx)
    Tn = ajoutCI(a, b, Tn)

    plt.plot(x, approx, marker="+")
    plt.plot(x, Tn)
    plt.show()


def questions():
    q = int(input("Quelle question voulez vous tester (1 ou 2) ? "))
    n = int(input("Combien d'intervalles ? "))
    a = 500
    b = 350
    if q == 1:
        q1(n, a, b)
    elif q == 2:
        q2(n, a, b)
    else:
        print("Question non trouvée")


if __name__ == "__main__":
    questions()
