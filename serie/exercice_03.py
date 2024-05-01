"""
Ecrire un programme en Python qui demande à l’utilisateur de saisir deux
nombres a et b et de lui afficher leur maximum.
"""

a = input("Donnez la valeur de a : ")
b = input("Donnez la valeur de b : ")

try:

    # convertir en entier : deja fait si vous avez ecrit int(input("Donnez la valeur de a : "))
    a = int(a)
    b = int(b)

    # Methode 1
    if a > b :
        print(f"{a} est plsu grand que {b}")
    else:
        print(f"{b} est plsu grand que {a}")

    # methode 2
    # print(f"Le maximum de {a} et {b} est {a if a > b else b}")

except:
    print("Nombres invalide")