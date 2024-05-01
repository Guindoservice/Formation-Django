"""
Ecrire un programme en langage Python qui demande à l’utilisateur de saisir un
nombre entier n et de lui afficher si ce nombre est carré parfait ou non.
"""
import math

n = input("Donner un nombre ")

try:

    # convertir en entier : deja fait si vous avez ecrit int(input("Donnez la valeur de a : "))
    n = int(n)

    racine = math.sqrt(n)

    partie_entiere = int(racine)

    if partie_entiere == racine:
        print(f"{n} est un carré parfait ")
    else:
        print(f"{n} n'est pas un carré parfait ")


except:
    print("Nombre invalide")