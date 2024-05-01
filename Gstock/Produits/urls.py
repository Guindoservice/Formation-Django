from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import accueil, Ajouterproduit, connexion, listeproduit, deconnexion, supprimer, modifier


urlpatterns=[
    path('',accueil,name="Accueil"),
    path('Article',Ajouterproduit,name="Article"),
    path('ListeProduit',listeproduit,name='ListeProduit'),
    path("connexion",connexion,name="connexion"),
    path("deconnexion",deconnexion,name="deconnexion"),
    path("supprimer/<int:id>", supprimer, name='supprimer'),
    path("modifier/<int:id>", modifier, name='modifier'),
]