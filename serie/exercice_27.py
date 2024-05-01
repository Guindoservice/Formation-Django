"""
Écrire un programme en Python sous forme de fonction qui calcul la somme des
élémen ts d’une liste de nombres. Et un autre qui permet de multiplier tous les
éléments d’une liste de nombres.
"""

def somme(liste):
    return sum(liste)

def produit(liste):
    p = 1

    for i in liste:
        p *= i
    return p

# pour test les fonction

ma_liste = [5,1,2]
print(f"somme de ma liste = {somme(ma_liste)}")
print(f"produit de ma liste = {produit(ma_liste)}")