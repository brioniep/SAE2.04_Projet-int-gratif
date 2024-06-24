# forms.py
from . import models
from django.utils.translation import gettext_lazy as _
from django import forms
from .models import capteurs, donnees


class capteursForm(forms.ModelForm):
    class Meta:
        model = models.capteurs
        fields = ['nom2', 'emplacement',]
        label = {
            'emplacement': _('emplacement du capteur'),
            'nom2': _('Nom du capteur'),            
        }

class donneesForm(forms.ModelForm):
    class Meta:
        model = donnees
        fields = ['capteurID', 'timestamp', 'valeur']

class FilterForm(forms.Form):
    capteur_nom = forms.CharField(required=False, label='ID capteur')
    start_date = forms.DateField(required=False, label='Date de début', widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(required=False, label='Date de fin', widget=forms.DateInput(attrs={'type': 'date'}))