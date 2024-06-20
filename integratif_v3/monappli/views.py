from django.shortcuts import render, HttpResponseRedirect
from . import models
from .models import Donnees
from .forms import CapteursForm, FilterForm
from django.http import JsonResponse


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

def filtrer_donnees(request):
    form = FilterForm(request.GET or None)
    donnees = models.Donnees.objects.all()

    if form.is_valid():
        capteur_nom = form.cleaned_data.get('capteur_nom')
        capteur_id = form.cleaned_data.get('capteur_id')
        start_date = form.cleaned_data.get('start_date')
        end_date = form.cleaned_data.get('end_date')

        if capteur_nom:
            donnees = donnees.filter(capteur__nom__icontains=capteur_nom)
        if capteur_id:
            donnees = donnees.filter(capteur__id=capteur_id)
        if start_date:
            donnees = donnees.filter(timestamp__gte=start_date)
        if end_date:
            donnees = donnees.filter(timestamp__lte=end_date)

    return render(request, "donnees/filtrer.html", {"form": form, "donnees": donnees})

def fetch_data(request):
    donnees = Donnees.objects.all().order_by('-timestamp')
    data = [
        {
            'id': donnee.id,
            'capteur': donnee.capteur.id,
            'timestamp': donnee.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
            'valeur': donnee.valeur
        } for donnee in donnees
    ]
    return JsonResponse(data, safe=False)