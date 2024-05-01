"""
Un palindrome est un mot dont l’ordre des lettres reste le même si on le lit de
gauche à droite ou de droite à gauche. Par exemple : ‘laval’ , ‘radar, ‘sos’… sont
des palindromes. Ecrire un programme en Python qui demande à l’utilisateur de
saisir un mot et de lui renvoyer s’il s’agit d’un palindrome ou non ?
"""

mot = input("Donnez un mot : ")

le_mot_est_palindrome = True
for i in range(int(len(mot)/2)):
    if mot[i] != mot[-(i+1)]:
        le_mot_est_palindrome = False

if le_mot_est_palindrome:
    print("le mot est palindrome")
else:
    print("le mot n'est pas palindrome")
