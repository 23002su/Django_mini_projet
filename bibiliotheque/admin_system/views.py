from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from gestionDeBibiliotheque.models import *
# Create your views here.
def ajout_liver(request):
    if request.method=='GET':
        return render(request,'admin/ajoute_liver.html')
    else:
            
        titre=request.POST['titre']
        description=request.POST['description']
        auteur=request.POST['auteur']
        date_publication=request.POST['date_publication']
        genre=request.POST['genre']
        couverture=request.FILES['couverture']
        liver=Livre(titre=titre,description=description,auteur=auteur,date_publication=date_publication,genre=genre,couverture=couverture)
        liver.save()
        return HttpResponse("nsr")
