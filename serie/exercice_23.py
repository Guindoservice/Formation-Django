"""
Ecrire un programme en langage Python qui demande à l’utilisateur de saisir le
nom d’un fichier et de lui renvoyer son extension. Exemple si l’utilisateur saisie
coursPython.pdf, le programme lui renvoie le message “L’extension du fichier
est .pdf”
"""

nom_du_fichier  = input("Donnez le nom d'un fichier : ")

# voir exercice 22

nom_du_fichier_en_liste = nom_du_fichier.split(".")
extension = nom_du_fichier_en_liste[-1]

print(f"L’extension du fichier est .{extension}")