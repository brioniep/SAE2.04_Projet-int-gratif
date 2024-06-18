from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Acteur(models.Model):
    nom = models.CharField(max_length=75, blank = False)
    prenom = models.CharField(max_length=75, blank = False)
    age = models.IntegerField(blank = True, null=True)
    photo = models.ImageField(upload_to='photo/', blank=True, null=True)

    def __str__(self):
        chaine = f"{self.prenom} {self.nom} pranked"
        return chaine
    
    def dico(self):
        return{"non":self.nom, "prenom":self.prenom, "age":self.age, "photo":self.photo}



class Film(models.Model):
    titre = models.CharField(max_length=75, blank = False)
    categorie = models.ForeignKey("categorie", on_delete=models.CASCADE, default=None, blank=False)
    annee = models.DateField(blank = False)
    realisateur = models.CharField(max_length=75, blank=False)
    affiche = models.ImageField(upload_to='photo/', blank=True, null=True)
    acteur = models.ManyToManyField(Acteur, related_name='film')
    

    def __str__(self):
        chaine = f"{self.titre}"
        return chaine
    
    def dico(self):
        return{"titre":self.titre, "categorie":self.categorie, "annee":self.annee, "realisateur":self.realisateur, "affiche":self.affiche}
    


class Categorie(models.Model):
    nom = models.CharField(max_length=75, blank = False)
    description = models.TextField(blank = False)

    def __str__(self):
        chaine = f"{self.nom}"
        return chaine
    
    def dico(self):
        return{"nom":self.nom, "description":self.description}



class Utilisateur(models.Model):
    AMATEUR = 'AMATEUR'
    PROFESSIONNEL = 'PROFESSIONNEL'

    CHOIX_TYPE = [
        (AMATEUR, 'Amateur'),
        (PROFESSIONNEL, 'Professionnel'),
    ]

    pseudo = models.CharField(max_length=75, blank = False)
    nom = models.CharField(max_length=75, blank = False)
    prenom = models.CharField(max_length=75, blank = False)
    mail = models.EmailField(max_length=75, blank = False)
    motdepasse = models.CharField(max_length=75, blank = False)
    type =  models.CharField(
        max_length=13,
        choices=CHOIX_TYPE,
        default=AMATEUR,
    )

    def __str__(self):
        chaine = f"{self.pseudo}"
        return chaine
    
    def dico(self):
        return{"pseudo":self.pseudo, "nom":self.nom, "prenom":self.nom, "mail":self.mail, "motdepasse":self.motdepasse, "type":self.type}



class Commentaire(models.Model):
    film = models.ForeignKey("film", on_delete=models.CASCADE, default=None, blank=False)
    utilisateur = models.ForeignKey("utilisateur", on_delete=models.CASCADE, default=None, blank=False)
    note = models.IntegerField(
        blank=False,
        validators=[MinValueValidator(0), MaxValueValidator(20)],
        help_text="La note doit être un entier entre 0 et 20."
    )
    commentaire = models.TextField(null = True, blank = False)
    date = models.DateField(blank = False)

    def __str__(self):
        chaine = f"Film : {self.film}, Note : {self.note}, De : {self.utilisateur}"
        return chaine
    
    def dico(self):
        return{"film":self.film, "utilisateur":self.utilisateur, "note":self.note, "commentaire":self.commentaire, "date":self.date }