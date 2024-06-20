from django.shortcuts import render, HttpResponseRedirect
from . import models
from .forms import CapteursForm, DonneesForm


#Views la page d'Accueil
def index(request):
    return render(request, 'accueil/accueil.html')


#Views pour les page Capteurs
def indexcapteurs(request):
    liste = list(models.Capteurs.objects.all())
    return render(request, "capteurs/index.html", {"liste": liste})

def affichecapteurs(request, id):
    capteur = models.Capteurs.objects.get(pk=id)
    return render(request, "capteurs/affiche.html", {"capteur": capteur})


def updatecapteurs(request, id):
    capteur = models.Acteur.objects.get(pk=id)
    if request.method == "POST":
        form = CapteursForm(request.POST, instance=capteur)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/index-capteurs/")
    else:
        form = CapteursForm(instance=capteur)
    return render(request, "capteurs/ajout.html", {"form": form, "id": id})


def updatetraitementcapteurs(request, id):
    capteur = models.Acteur.objects.get(pk=id)
    if request.method == "POST":
        form = CapteursForm(request.POST, instance=capteur)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/index-capteurs/")
    else:
        form = CapteursForm(instance=capteur)
    return render(request, "capteurs/ajout.html", {"form": form, "id": id})




#Views pour les pages Données

def indexdonnees(request):
    liste = list(models.Donnees.objects.all())
    return render(request, "donnees/index.html", {"liste": liste})


def affichedonnees(request, id):
    donnee = models.Donnees.objects.get(pk=id)
    return render(request, "donnees/affiche.html", {"donnee": donnee})
