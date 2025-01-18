from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password,check_password
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import *
from datetime import datetime, timedelta

# Create your views here.

def displayBooks(request):
    livres = Livre.objects.filter(status='disponible').all()
    if "user" in request.session:
        user_conect=request.session['user']
        return render(request, 'index.html', {'livres': livres, 'user_conect':user_conect })
    else:
        return render(request, 'index.html', {'livres': livres})

def ClickedBook(request, id):
    livres = Livre.objects.all().filter(status='disponible')
    try:
        selectedbook = Livre.objects.get(id=id)
    except Livre.DoesNotExist:
        selectedbook = None
    if "user" in request.session:
        client=Clients.objects.filter(email=request.session['user']).first()
        nbr=client.nbr_point
        # if nbr==0:
        #     return render(request, 'index.html',{'livres':livres, 'selectedbook':selectedbook})
        # return HttpResponse(nbr)
        return render(request, 'index.html',{'livres':livres, 'selectedbook':selectedbook,"nbr_point":nbr})
    return render(request, 'index.html',{'livres':livres, 'selectedbook':selectedbook})

def cancel(request):
    return HttpResponseRedirect(reverse('displayBooks'))

def regester(request):
    if request.method=='GET':
        return  render(request,'regester.html')
    else:
        nom=request.POST['nom']
        prenom=request.POST['prenom']
        email=request.POST['email']
        tel=request.POST['tel']
        age=request.POST['age']
        password=make_password(request.POST['password'])
        user=Clients(nom=nom,prenom=prenom,email=email,password=password,tel=tel,age=age)
        user.save()
        return HttpResponseRedirect(reverse("displayBooks"))
def emprent_liver(request,id):
    if "user" in request.session:
        email=request.session['user']
        client=Clients.objects.filter(email=email).first()
        if client.nbr_point==0:
            livres = Livre.objects.all().filter(status='disponible')
            return render(request, 'index.html',{'livres':livres,'vide':"vide"})
        client.nbr_point=client.nbr_point-50
        date_emprunt=datetime.today().date()
        date_retour_prevue =datetime.today().date()+timedelta(days=4)
        livre =Livre.objects.filter(id=int(id)).first()
        
        emprenteur=Emprunt(id_client=client,id_livre=livre,date_emprunt=date_emprunt,date_retour_prevue=date_retour_prevue)
        emprenteur.save()

        client.save()
        return HttpResponseRedirect(reverse('displayBooks'))
    else:
        return HttpResponseRedirect(reverse("login"))
def emprent_avec_livreson(request,id):
    if "user" in request.session:
        email=request.session['user']
        client=Clients.objects.filter(email=email).first()
        if client.nbr_point==0:
            livres = Livre.objects.all().filter(status='disponible')
            return render(request, 'index.html',{'livres':livres,'vide':"vide"})
        client.nbr_point=client.nbr_point-75
        date_emprunt=datetime.today().date()
        date_retour_prevue =datetime.today().date()+timedelta(days=4)
        livre =Livre.objects.filter(id=int(id)).first()
        
        emprenteur=Emprunt(id_client=client,id_livre=livre,date_emprunt=date_emprunt,date_retour_prevue=date_retour_prevue)
        emprenteur.save()

        client.save()
        return HttpResponseRedirect(reverse('displayBooks'))
    else:
        return HttpResponseRedirect(reverse("login"))
    
    
        
def login(request):
    if request.method=='GET':
        return  render(request,'login.html')
    else:
        email=request.POST['email']
        password=request.POST['password']
        user=Clients.objects.filter(email=email).first()
        if user:
            if check_password(password,user.password):
                if user.role=='user':
                    request.session['user']=email
                    return HttpResponseRedirect(reverse('displayBooks'))
                else:
                    request.session['admin']=email
                    return HttpResponseRedirect("/admin_system")
            else:
                return  render(request,'login.html',{'message':"password n'est pas corecte "})
                # return HttpResponse("password n'est pas corecte ")
        else:
            return  render(request,'login.html',{'message':"user n'est pas enregestre"})
            # return HttpResponse("user n'est pas enregestre")
def logout(request):
    # del request.session['user']
    request.session.flush()
    return HttpResponseRedirect(reverse('displayBooks'))