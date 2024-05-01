"""
Ecrire un programme en langage Python, qui permet de compter le nombre de
voyelles dans une chaine donnée. Exemple pour la chaine s=
‘anticonstitutionellement’ le programme doit renvoyer le message suivant : La
chaine anticonstitutionellement possède 10 voyelles.
"""

s = input("Donnez un chaine : ")

les_voyelles = ["a","e","i","u","o","y"]
nombre_de_voyelle = 0

for lettre in s:
    if lettre in les_voyelles:
        nombre_de_voyelle += 1

print(f"La chaine {s} contient {nombre_de_voyelle} voyelles")
