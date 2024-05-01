"""
Ecrire un programme en Python qui demande à l’utilisateur de saisir un nombre
entier n et de lui afficher n !
"""

# On demande de saisir un nombre n
n = input("Donnez la valeur de n : ")


try:
    # Convertir n en nombre (en int)
    n = int(n)

    # Il est important de commencer par 1
    somme = 1
    for i in range(1, n+1):
        somme *= i
    print(f"{n}! = {somme}")

except:
    print("nombre invalide")