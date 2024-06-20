from django.shortcuts import render, HttpResponseRedirect
from . import models
from .models import donnees
from .forms import capteursForm, FilterForm
from django.http import JsonResponse


#Views la page d'Accueil
def index(request):
    return render(request, 'accueil/accueil.html')


#Views pour les page Capteurs
def indexcapteurs(request):
    liste = list(models.capteurs.objects.all())
    return render(request, "capteurs/index.html", {"liste": liste})

def affichecapteurs(request, id):
    capteur = models.capteurs.objects.get(pk=id)
    return render(request, "capteurs/affiche.html", {"capteur": capteur})


def updatecapteurs(request, id):
    capteur = models.Acteur.objects.get(pk=id)
    if request.method == "POST":
        form = capteursForm(request.POST, instance=capteur)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/index-capteurs/")
    else:
        form = capteursForm(instance=capteur)
    return render(request, "capteurs/ajout.html", {"form": form, "id": id})


def updatetraitementcapteurs(request, id):
    capteur = models.Acteur.objects.get(pk=id)
    if request.method == "POST":
        form = capteursForm(request.POST, instance=capteur)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/index-capteurs/")
    else:
        form = capteursForm(instance=capteur)
    return render(request, "capteurs/ajout.html", {"form": form, "id": id})




#Views pour les pages Données

def indexdonnees(request):
    liste = list(models.donnees.objects.all())
    return render(request, "donnees/index.html", {"liste": liste})

