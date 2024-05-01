"""
Ecrire un programme en Python qui demande à l’utilisateur de saisir une chaine
de caractère s et de lui renvoyer un message indiquant si la chaine contient la
lettre ‘a’ tout en indiquant sa position sur la chaine. Exemple si l’utilisateur tape
la chaine s = ‘langage’ le programme lui renvoie : La lettre ‘a’ se trouve à la
position : 1 La lettre ‘a’ se trouve à la position : 4
"""

s = input("Donnez une phrase : ")

possition = s.find("a")

if possition != -1:
    print(f"a se trouve dans la chaine à l'index {possition}")
else:
    print(f"a ne se trouve pas dans la chaine")

