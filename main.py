import math
import matplotlib.pyplot as plt
import numpy as np

def print_hi(name):
    print("Salut", name, "!")

def f(x):
    return x ** 3 - 3 * x ** 2 + 2 * x + 5

def moinsf(x):
    return -(x ** 3 - 3 * x ** 2 + 2 * x + 5)

minReel = 5 - 2 / (3 * math.sqrt(3))

# méthode par balayage à pas constant
def balayage_const(f, a, b, n):
    dx = (b-a)/n
    y = np.zeros(n+1)
    for i in range(n+1):
        y[i] = f(i * dx)
    return min(y)

def balayage_constMax(f, a, b, n):
    dx = (b-a)/n
    y = np.zeros(n+1)
    for i in range(n+1):
        y[i] = f(i * dx)
    return max(y)

# méthode par balayage aléatoire
def balayAleat(f, a, b, n):
    x = np.random.uniform(a, b, size=(n + 1, 1))
    y = []
    for i in x:
        y.append(f(i))
    return min(y)

def erreur(f, a, b, n):
    y = np.zeros(n+1)
    z = np.zeros(n+1)
    pas = np.linspace(1, n+1, n+1)
    for i in range(1,n+1):
        y[i] = balayage_const(f,a,b,i)-minReel
        z[i] = balayAleat(f,a,b,i)-minReel
    plt.plot(pas, z)
    plt.plot(pas, y)
    plt.show()

if __name__ == '__main__':
    N = 400
    print("cst: ", balayage_const(f,0,3,N))
    print(balayAleat(f, 0, 3, N))
    print("valeur max: ", balayage_constMax(f, 0, 3, N))

    erreur(f,0,3,N)

