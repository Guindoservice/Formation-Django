"""
Ecrire un programme en Python permettant de supprimer les espaces multiples
dans une chaine s.
"""
import re

s = input("Donnez un chaine : ")

s_sans_espace_multiple = re.sub(' +', ' ', s)

print(s_sans_espace_multiple)