from django.db import models

# Create your models here.
class TodoList(models.Model):
    nom= models.CharField(max_length=500)
    effectuer = models.BooleanField(default=False)
