from django.db import models

# Create your models here.

class Livre(models.Model):
    titre = models.CharField(max_length=200)
    auteur = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    description = models.TextField()
    date_publication = models.DateField()
    couverture_link = models.URLField(max_length=255)
    
    def __init__(self,titre,auteur,genre,description,date_publication,couverture_link):
        self.titre = titre
        self.auteur = auteur
        self.genre = genre
        self.description = description
        self.date_publication = date_publication
        self.couverture_link = couverture_link
        
class Clients(models.Model):
    nom = models.CharField(max_length=55)
    prenom = models.CharField(max_length=55)
    tel = models.IntegerField(max_length=8)
    age = models.IntegerField(max_length=5)
    
    def __init__(self,nom,prenom,tel,age):
        self.nom = nom
        self.prenom = prenom
        self.tel = tel
        self.age = age
        

class Emprunt(models.Model):
    id_livre = models.ForeignKey(Livre,on_delete=models.CASCADE)
    id_client = models.ForeignKey(Clients,on_delete=models.CASCADE)
    date_emprunt = models.DateField()
    date_retour_prevue = models.DateField()
    date_retour_effective = models.DateField(null=True)
    
    
    def __init__(self,id_livre,id_client,date_emprunt,date_retour_prevue):
        self.id_livre = id_livre
        self.id_client = id_client
        self.date_emprunt = date_emprunt
        self.date_retour_prevue = date_retour_prevue