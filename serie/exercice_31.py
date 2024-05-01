"""
Écrire un programm e Python qui permet d’extraire la liste des entiers pairs et la
liste des entiers impairs d’une liste de nombres.
"""

# soit la liste suivante

ma_list = [2,6,4,9,2,55,32,21,7,38]

list_pair = []
list_impair = []

[ list_pair.append(i) if i%2 == 0 else list_impair.append(i) for  i in ma_list]

print(f"liste des pairs {list_pair}")
print(f"liste des impairs {list_impair}")
