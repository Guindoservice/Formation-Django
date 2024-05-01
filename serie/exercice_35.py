"""
Ecrire un programme en Python qui permet de transformer une adresse url saisie
au clavier en un lien hypertexte.
"""
url = input("Donnez une adresse url : ")

lien_hyper_text = f"<a hre='{url}'>Lien</a>"
print(lien_hyper_text)