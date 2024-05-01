"""
Ecrire un programme en Python qui demande à l’utilisateur de saisir 3 nombres
x, y et z et de lui afficher leur maximum.
"""

a = input("Donnez la valeur de a : ")
b = input("Donnez la valeur de b : ")
c = input("Donnez la valeur de c : ")

try:
    a = int(a)
    b = int(b)
    c = int(c)


    if a > b and a > c:
        print(f"Le maximum de {a}, {b} et {c} est {a}")
    elif b > a and b > c:
        print(f"Le maximum de {a}, {b} et {c} est {b}")
    else:
        print(f"Le maximum de {a}, {b} et {c} est {c}")


except:
    print("Nombres invalide")
