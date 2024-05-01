"""
Ecrire un programme en Python qui demande à l’utilisateur de saisir le rayon
d’un cercle et de lui renvoyer la surface et le périmètre.
"""
import math

# On demande de saisir le rayon du cercle
r = input("Donnez le rayon du cercle : ")


try:
    # Convertir n en nombre (en int)
    r = int(r)

    perimetre = 2 * math.pi * r

    surface = math.pi * r * r

    print(f"Le perimetre est {perimetre}")
    print(f"La surface est {surface}")


except:
    print("rayon invalide")