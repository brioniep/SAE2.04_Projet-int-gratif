from django.urls import path 
from . import viewsfilm, viewsacteur, viewscategorie, viewscommentaire, viewsutilisateur, viewsaccueil

urlpatterns = [
    #page d'accueil
    path("index/", viewsaccueil.index),

    #page pour les films
    path("index-films/", viewsfilm.index),
    path("traitement-films/", viewsfilm.traitement),
    path("ajout-films/", viewsfilm.ajout),
    path("affiche-films/<int:id>/", viewsfilm.affiche),
    path("update-films/<int:id>/", viewsfilm.update),
    path("updatetraitement-films/<int:id>/", viewsfilm.updatetraitement),
    path("delete-films/<int:id>/", viewsfilm.delete),
    path('import-films/', viewsfilm.import_films, name='import_films'),
    path('generate-pdf/<int:film_id>/', viewsfilm.generate_film_pdf, name='generate_film_pdf'),

    #page pour les acteurs
    path("index-acteurs/", viewsacteur.index),
    path("traitement-acteurs/", viewsacteur.traitement),
    path("ajout-acteurs/", viewsacteur.ajout),
    path("affiche-acteurs/<int:id>/", viewsacteur.affiche),
    path("update-acteurs/<int:id>/", viewsacteur.update),
    path("updatetraitement-acteurs/<int:id>/", viewsacteur.updatetraitement),
    path("delete-acteurs/<int:id>/", viewsacteur.delete),

    #page pour les categorie
    path("index-categories/", viewscategorie.index),
    path("traitement-categories/", viewscategorie.traitement),
    path("ajout-categories/", viewscategorie.ajout),
    path("affiche-categories/<int:id>/", viewscategorie.affiche),
    path("update-categories/<int:id>/", viewscategorie.update),
    path("updatetraitement-categories/<int:id>/", viewscategorie.updatetraitement),
    path("delete-categories/<int:id>/", viewscategorie.delete),

    #page pour les commentaires
    path("index-commentaires/", viewscommentaire.index),
    path("traitement-commentaires/", viewscommentaire.traitement),
    path("ajout-commentaires/", viewscommentaire.ajout),
    path("affiche-commentaires/<int:id>/", viewscommentaire.affiche),
    path("update-commentaires/<int:id>/", viewscommentaire.update),
    path("updatetraitement-commentaires/<int:id>/", viewscommentaire.updatetraitement),
    path("delete-commentaires/<int:id>/", viewscommentaire.delete),
    path('commentaires/film/<int:film_id>/', viewscommentaire.commentaires_par_film, name='commentaires-par-film'),

    #page pour les utilisateurs
    path("index-utilisateurs/", viewsutilisateur.index),
    path("traitement-utilisateurs/", viewsutilisateur.traitement),
    path("ajout-utilisateurs/", viewsutilisateur.ajout),
    path("affiche-utilisateurs/<int:id>/", viewsutilisateur.affiche),
    path("update-utilisateurs/<int:id>/", viewsutilisateur.update),
    path("updatetraitement-utilisateurs/<int:id>/", viewsutilisateur.updatetraitement),
    path("delete-utilisateurs/<int:id>/", viewsutilisateur.delete),
]
