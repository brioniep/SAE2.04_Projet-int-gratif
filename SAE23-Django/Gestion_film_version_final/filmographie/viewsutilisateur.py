from django.shortcuts import render, HttpResponseRedirect
from .forms import UtilisateurForm
from . import models


def index(request):
    liste = list(models.Utilisateur.objects.all())
    return render(request, "utilisateurs/index.html", {"liste": liste})


def ajout(request):
    if request.method == "POST":
        form = UtilisateurForm(request)
        return render(request, "utilisateurs/ajout.html", {"form" : form})
    else :
        form = UtilisateurForm
        return render(request, "utilisateurs/ajout.html", {"form" : form})


def traitement(request):
    uform = UtilisateurForm(request.POST, request.FILES)
    if uform.is_valid():
        utilisateur = uform.save()
        return HttpResponseRedirect("/index-utilisateurs/")
    else:
        return render(request, "utilisateurs/ajout.html", {"form": uform})


def affiche(request, id):
    utilisateur = models.Utilisateur.objects.get(pk=id)
    return render(request, "utilisateurs/affiche.html", {"utilisateur": utilisateur})


def update(request, id):
    utilisateur = models.Utilisateur.objects.get(pk=id)
    if request.method == "POST":
        form = UtilisateurForm(request.POST, instance=utilisateur)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/index-utilisateurs/")
    else:
        form = UtilisateurForm(instance=utilisateur)
    return render(request, "utilisateurs/ajout.html", {"form": form, "id": id})


def updatetraitement(request, id):
    utilisateur = models.Utilisateur.objects.get(pk=id)
    if request.method == "POST":
        form = UtilisateurForm(request.POST, instance=utilisateur)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/index-utilisateurs/")
    else:
        form = UtilisateurForm(instance=utilisateur)
    return render(request, "utilisateurs/ajout.html", {"form": form, "id": id})


def delete(request, id):
    utilisateur = models.Utilisateur.objects.get(pk=id)
    utilisateur.delete()
    return HttpResponseRedirect("/index-utilisateurs/")