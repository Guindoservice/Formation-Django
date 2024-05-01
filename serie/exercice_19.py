"""
Ecrire un programme en Python qui permet de lister les chaines qui composent
la liste l = [“laptop”, “iphone”, “tablet”] tout en indiquant la longueur de chaque
chaine.
"""

l = ["laptop","iphone","tablet"]

for chaine in l:
    print(f"{chaine} est de longueur:  {len(chaine)} ")