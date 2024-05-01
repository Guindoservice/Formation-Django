from django.urls import path

from .views import index, nouvelle_facture, nouvel_client, connexion, deconnexion

urlpatterns= [
    path('', index, name='index'),
    path('nouvelle_facture', nouvelle_facture, name='nouvelle_facture'),
    path('nouvel_client', nouvel_client, name='nouvel_client'),
    path('connexion', connexion, name='connexion'),
    path('deconnexion', deconnexion, name='deconnexion'),

]