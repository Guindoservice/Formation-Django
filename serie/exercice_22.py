"""
Ecrire un programme en Python, qui permet de renvoyer le premier mot d’un
texte donné. Exemple pour le texte : t =’Python est un merveilleux langage de
programmation’, le programme doit renvoyer Python
"""
s = input("Donnez une phrase : ")

# split permet de transformer un chaine en liste (tableau)
# exempe si s = "Bonjour tout le nom"
# s.split(" ") = ["Bonjour", "tout","le","monde"]
#
# exempe si s = "Bonjour-tout-le-nom"
# s.split("-") = ["Bonjour", "tout","le","monde"]

s_en_liste = s.split(" ")
print(s_en_liste[0])
