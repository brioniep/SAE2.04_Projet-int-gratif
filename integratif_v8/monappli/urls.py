from django.urls import path 
from . import views
from .views import get_all_sensor_data

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
    path('api/all-sensor-data/', get_all_sensor_data, name='get_all_sensor_data'),



]