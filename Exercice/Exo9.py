#a= int (input("saisir le nombre de n"))
#produit =1
#for i in range(1,a+1):
#    produit *= i
#print(produit)
import math

# calcule du quotient et le reste de la division
#a= int (input("Saisir un nombre"))
#b= int (input("saisir le deuxieme nombre"))
#c= a/b
#d= a%b

#print(f"le quotient est {c}")
#print(f"le reste de la division est {d}")

# si un nombre est carré partfaiit ou non Exemple de rcin carré
x= int(input("saisir un nombre à verifier"))
c= math.sqrt(x)
d= int (c)
print(c)
print(d)
if c==d:
    print("c'est un nombre parfait")
else:
    print("ce n'est un nombre parfait")

