"""
Ecrire un programme en Python qui demande à l’utilisateur de saisir deux
nombres a et b et de lui afficher leur somme : a + b
"""

a = input("Donnez la valeur de a : ")
b = input("Donnez la valeur de b : ")

try:
    a = int(a) # ou faire int(input("Donnez la valeur de a : "))
    b = int(b) # idem
    somme = a + b
    print(f"La somme de {a} et {b} est {somme}")

except:
    print("Nombre invalide")