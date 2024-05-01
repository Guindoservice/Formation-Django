"""
Écrire un programme en Python qui renvoie toutes les listes obtenues en
permutant les termes d’une liste donnée.
"""
import itertools

# soit la list suivant

ma_liste = [1,2,3,4,5]

for L in range(len(ma_liste) + 1):
    for subset in itertools.combinations(ma_liste, L):
        print(list(subset))