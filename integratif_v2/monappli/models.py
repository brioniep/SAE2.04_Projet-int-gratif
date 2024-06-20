from django.db import models

# Create your models here.

class Capteurs(models.Model):
    nom = models.CharField(max_length=100, unique=True)
    piece = models.CharField(max_length=100)
    emplacement = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class Donnees(models.Model):
    capteur = models.ForeignKey(Capteurs, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    valeur = models.FloatField()

    def __str__(self):
        return f"{self.capteur.nom} - {self.timestamp}"