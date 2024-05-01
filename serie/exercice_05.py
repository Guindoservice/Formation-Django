"""
Ecrire un programme en langage Python qui demande à l’utilisateur de saisir un
nombre entier et de lui afficher si ce nombre est pair ou impair.
"""
n = input("Donnez un nombre : ")


try:
    n = int(n)
    if n % 2 == 0: # si le rest de la division par 2 est 0
        print(f"Le nombre {n} esst Pair")
    else:
        print(f"Le nombre {n} esst Impair")
except:
    print("Nombres invalide")