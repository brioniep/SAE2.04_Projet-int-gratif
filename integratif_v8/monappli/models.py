from django.db import models

# Create your models here.

class capteurs(models.Model):
    nom = models.CharField(max_length=255, unique=True)
    nom2 = models.CharField(max_length=255, blank=True, unique=True)
    piece = models.CharField(max_length=255)
    emplacement = models.CharField(max_length=255, blank=True)

    
    def dico(self):
        return {
            "emplacement": self.emplacement, "nom2": self.nom2
            
        }
    

class donnees(models.Model):
    capteurID = models.ForeignKey(capteurs, on_delete=models.CASCADE, null=True, blank=True)
    timestamp = models.DateTimeField()
    valeur = models.FloatField()