from django.shortcuts import render
from django.contrib.auth.hashers import make_password,check_password
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import *

# Create your views here.

def displayBooks(request):
    livres = Livre.objects.all()
    return render(request, 'index.html',{'livres':livres})
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
        user=Clients(nom=nom,prenom=prenom,email=email,password=password,tel=tel,age=age,role='admin')
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
                if user.role=='user':
                    request.session['user']='user'
                    return HttpResponseRedirect(reverse('displayBooks'))
                else:
                    request.session['user']='admin'
                    return HttpResponseRedirect("/admin_system")
            else:
                return  render(request,'login.html',{'message':"password n'est pas corecte "})
                # return HttpResponse("password n'est pas corecte ")
        else:
            return  render(request,'login.html',{'message':"user n'est pas enregestre"})
            # return HttpResponse("user n'est pas enregestre")
def logout(request):
    # request.session.flush()
    return HttpResponse("deconection")