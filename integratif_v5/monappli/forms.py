# forms.py
from django import forms
from .models import capteurs, donnees

class capteursForm(forms.ModelForm):
    class Meta:
        model = capteurs
        fields = ['nom', 'piece', 'emplacement']

class donneesForm(forms.ModelForm):
    class Meta:
        model = donnees
        fields = ['capteurID', 'timestamp', 'valeur']

class FilterForm(forms.Form):
    capteur_nom = forms.CharField(required=False, label='Nom du Capteur')
    capteur_id = forms.IntegerField(required=False, label='ID du Capteur')
    start_date = forms.DateField(required=False, label='Date de début', widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(required=False, label='Date de fin', widget=forms.DateInput(attrs={'type': 'date'}))