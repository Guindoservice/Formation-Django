"""
Ecrire un programme en Python qui demande à l’utilisateur de saisir un nombre
entier n et de lui afficher la valeur de la somme 1 + 2 + … + n = ?
"""
n = input("Donnez la valeur de n : ")

try:
    n = int(n)

    # methode 1
    somme = 0
    for i in range(n+1):
        somme += i
    print(f"La somme de  1 + 2 + … + {n} = {somme}")

    # methode 2
    # somme = sum([i for i in range(n+1)])
    # print(f"La somme de  1 + 2 + … + {n} = {somme}")


    # Methode 3
    # somme = (n * (n+1)) / 2
    # print(f"La somme de  1 + 2 + … + {n} = {somme}")


except:
    print("nombre invalide")