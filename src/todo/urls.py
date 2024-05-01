import connexion

from django.conf.urls.static import static
from django.urls import path

from Gstock.Stock import settings
from .views import *

urlpatterns= [
    path("", todo_index, name='todo_index'),
    path("liste",todo_liste,name="todo_list"),
    path("ajouter", todo_ajouter,name='todo_ajouter'),
    path("supprimer/<int:id>",todo_suprimer,name='todo_suprimer'),
    path("changer_etat/<int:id>", todo_change_etat,name="todo_change_etat"),
    path("connexion",connexion, name="connexion"),
    path("deconnexion",deconnexion, name="deconnexion"),
]
