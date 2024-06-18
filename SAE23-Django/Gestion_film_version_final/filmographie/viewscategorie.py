from django.shortcuts import render, HttpResponseRedirect
from .forms import CategorieForm
from . import models


def index(request):
    liste = list(models.Categorie.objects.all())
    return render(request, "categories/index.html", {"liste": liste})


def ajout(request):
    if request.method == "POST":
        form = CategorieForm(request)
        return render(request, "categories/ajout.html", {"form" : form})
    else :
        form = CategorieForm
        return render(request, "categories/ajout.html", {"form" : form})


def traitement(request):
    cform = CategorieForm(request.POST, request.FILES)
    if cform.is_valid():
        categorie = cform.save()
        return HttpResponseRedirect("/index-categories/")
    else:
        return render(request, "categories/ajout.html", {"form": cform})


def affiche(request, id):
    categorie = models.Categorie.objects.get(pk=id)
    return render(request, "categories/affiche.html", {"categorie": categorie})


def update(request, id):
    categorie = models.Categorie.objects.get(pk=id)
    if request.method == "POST":
        form = CategorieForm(request.POST, instance=categorie)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/index-categories/")
    else:
        form = CategorieForm(instance=categorie)
    return render(request, "categories/ajout.html", {"form": form, "id": id})


def updatetraitement(request, id):
    categorie = models.Categorie.objects.get(pk=id)
    if request.method == "POST":
        form = CategorieForm(request.POST, instance=categorie)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/index-categories/")
    else:
        form = CategorieForm(instance=categorie)
    return render(request, "categories/ajout.html", {"form": form, "id": id})


def delete(request, id):
    categorie = models.Categorie.objects.get(pk=id)
    categorie.delete()
    return HttpResponseRedirect("/index-categories/")