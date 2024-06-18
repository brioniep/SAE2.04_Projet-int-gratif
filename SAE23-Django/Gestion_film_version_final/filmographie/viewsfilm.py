from django.shortcuts import render, HttpResponseRedirect, redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from .forms import FilmForm
from . import models
from .models import Film, Acteur, Categorie, Commentaire
import csv


def index(request):
    liste = list(models.Film.objects.all())
    return render(request, "films/index.html", {"liste": liste})


def ajout(request):
    if request.method == "POST":
        form = FilmForm(request)
        return render(request, "films/ajout.html", {"form" : form})
    else :
        form = FilmForm
        return render(request, "films/ajout.html", {"form" : form})


def traitement(request):
    fform = FilmForm(request.POST, request.FILES)
    if fform.is_valid():
        film = fform.save()
        return HttpResponseRedirect("/index-films/")
    else:
        return render(request, "films/ajout.html", {"form": fform})


def affiche(request, id):
    film = models.Film.objects.get(pk=id)
    return render(request, "films/affiche.html", {"film": film})


def update(request, id):
    film = models.Film.objects.get(pk=id)
    if request.method == "POST":
        form = FilmForm(request.POST, instance=film)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/index-films/")
    else:
        form = FilmForm(instance=film)
    return render(request, "films/ajout.html", {"form": form, "id": id})


def updatetraitement(request, id):
    film = models.Film.objects.get(pk=id)
    if request.method == "POST":
        form = FilmForm(request.POST, instance=film)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/index-films/")
    else:
        form = FilmForm(instance=film)
    return render(request, "films/ajout.html", {"form": form, "id": id})


def delete(request, id):
    film = models.Categorie.objects.get(pk=id)
    film.delete()
    return HttpResponseRedirect("/index-films/")
 

def import_films(request):
    if request.method == 'POST' and request.FILES['csv_file']:
        csv_file = request.FILES['csv_file']
        fs = FileSystemStorage()
        filename = fs.save(csv_file.name, csv_file)
        file_path = fs.path(filename)

        with open(file_path, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                categorie, _ = Categorie.objects.get_or_create(nom=row['categorie'])
                film = Film.objects.create(
                    titre=row['titre'],
                    annee=row['annee'],
                    realisateur=row['realisateur'],
                    categorie=categorie
                )
                acteurs_noms = row['acteur'].split(', ')
                for nom in acteurs_noms:
                    prenom, nom_de_famille = nom.split(' ')
                    acteur, _ = Acteur.objects.get_or_create(prenom=prenom, nom=nom_de_famille)
                    film.acteur.add(acteur)
        return HttpResponseRedirect('/index-films/')
    return render(request, 'films/import_films.html')


def generate_film_pdf(request, film_id):
    try:
        film = Film.objects.get(id=film_id)
        commentaires = Commentaire.objects.filter(film=film)
    except Film.DoesNotExist:
        return HttpResponse("Film non trouvé", status=404)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{film.titre}.pdf"'

    p = canvas.Canvas(response, pagesize=letter)
    width, height = letter

    p.setFont("Helvetica-Bold", 20)
    p.drawString(100, height - 50, f"Fiche du film : {film.titre}")

    p.setFont("Helvetica", 12)
    p.drawString(100, height - 100, f"Catégorie : {film.categorie.nom}")
    p.drawString(100, height - 120, f"Date de sortie : {film.annee}")
    p.drawString(100, height - 140, f"Réalisateur : {film.realisateur}")

    p.setFont("Helvetica-Bold", 14)
    p.drawString(100, height - 180, "Acteurs :")
    p.setFont("Helvetica", 12)
    y = height - 200
    for acteur in film.acteur.all():
        p.drawString(120, y, f"{acteur.prenom} {acteur.nom}")
        y -= 20

    p.setFont("Helvetica-Bold", 14)
    p.drawString(100, y - 20, "Commentaires :")
    y -= 40
    p.setFont("Helvetica", 12)
    for commentaire in commentaires:
        p.drawString(120, y, f"{commentaire.utilisateur.pseudo} ({commentaire.note}/20) : {commentaire.commentaire}")
        y -= 20
        if y < 50:
            p.showPage()
            y = height - 50
            p.setFont("Helvetica", 12)

    p.showPage()
    p.save()

    return response