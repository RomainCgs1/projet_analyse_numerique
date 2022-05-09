import math
import random

import matplotlib.pyplot as plt
import numpy as np


def print_hi(name):
    print("Salut", name, "!")


def f(x):
    return x ** 3 - 3 * x ** 2 + 2 * x + 5


def moinsf(x):
    return -(x ** 3 - 3 * x ** 2 + 2 * x + 5)

def derivF(x):
    return 3 * x ** 2 - 6 * x + 2

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

if __name__ == '__main__':
    n = 400 #nombre d'intervalles
    print("Minimum de la fonction entre 0 et 3 :")
    print("Balayage à pas constant : ", balayage_const(f, 0, 3, n))
    print("Balayage aléatoire : ", float(balayAleat(f, 0, 3, n)))

    #erreur(f, 0, 3, N)


    print("valeur max: ", -1*balayAleat(moinsf, -1, 2, n))

    nGrad = 30
    u = -0.1
    print("Min via gradient : ", methodeDuGradient(f, derivF, 0, 1, u, nGrad))