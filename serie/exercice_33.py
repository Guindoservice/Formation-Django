"""
Ecrire un programme en Python qui demande à l’utilisateur de saisir une chaine
de caractères et d’afficher les caractères d’indice pair. Exemple pour la chaine s
= “Python”, le programme renvoie ‘Pto’.
"""

s = input("Donner une chaine : ")

les_mots_index_pair = ""

for i in range(len(s)):
    if i % 2 == 0:
        les_mots_index_pair += s[i]

print(les_mots_index_pair)