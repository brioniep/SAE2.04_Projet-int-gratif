from django.urls import path 
from . import views

urlpatterns = [
    #page d'accueil
    path("index/", views.index),

    #page capteurs
    path("index-capteurs/", views.indexcapteurs),
    path("update-capteurs/<int:id>/",views.updatecapteurs),
    path("updatetraitement-capteurs/<int:id>/", views.updatetraitementcapteurs),
    
    # page données
    path("index-donnees/", views.indexdonnees, name='index_donnees'),
    path("index-donnees/reset/", views.reset),
    path("index-graph/", views.indexgraph),

]