from django.urls import path 
from . import views

urlpatterns = [
    #page d'accueil
    path("index/", views.index),

    #page capteurs
    path("index-capteurs/", views.indexcapteurs),
    path("affiche-capteurs", views.affichecapteurs),
    path("update-capteurs",views.updatecapteurs),
    path("updatetraitement-capteurs/<int:id>/", views.updatetraitementcapteurs),
    
    # page données
    path("index-donnees/", views.indexdonnees),
]