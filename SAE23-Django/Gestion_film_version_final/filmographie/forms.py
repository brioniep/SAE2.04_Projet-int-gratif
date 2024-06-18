from django import forms
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class FilmForm(ModelForm):
    class Meta :
        model = models.Film
        fields = '__all__'
        labels = {
            'titre' : _('Titre'),
            'categorie' : _('Categorie'),
            'annee' : _('Annee'),
            'realisateur' : _('Realisateur'), 
            'affiche' : _('Affiche'),  
            'acteur' : _('Acteur'),         
        }

        widgets = {
            'acteur': forms.CheckboxSelectMultiple,
            'id': forms.HiddenInput(),
        }

class CategorieForm(ModelForm):
    class Meta :
        model = models.Categorie
        fields = '__all__'
        labels = {
            'nom' : _('Nom'),
            'description' : _('Description'),
        }

        widgets = {
            'id': forms.HiddenInput(),
        }

class ActeurForm(ModelForm):
    class Meta :
        model = models.Acteur
        fields = '__all__'
        labels = {
            'nom' : _('Nom'),
            'prenom' : _('Prenom'),
            'age' : _('Age'),
            'photo' : _('Photo'),
        }

        widgets = {
            'id': forms.HiddenInput(),
        }

class UtilisateurForm(ModelForm):
    motdepasse = forms.CharField(widget=forms.PasswordInput)

    class Meta :
        model = models.Utilisateur
        fields = '__all__'
        labels = {
            'nom' : _('Nom'),
            'prenom' : _('Prenom'),
            'pseudo' : _('Pseudo'),
            'mail' : _('Mail'),
            'motdepasse' : _('Motdepasse'),
            'type' : _('Type'),
        }

        widgets = {
            'id': forms.HiddenInput(),
        }

class CommentaireForm(ModelForm):
    class Meta :
        model = models.Commentaire
        fields = '__all__'
        labels = {
            'film' : _('Film'),
            'utilisateur' : _('Utilisateur'),
            'note' : _('Note'),
            'commentaire' : _('Commentaire'),
            'date' : _('Date'),
        }

        widgets = {
            'id': forms.HiddenInput(),
        }

        