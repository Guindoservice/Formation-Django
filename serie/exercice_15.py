"""
Ecrire un programme en langage Python qui demande à l’utilisateur de saisir un
nombre entier n et de lui afficher si ce nombre est premier ou non.
"""
n = input("Donner un nombre : ")


try:

    # convertir en entier : deja fait si vous avez ecrit int(input("Donnez la valeur de a : "))
    n = int(n)

    # on compte le nombre de diviseur
    nombre_diviseur = 0
    for i in range(1,n+1):
        if n % i == 0:
            nombre_diviseur += 1

    if nombre_diviseur == 2:
        print(f"{n} est un nombre premier ")
    else:
        print(f"{n} n'est pas un un nombre premier ")


except:
    print("Nombre invalide")