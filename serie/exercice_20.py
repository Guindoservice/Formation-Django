"""
Ecrire un programme en langage Python, permettant d’échanger le premier et le
dernier caractère d’une chaine donnée.
"""

s = input("Donnez une phrase : ")

print(s[-1]+s[1:-1]+s[0])