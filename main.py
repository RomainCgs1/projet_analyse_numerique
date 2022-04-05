import math

import numpy as np

def print_hi(name):
    print("Salut", name, "!")

def f(x):
    return x**3 - 3*x**2 + 2*x + 5

minReel = 5 - 2/(3*math.sqrt(3))

# méthode par balayage à pas constant
def balayage_const(a, b, N, f):
    liste=[]
    x=[]
    pas=(b-a)/N
    for k in range(N+1):
        x.append(a)
        a=a+pas
    print('x = ', x)
    #x=np.arange(a,b,pas)
    for i in x:
        liste.append(f(i))
        #print(f(i))
    r=min(liste)
    print('a = ', a, '\nb = ', b, '\nN = ', N, '\nliste = ', liste, '\nr = ', r)
    return r

# méthode par balayage aléatoire
def balayAleat(f, a, b, n):
    x = np.random.uniform(a, b, size=(n+1, 1))
    y = []
    for i in x:
        y.append(f(i))
    return min(y)

if __name__ == '__main__':
    #nom = input("Quel est ton nom ? ")
    #nom = nom.title()
    #print_hi(nom)
    balayage_const(0,3,6,f)
    print(balayAleat(f, 0, 3, 30))
