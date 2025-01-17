from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.hashers import make_password,check_password
from gestionDeBibiliotheque.models import *
from django.core.paginator import Paginator

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
        return HttpResponseRedirect(reverse('affiche_livre'))
def update_liver(request,id):
    if request.method=='GET':
        liver=Livre.objects.filter(id=id).first()
        return render(request,'admin/update.html',{'livre':liver})
    else:
        liver=Livre.objects.filter(id=id).first()
        
        liver.titre=request.POST['titre']
        liver.description=request.POST['description']
        liver.auteur=request.POST['auteur']
        liver.date_publication=request.POST['date_publication']
        liver.genre=request.POST['genre']
        # liver['couverture']=request.POST['couverture']
        liver.save()
        return HttpResponseRedirect(reverse('affiche_livre'))
def update_client(request,id):
    if request.method=='GET':
        client=Clients.objects.filter(id=id).first()
        return render(request,'admin/update_cliens.html',{'client':client})
    else:
        client=Clients.objects.filter(id=id).first()
        
        client.nom=request.POST['nom']
        client.prenom=request.POST['prenom']
        client.email=request.POST['email']
        client.tel=request.POST['tel']
        client.save()
        return HttpResponseRedirect(reverse('affiche_cliens'))
def affiche_livre(request):
    livres=Livre.objects.all()
    paginator = Paginator(livres, 4)
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'admin/affiche_livre.html',{'livres':page_obj})
def affiche_cliens(request):
    clients=Clients.objects.all()
    return render(request,'admin/affiche_cliens.html',{'clients':clients})
def delete(request,id):
    liver=Livre.objects.filter(id=id).first()
    liver.delete()
    return HttpResponseRedirect(reverse('affiche_livre'))
def test(request):
    return render(request,'admin/test.html')
def ajoute_clients(request):
        nom=request.POST['nom']
        prenom=request.POST['prenom']
        email=request.POST['email']
        tel=request.POST['tel']
        age=request.POST['age']
        password=make_password(request.POST['password'])
        user=Clients(nom=nom,prenom=prenom,email=email,password=password,tel=tel,age=age)
        user.save()
        return HttpResponseRedirect(reverse('affiche_cliens'))
def delete_clients(request,id):
    client=Clients.objects.filter(id=id).first()
    client.delete()
    return HttpResponseRedirect(reverse('affiche_cliens'))
def login(request):
    return HttpResponseRedirect('/login')