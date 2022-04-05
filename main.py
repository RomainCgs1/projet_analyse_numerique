
def print_hi(name):
    print("Salut", name, "!")

def f(x):
    return x**3-3*x**2+2*x+5

# méthode par balayage à pas constant
def balayage_const(a, b, N, f):
    liste=[]

    x=(a-b)/N
    for i in range (1, N+1):
        liste.append(f(i))
        print(f(i))
    r=min(liste)
    print(a, ',', b, ',', N, ',', x, ',', liste, ',', r)
    return x

# méthode par balayage aléatoire


if __name__ == '__main__':
    nom = input("Quel est ton nom ? ")
    nom = nom.title()
    print_hi(nom)
    balayage_const(1,3,6,f)