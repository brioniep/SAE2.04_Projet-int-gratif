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


def updatecapteurs(request, id):
    capteurs = models.capteurs.objects.get(pk = id)
    form = capteursForm(capteurs.dico())
    return render(request, "capteurs/ajout.html", {"form":form, "id":id})


def updatetraitementcapteurs(request, id):
    capteur = models.capteurs.objects.get(pk=id)
    if request.method == "POST":
        cform = capteursForm(request.POST, instance=capteur)
        if cform.is_valid():
            cform.save()
            return HttpResponseRedirect("/index-capteurs/")
    else:
        cform = capteursForm(instance=capteur)
    return render(request, 'capteurs/ajout.html', {"form": cform, "id": id})





#Views pour les pages Données

def indexdonnees(request):
    form = FilterForm(request.GET or None)
    donnees_liste = donnees.objects.all()

    if form.is_valid():
        capteur_nom = form.cleaned_data.get('capteur_nom')
        capteur_id = form.cleaned_data.get('capteur_id')
        start_date = form.cleaned_data.get('start_date')
        end_date = form.cleaned_data.get('end_date')

        if capteur_nom:
            donnees_liste = donnees_liste.filter(capteurID__nom__icontains=capteur_nom)
        if capteur_id:
            donnees_liste = donnees_liste.filter(capteurID__id=capteur_id)
        if start_date:
            donnees_liste = donnees_liste.filter(timestamp__gte=start_date)
        if end_date:
            donnees_liste = donnees_liste.filter(timestamp__lte=end_date)

    return render(request, 'donnees/index.html', {'form': form, 'donnees': donnees_liste})
    

import mysql.connector


def reset(request):
    mydb = mysql.connector.connect(
    host="192.168.1.14",
    user="root",
    password="Sae@2025!1",
    database="integratif")
    mycursor = mydb.cursor()
    mycursor.execute("TRUNCATE TABLE monappli_donnees")

    return HttpResponseRedirect("/index-donnees/")




from django.shortcuts import render
from django.http import JsonResponse
from .models import donnees

def get_all_sensor_data(request):
    try:
        data = donnees.objects.all().order_by('timestamp')
        response_data = {}
        for entry in data:
            capteur_id = str(entry.capteurID)  # Utiliser l'ID du capteur comme clé
            if capteur_id not in response_data:
                response_data[capteur_id] = []
            response_data[capteur_id].append({
                'timestamp': entry.timestamp.isoformat(),  # Convertir en format ISO pour JSON
                'valeur': entry.valeur
            })
        print("Données renvoyées:", response_data)  # Ajout du message de console
        return JsonResponse(response_data, safe=False)
    except Exception as e:
        print("Erreur lors de la récupération des données des capteurs:", e)
        return JsonResponse({"error": str(e)}, status=500)


# Dans views.py

import pandas as pd
import matplotlib.pyplot as plt
from django.shortcuts import render
from .models import donnees

def indexgraph(request):
    return render(request, 'donnees/graph.html')

