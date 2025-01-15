from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password,check_password
from django.http import HttpResponse,HttpResponseRedirect
from .models import *


# Create your views here.

def displayBooks(request):
    livres = Livre.objects.all().filter(status='disponible')
    return render(request, 'index.html',{'livres':livres})

def ClickedBook(request, id):
    livres = Livre.objects.all().filter(status='disponible')
    try:
        selectedbook = Livre.objects.get(id=id)
    except Livre.DoesNotExist:
        selectedbook = None
    return render(request, 'index.html',{'livres':livres, 'selectedbook':selectedbook})

def cancelClickedBook(request):
    return redirect('displayBooks')

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
        return HttpResponse("user est insert ")
def login(request):
    if request.method=='GET':
        return  render(request,'login.html')
    else:
        email=request.POST['email']
        password=request.POST['password']
        user=Clients.objects.filter(email=email).first()
        if user:
            if check_password(password,user.password):
                return HttpResponse("vrai")
            else:
                return HttpResponse("no")
        else:
            return HttpResponse("no")
        