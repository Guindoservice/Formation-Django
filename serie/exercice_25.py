"""
Ecrire un programme qui demande à l’utilisateur de saisir un mot et de lui
renvoyer son inverse. Exemple si l’utilisateur saisi le mot python, le programme
lui renvoie nohtyp
"""

mot = input("Donnez un mot : ")

mot_inverse = "".join([mot[-(i+1)] for i in range(len(mot))])
print(mot_inverse)
