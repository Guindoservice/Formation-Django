"""
Etant donnée la liste des notes des élèves : notes = [12 , 04 , 14 , 11 , 18 , 13 ,
07, 10 , 05 , 09 , 15 , 08 , 14 , 16]
Ecrire un programme Python qui permet d’extraire de cette liste et créer une
autre liste qui contient uniquement les notes au-dessus de la moyenne ( les notes
>= 10 )
"""

notes = [12 , 4 , 14 , 11 , 18 , 13 , 7, 10 , 5 , 9 , 15 , 8 , 14 , 16]

liste_2 = []

for i in notes:
    if i >= 10:
        liste_2.append(i)

print(liste_2)