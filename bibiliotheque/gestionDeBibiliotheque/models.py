from django.db import models

# Create your models here.

class Livre(models.Model):
    titre = models.CharField(max_length=200)
    auteur = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    description = models.TextField()
    date_publication = models.DateField()
    couverture = models.ImageField(upload_to='book_covers/',default='book_covers/default.jpg')
    status=models.CharField(max_length=255,default='disponible')
    
    
        
class Clients(models.Model):
    nom = models.CharField(max_length=55)
    prenom = models.CharField(max_length=55)
    email=models.CharField(max_length=255,default='')
    password=models.CharField(max_length=255,default='')
    tel = models.IntegerField(max_length=8)
    age = models.IntegerField(max_length=5)
    nb_livre=models.IntegerField(default=0)
    
        

class Emprunt(models.Model):
    id_livre = models.ForeignKey(Livre,on_delete=models.CASCADE)
    id_client = models.ForeignKey(Clients,on_delete=models.CASCADE)
    date_emprunt = models.DateField()
    date_retour_prevue = models.DateField()
    date_retour_effective = models.DateField(null=True)
    
    