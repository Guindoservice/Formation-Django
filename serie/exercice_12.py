"""
1) – Ecrire un programme en Python qui demande à l’utilisateur de saisir un
nombre entier n et de lui afficher la table de multiplication de ce nombre.
2) – Améliorez le programme afin qu’il affiche les tables de multiplications de
tous les nombres compris entre 1 et 9
"""
import math

# On demande de saisir le un du cercle
n = input("Donnez un enier : ")


try:
    # Convertir n en nombre (en int)
    n = int(n)
    # 1)
    # for i in range(1, 11):
    #     print(f"{n} x {i} = {n*i}")

    # 2)
    for i in range(1, 11):
        print(f"Table de multiplication de {i}")
        for j in range(1, 11):
            print(f"{i} x {j} = {i*j}")
        print("\n")

except:
    print("nombre invalide")