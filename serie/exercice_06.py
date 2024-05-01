"""
Ecrire un programme en langage Python qui demande à l’utilisateur de saisir son
âge et de lui afficher le message « vous êtes Majeur ! » si l’âge tapé est
supérieur ou égale à 18 et le message « vous êtes mineur ! » si l’âge tapé est
inférieur à 18
"""

age = input("Donnez votre âge : ")

try:
    age = int(age)
    if age >= 0:
        print("vous êtes Majeur !")
    else:
        print("vous êtes mineur ! »")
except:
    print("âge invalide")