"""
Ecrire un programme en langage Python qui permet de parcourir et afficher les
caractères d’une variable du type chaine de caractères. Exemple pour s = «
Python », le programme affiche les caractères : P y t h o n

"""
# on lit un phrase (Ne met pas int(input(......)
s = input("Donnez un mot : ")

# convertir la chaine en liste
s_en_liste = [c for c in s]

# print(s_en_liste)

# converitir la liste en chaine
s_avec_espace = " ".join(s_en_liste)
print(s_avec_espace)
