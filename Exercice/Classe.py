class Rectangle:
    def __init__(self,longeur, largeur):
        self.longeur= longeur
        self.largeur = largeur

    # la methode pour calculer le perimetre
    def Perimetre(self):
        return 2*self.longeur+ self.largeur

    def surface(self):
        return self.longeur* self.largeur


monRectangle = Rectangle(8,3)

print("le perimetre de ce nombre est ", monRectangle.Perimetre())
print("le surface est est ",monRectangle.surface())
