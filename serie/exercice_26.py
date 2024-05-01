"""
Ecrire un programme qui demande à l’utilisateur de saisir un texte et de lui
renvoyer tous les mots commençant par la lettre a.
"""

s = input("Donnez un e phrase : ")

# on transforme le text en tableau de mot

s_en_tablea_de_mot  = s.split(" ")

for mot in s_en_tablea_de_mot:
    if mot[0] == "a":
        print(mot)