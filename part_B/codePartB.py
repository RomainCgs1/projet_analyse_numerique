import math
import numpy as np
from matplotlib import pyplot as plt
import random


def f(x):
    return x ** 3 - 3 * x ** 2 + 2 * x + 5


def moinsf(x):
    return -1 * f(x)

def derivF(x):
    dF = 3 * x ** 2 - 6 * x + 2
    return dF

minReel = 5 - 2 / (3 * math.sqrt(3))
maxReel = 5 + 2 / (3 * math.sqrt(3))


# méthode par balayage à pas constant
def balayage_const(f, a, b, n):
    dx = (b - a) / n
    y = np.zeros(n + 1)
    for i in range(n + 1):
        y[i] = f(a + i * dx)
    return min(y)


# méthode par balayage aléatoire
def balayAleat(f, a, b, n):
    x = np.random.uniform(a, b, size=(n + 1, 1))
    y = []
    for i in x:
        y.append(f(i))
    return float(min(y))


def erreur(f, a, b, n):
    y = np.zeros(n + 1)
    z = np.zeros(n + 1)
    pas = np.linspace(1, n + 1, n + 1)
    for i in range(1, n + 1):
        y[i] = balayage_const(f, a, b, i) - minReel
        z[i] = balayAleat(f, a, b, i) - minReel
    plt.plot(pas, z)
    plt.plot(pas, y)
    plt.show()

def methodeDuGradient(f, df, a, b, u, n):
    x = random.uniform(a, b)
    for i in range(n):
        x = x + u * df(x)
    return f(x)


def q2(n):
    print("Minimum de la fonction entre 0 et 3 :")
    print("Balayage à pas constant : ", balayage_const(f, 0, 3, n))
    print("Balayage aléatoire : ", float(balayAleat(f, 0, 3, n)))


def q3(n):
    erreur(f, 0, 3, n)


def q4(n):
    print("Maximum de la fonction :")
    print(-1 * balayage_const(moinsf, -1, 1, n))


def q6(nGrad):
    u = -0.1
    print("Min de f avec le gradient 1D à pas constant en", nGrad, "itérations :", methodeDuGradient(f, derivF, 0, 1, u, nGrad))


if __name__ == '__main__':
    q = int(input("Quelle question voulez vous tester (2, 3, 4 ou 6) ? "))
    if 2 <= q <= 4:
        n = int(input("Combien d'intervalles ? "))
        if q == 2:
            q2(n)
        elif q == 3:
            q3(n)
        elif q == 4:
            q4(n)
    elif q == 6:
        n = int(input("Combien d'itérations ? "))
        q6(n)
    else:
        print("Question non trouvée")

