from django.shortcuts import render, HttpResponseRedirect
from django.db.models import Avg, Max, Min
from .forms import CommentaireForm
from . import models
from .models import Film, Commentaire


def index(request):
    liste = list(models.Commentaire.objects.all())
    return render(request, "commentaires/index.html", {"liste": liste})


def ajout(request):
    if request.method == "POST":
        form = CommentaireForm(request)
        return render(request, "commentaires/ajout.html", {"form" : form})
    else :
        form = CommentaireForm
        return render(request, "commentaires/ajout.html", {"form" : form})


def traitement(request):
    cform = CommentaireForm(request.POST, request.FILES)
    if cform.is_valid():
        commentaire = cform.save()
        return HttpResponseRedirect("/index-commentaires/")
    else:
        return render(request, "commentaires/ajout.html", {"form": cform})


def affiche(request, id):
    commentaire = models.Commentaire.objects.get(pk=id)
    return render(request, "commentaires/affiche.html", {"commentaire": commentaire})


def update(request, id):
    commentaire = models.Commentaire.objects.get(pk=id)
    if request.method == "POST":
        form = CommentaireForm(request.POST, instance=commentaire)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/index-commentaires/")
    else:
        form = CommentaireForm(instance=commentaire)
    return render(request, "commentaires/ajout.html", {"form": form, "id": id})


def updatetraitement(request, id):
    commentaire = models.Commentaire.objects.get(pk=id)
    if request.method == "POST":
        form = CommentaireForm(request.POST, instance=commentaire)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/index-commentaires/")
    else:
        form = CommentaireForm(instance=commentaire)
    return render(request, "commentaires/ajout.html", {"form": form, "id": id})


def delete(request, id):
    commentaire = models.Commentaire.objects.get(pk=id)
    commentaire.delete()
    return HttpResponseRedirect("/index-commentaires/")


def commentaires_par_film(request, film_id):
    film = Film.objects.get(pk=film_id)
    commentaires = Commentaire.objects.filter(film=film)
    moyenne_notes = commentaires.aggregate(moyenne=Avg('note'))['moyenne']
    meilleure_note = commentaires.aggregate(meilleure=Max('note'))['meilleure']
    pire_note = commentaires.aggregate(pire=Min('note'))['pire']
    meilleure_commentaire = Commentaire.objects.filter(film=film, note=meilleure_note).first()
    pire_commentaire = Commentaire.objects.filter(film=film, note=pire_note).first()
    meilleur_utilisateur = meilleure_commentaire.utilisateur.pseudo if meilleure_commentaire else None
    pire_utilisateur = pire_commentaire.utilisateur.pseudo if pire_commentaire else None

    return render(request, "commentaires/commentaires_par_film.html", {
        "film": film,
        "commentaires": commentaires,
        "moyenne_notes": moyenne_notes,
        "meilleure_note": meilleure_note,
        "pire_note": pire_note,
        "meilleure_commentaire": meilleure_commentaire,
        "pire_commentaire": pire_commentaire,
        "meilleur_utilisateur": meilleur_utilisateur,
        "pire_utilisateur": pire_utilisateur,
    })