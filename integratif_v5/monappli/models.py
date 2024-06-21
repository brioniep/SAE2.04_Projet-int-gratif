from django.db import models

# Create your models here.

class capteurs(models.Model):
    nom = models.CharField(max_length=255, unique=True)
    piece = models.CharField(max_length=255)
    emplacement = models.CharField(max_length=255)

    def __str__(self):
        return self.nom

class donnees(models.Model):
    capteurID = models.ForeignKey(capteurs, on_delete=models.CASCADE, null=True, blank=True)
    timestamp = models.DateTimeField()
    valeur = models.FloatField()

    def __str__(self):
        return f"{self.capteurID} - {self.timestamp}"