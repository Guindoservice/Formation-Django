"""
Écrire un programme Python qui permet de supprimer les éléments dupliqués
"""

# exemple
ma_liste = [5,9,6,3,5,6,2,6,3]

ma_liste = list(set(ma_liste))

print(ma_liste)

# les set permet de supprimer les doublons d'une liste