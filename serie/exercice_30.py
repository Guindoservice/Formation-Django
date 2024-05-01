"""
Ecrire une fonction en Python qui permet de comparer deux listes et de nous
indiquer si ces deux listes ont une valeur commune ou non
"""

list_1 = [5,65,4,9,2,3,64,8,6,5]
list_2 = [6,8,22,55]

ont_une_valeur_en_commune = False
for i in list_2:
    if i in list_1:
        ont_une_valeur_en_commune = True

if ont_une_valeur_en_commune:
    print("Ces deux listes ont une valeur en commune")
else:
    print("Ces deux listes n'ont pas une valeur en commune")
