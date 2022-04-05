
def print_hi(name):
    print("Salut", name, "!")

if __name__ == '__main__':
    nom = input("Quel est ton nom ? ")
    nom = nom.title()
    print_hi(nom)
