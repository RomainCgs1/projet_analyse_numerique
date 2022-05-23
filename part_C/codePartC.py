import math

import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class G:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def g(self, x, y):
        return (x ** 2) / self.a + (y ** 2) / self.b

    def dgx(self, x, y):
        return 2 * x / self.a

    def dgy(self, x, y):
        return 2 * y / self.b


def h(x, y):
    return np.cos(x) * np.sin(y)


def dhx(x, y):
    return - math.sin(x) * math.sin(y)


def dhy(x, y):
    return math.cos(x) * math.cos(y)

def norme(vect):
    r = 0
    for a in vect:
        r += a ** 2
    return math.sqrt(r)

def grad(x, y, dfx, dfy):
    return (dfx(x, y), dfy(x, y))

def figure3D(f):
    ax = Axes3D(plt.figure())
    f = np.vectorize(f)
    X = np.arange(-8, 8, 0.01)
    Y = np.arange(-8, 8, 0.01)
    X, Y = np.meshgrid(X, Y)
    Z = f(X, Y)
    ax.plot_surface(X, Y, Z)

def courbeNiveau(f, ymin, ymax):
    f = np.vectorize(f)
    X = np.arange(-7, 7, 0.01)
    Y = np.arange(-7, 7, 0.01)
    X, Y = np.meshgrid(X, Y)
    Z = f(X, Y)
    plt.axis('auto')
    courbesNiv = np.linspace(ymin, ymax, 10)
    plt.contour(X, Y, Z, courbesNiv)
    plt.show()

def gradpc(eps, m, u, x0, y0, f, df1, df2, graph):
    a = [(x0, y0)]
    i = 0
    while i < m and norme(grad(a[i][0], a[i][1], df1, df2)) >= eps:
        x = a[i - 1][0]
        y = a[i - 1][1]
        # print(i)
        x1 = x + u * grad(x, y, df1, df2)[0]
        y1 = y + u * grad(x, y, df1, df2)[1]
        a.append((x1, y1))
        i += 1

    Z = [f(x, y) for (x, y) in a]

    if graph :
        ax = plt.axes(projection='3d')
        X = [A[0] for A in a]
        Y = [A[1] for A in a]
        plt.axis('auto')
        ax.scatter3D(X, Y, Z, c=Z)
        # figure3D(f)
        courbeNiveau(f, f(X[-1], Y[-1]), f(X[0], Y[0]))
        plt.show()
    return min(Z)

def erreurAbsolueG(eps, m, umin, umax, x0, y0, f, df1, df2):
    ea = []
    linU = np.linspace(umin, umax, 300)
    for u in linU:
        ea.append(gradpc(eps, m, u, x0, y0, f, df1, df2, False))
    plt.plot(linU,ea)
    plt.show()


def gradamax(eps, m, u, x0, y0, f, df1, df2, graph):
    if u < 0:
        u = -u
    a = [(x0, y0)]
    i = 0
    while i < m and norme(grad(a[i][0], a[i][1], df1, df2)) >= eps:
        x = a[i - 1][0]
        y = a[i - 1][1]
        F2 = 2
        F1 = 1
        k = 0
        print(i)
        while F2 > F1 and k<m:
            k += 1
            X1 = x + k * u * df1(x, y)
            Y1 = y + k * u * df2(x, y)
            F1 = f(X1, Y1)

            X2 = x + (k+1) * u * grad(x, y, df1, df2)[0]
            Y2 = y + (k+1) * u * grad(x, y, df1, df2)[1]
            F2 = f(X2, Y2)

        xn = x + k * u * grad(x, y, df1, df2)[0]
        yn = y + k * u * grad(x, y, df1, df2)[1]
        a.append((xn, yn))
        i += 1

    ax = plt.axes(projection='3d')
    X = [A[0] for A in a]
    Y = [A[1] for A in a]

    Z = [f(x, y) for (x, y) in a]

    if graph:
        plt.axis('auto')
        ax.scatter3D(X, Y, Z, c=Z)
        yMin = min(f(X[-1], Y[-1]), f(X[0], Y[0]))
        yMax = max(f(X[-1], Y[-1]), f(X[0], Y[0]))
        courbeNiveau(f, yMin, yMax)
        plt.show()
    return max(Z), i

