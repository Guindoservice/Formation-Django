"""
Ecrire un programme Python qui permet de regrouper dans une liste les mots
communs à deux chaines s1 et s2.
"""

s1 = input("Donnez la chaine s1 : ")
s2 = input("Donnez la chaine s2 : ")

s1_en_tableau_de_mot = s1.split(" ")
s2_en_tableau_de_mot = s2.split(" ")

liste_mot_commun = []

for mot in s2_en_tableau_de_mot:
    if mot in s1_en_tableau_de_mot:
        liste_mot_commun.append(mot)

print(liste_mot_commun)