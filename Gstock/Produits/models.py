from django.db import models

# Create your models here.
class Produit(models.Model):
    nom= models.CharField(max_length=100)
    prix= models.IntegerField()
    quantite= models.IntegerField()
    image= models.ImageField()
    description= models.TextField()
    disponible= models.BooleanField(default=False)

