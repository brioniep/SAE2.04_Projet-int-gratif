from django import forms
from .models import Capteurs, Donnees

class CapteursForm(forms.ModelForm):
    class Meta:
        model = Capteurs
        fields = ['nom', 'piece', 'emplacement']

class DonneesForm(forms.ModelForm):
    class Meta:
        model = Donnees
        fields = ['capteur', 'timestamp', 'valeur']