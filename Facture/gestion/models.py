from django.contrib.auth.models import User
from django.db import models

# Create your m
class Customer(models.Model):
    """
    nom = Customer definition
   """
    sex_type = (
        ('M','Masculin'),
        ('F','Feminin'),
    )
    nom = models.CharField(max_length=150)

    email = models.EmailField()

    telephone= models.CharField(max_length=100)

    adresse= models.CharField(max_length=100)

    sexe= models.CharField(max_length=1 , choices=sex_type)

    creat_date= models.DateTimeField(auto_now_add=True)

    save_by = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        verbose_name= 'Customer'
        verbose_name_plural= 'Customers'
    def __str__(self):
        return self.nom

class Invoice(models.Model):
    """
    nom = Invoice
    description:
    auteur : Abdala guindo
    """
    INVOICE_TYPE= (
        ('R', 'Reçu'),
        ('P', 'PROFORMA'),
        ('F', 'FACTURE'),
    )
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    save_by = models.ForeignKey(User, on_delete=models.PROTECT)
    invoice_date_time= models.DateTimeField(auto_now_add=True)
    total= models.DecimalField(max_digits=10000, decimal_places=2)
    last_update_date= models.DateTimeField(null=True, blank =True)
    paie= models.BooleanField(default=False)
    invoice_type= models.CharField(max_length=1, choices=INVOICE_TYPE)
    comments= models.TextField(max_length=1000, blank=True)

    class Meta:
        verbose_name = 'Invoice'
        verbose_name_plural= 'Invoices'


    def __str__(self):
        return f"{self.customer.nom} {self.invoice_date_time}"
    @property
    def get_total(self):
        articles= self.article_set.all()
        total= sum(article.get_total for article in articles)

class Article(models.Model):
    """
    nom = Article invoice
    description :
    Auteur : Ablo
    """
    invoice= models.ForeignKey(Invoice,on_delete=models.CASCADE)
    nom = models.CharField(max_length=1000)
    quantite= models.IntegerField()
    prix_unit= models.DecimalField(max_digits=1000, decimal_places=2)
    total= models.DecimalField(max_digits=1000, decimal_places=2)
    class Meta:
        verbose_name= 'Article'
        verbose_name_plural= 'Articles'
    @property
    def get_total(self):
        total= self.quantite * self.prix_unit




