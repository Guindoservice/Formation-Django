liste=  [
{ "nom":"Abdala","prenom": "Guindo", "age":25},
{ "nom":"togo","prenom": "ALY", "age":22},
{ "nom":"Diarra","prenom": "Guindo", "age":15},

]
print(liste[0])
nom = "Abdala"
poste= "developpeur web en python"
a= "Je suis {1} guindo et je suis  {0}   ".format(nom,poste)
print(a)

#la methode pour formater de typr de donné
var= 26
print("La valeur decimale est : {0:d}".format(var))
print("La valeur hexadecimal est : {0:x}".format(var))
print("La valeur octal est : {0:o}".format(var))
print("la valeur binaire est : {0:b}".format(var))

# le formatage par symbole  "%s pour variable en chaine"
# "%f pour les decimaux",
# "%d pour les entier" ,
# "%x por les exadecimaux "
a= "Guindo"
b= "Developeur"
d= 24
print("le m'appel %s je suis %s en python j'ai  %d ans "%(a,b,d))