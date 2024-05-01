"""
Ecrire un programme en Python qui demande à l’utilisateur de saisir un nombre
entier n et de lui afficher tous les diviseurs de ce nombre.
"""

# On demande de saisir le un du cercle
n = input("Donnez un enier : ")


try:
    # Convertir n en nombre (en int)
    n = int(n)
    for i in range(1, n+1):
        if n % i == 0:
            print(i)


except:
    print("nombre invalide")