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
    coins_to_pay = models.IntegerField(default=20)
    num_borrow=models.IntegerField(default=0)
    
    
        
class Clients(models.Model):
    nom = models.CharField(max_length=55)
    prenom = models.CharField(max_length=55)
    email=models.CharField(max_length=255,default='')
    password=models.CharField(max_length=255,default='')
    role=models.CharField(max_length=80,default='user')
    tel = models.IntegerField(max_length=8)
    age = models.IntegerField(max_length=5)
    nb_livre=models.IntegerField(default=0)
    coins_purchased = models.IntegerField(default=200)
    
        

class Emprunt(models.Model):
    id_livre = models.ForeignKey(Livre,on_delete=models.CASCADE)
    id_client = models.ForeignKey(Clients,on_delete=models.CASCADE)
    date_emprunt = models.DateField()
    date_retour_prevue = models.DateField()
    date_retour_effective = models.DateField(null=True)
    coins_payed = models.IntegerField(default=0)


class CoinsPromo(models.Model):
    name = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True, null=True)
    coins = models.PositiveIntegerField(default=0)
    bonus_coins = models.PositiveIntegerField(default=0) 
    price = models.DecimalField(default=0,max_digits=10,decimal_places=2)
    is_active = models.BooleanField(default=True)  
    
    
class Purchase(models.Model):
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    coins_promo = models.ForeignKey(CoinsPromo, on_delete=models.CASCADE)  # Total cost of the purchase
    purchase_date = models.DateTimeField(auto_now_add=True)