def gradamin(eps, m, u, x0, y0, f, df1, df2, graph):
    a = [(x0, y0)]
    i = 0
    while i < m and norme(grad(a[i][0], a[i][1], df1, df2)) >= eps:
        x = a[i - 1][0]
        y = a[i - 1][1]
        # print(i)
        F2 = 1
        F1 = 2
        k = 0
        while F2 < F1:
            k += 1
            X1 = x + k * u * df1(x, y)
            Y1 = y + k * u * df2(x, y)
            F1 = f(X1, Y1)

            X2 = x + (k + 1) * u * grad(x, y, df1, df2)[0]
            Y2 = y + (k + 1) * u * grad(x, y, df1, df2)[1]
            F2 = f(X2, Y2)
            print(k)

        xn = x + k * u * grad(x, y, df1, df2)[0]
        yn = y + k * u * grad(x, y, df1, df2)[1]
        a.append((xn, yn))
        i += 1

    ax = plt.axes(projection='3d')
    X = [A[0] for A in a]
    Y = [A[1] for A in a]

    Z = [f(x, y) for (x, y) in a]

    if graph:
        plt.axis('auto')
        ax.scatter3D(X, Y, Z, c=Z)
        yMin = min(f(X[-1], Y[-1]), f(X[0], Y[0]))
        yMax = max(f(X[-1], Y[-1]), f(X[0], Y[0]))
        if(yMin == yMax):
            yMin -= 2
            yMax += 2
        courbeNiveau(f, yMin, yMax)
        plt.show()
    return min(Z), i

def grada_iterations(eps, m, umin, umax, x0, y0, f, df1, df2, max):
    linU = np.linspace(umin, umax, 20)
    nbIter = []
    for u in linU:
        if max:
            nbIter.append(gradamax(eps, m, u, x0, y0, f, df1, df2, False)[1])
        else:
            nbIter.append(gradamin(eps, m, u, x0, y0, f, df1, df2, False)[1])
    div = True
    for n in nbIter:
        if n != m:
            div = False
    if div:
        print("La méthode du gradient ne converge pas. La fonction semple ne pas avoir l'extremum demandé.")
    plt.axis('auto')
    plt.plot(linU, nbIter)
    plt.show()

def q2():
    fct = input("Fonction g ou h ? g/h ")
    if fct == 'g':
        f = G(2, 2/7).g
    elif fct == 'h':
        f = h
    figure3D(f)
    courbeNiveau(f, -1, 1)  # invisible si la figure 3D est affichée

def q6():
    fct = input("Fonction g ou h ? g/h ")
    if fct == 'g':
        F = G(2, 2 / 7)
        f = F.g
        x0, y0 = 7, 1.5
        dfx = F.dgx
        dfy = F.dgy
    elif fct == 'h':
        f = h
        x0, y0 = 0, 0
        dfx = dhx
        dfy = dhy

    eups = 10**(-5)
    m = 120
    u = -0.2
    gradpc(eups, m, u, x0, y0, f, dfx, dfy, True)


def q7():
    F = G(1, 20)
    erreurAbsolueG(10 ** (-5), 120, -0.99, -0.001, 7, 1.5, F.g, F.dgx, F.dgy)

def q8():
    gradamax(10 ** (-5), 120, 0.2, 0, 0, h, dhx, dhy, True)

def q9():
    gradamin(10 ** (-5), 120, -0.2, 0, 0, h, dhx, dhy, True)

def q10():
    F = G(1, 20)
    grada_iterations(10 ** (-5), 120, -0.999, 0.001, 7, 1.5, F.g, F.dgx, F.dgy, True)
    grada_iterations(10 ** (-5), 120, -0.999, 0.001, 7, 1.5, F.g, F.dgx, F.dgy, False)

if __name__ == '__main__':
    q10()
