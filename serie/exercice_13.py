"""
Ecrire un programme en langage Python qui demande à l’utilisateur de saisir
deux nombres entiers a et b et de lui afficher le quotient et le reste de la division
euclidienne de a par b.
"""

a = input("Donnez la valeur de a : ")
b = input("Donnez la valeur de b : ")

try:

    # convertir en entier : deja fait si vous avez ecrit int(input("Donnez la valeur de a : "))
    a = int(a)
    b = int(b)

    # le quotient
    q = int(a / b)

    # le reste avec %

    reste = a % b

    print(f"quotient = {q}")
    print(f"reste = {reste}")

except:
    print("Nombres invalide")