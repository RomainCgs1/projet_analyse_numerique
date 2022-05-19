import math
import random
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

def f(x):
    return x ** 3 - 3 * x ** 2 + 2 * x + 5

def moinsf(x):
    return -(x ** 3 - 3 * x ** 2 + 2 * x + 5)

def derivF(x):
    dF = 3 * x ** 2 - 6 * x + 2
    return dF

def grad(x, y, dfx, dfy):
    return (dfx(x, y), dfy(x, y))

def norme(vect):
    r = 0
    for a in vect:
        r += a**2
    return math.sqrt(r)


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

def g(x, y):
    return (x ** 2) / 2 + (y ** 2) / (2/7)

def dgx(x, y):
    return 2 * x / 2

def dgy(x, y):
    return 2 * y / (2/7)

def h(x, y):
    return np.cos(x) * np.sin(y)

def dhx(x, y):
    return - math.sin(x) * math.sin(y)

def dhy(x, y):
    return math.cos(x) * math.cos(y)

def figure3D(f):
    ax = Axes3D(plt.figure())
    f = np.vectorize(f)
    X = np.arange(-8, 8, 0.01)
    Y = np.arange(-8, 8, 0.01)
    X, Y = np.meshgrid(X, Y)
    Z = f(X, Y)
    ax.plot_surface(X, Y, Z)

def courbeNiveau(f):
    f = np.vectorize(f)
    X = np.arange(-2, 2, 0.01)
    Y = np.arange(-2, 2, 0.01)
    X, Y = np.meshgrid(X, Y)
    Z = f(X, Y)
    plt.axis('auto')
    plt.contour(X, Y, Z, [0.1, 0.4, 0.5])
    plt.show()

def gradpc(eps, m, u, x0, y0, df1, df2, f):
    a = [(x0, y0)]
    i = 0
    while i < m and norme(grad(a[i][0], a[i][1], df1, df2)) >= eps:
        x = a[i-1][0]
        y = a[i-1][1]
        #print(i)
        x1 = x + u*grad(x, y, df1, df2)[0]
        y1 = y + u*grad(x, y, df1, df2)[1]
        a.append((x1, y1))
        i += 1

    ax = plt.axes(projection='3d')
    X = [A[0] for A in a]
    Y = [A[1] for A in a]
    Z = [f(x, y) for (x, y) in a]
    plt.axis('auto')
    ax.scatter3D(X, Y, Z, c=Z)
    #figure3D(f)
    courbeNiveau(f)
    plt.show()


#def gradamax(eps, m, u, x0, y0, f, df1, df2):


#def gradamin(eps, m, u, x0, y0, f, df1, df2):


if __name__ == '__main__':
    n = 400 #nombre d'intervalles
    #print("Minimum de la fonction entre 0 et 3 :")
    #print("Balayage à pas constant : ", balayage_const(f, 0, 3, n))
    #print("Balayage aléatoire : ", float(balayAleat(f, 0, 3, n)))

    #balayage_const(f, 0, 3, n)
    #balayAleat(f, 0, 3, n)
    #erreur(f, 0, 3, n)

    #print("Valeur max: ", -1*balayAleat(moinsf, -1, 2, n))

    nGrad = 30
    u = -0.1
    print("Min via gradient : ", methodeDuGradient(f, derivF, 0, 1, u, nGrad))

    #figure3D(h)
    #courbeNiveau(h)

    # gradpc(10**(-5), 120, -0.2, 0, 0, dhx, dhy, h)
    #gradpc(10 ** (-5), 120, -0.05, 7, 1.5, dgx, dgy, g)