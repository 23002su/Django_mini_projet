from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.hashers import make_password,check_password
from gestionDeBibiliotheque.models import *
from django.core.paginator import Paginator
from django.core.cache import cache



def no_cache(view_func):
    def _wrapped_view_func(request, *args, **kwargs):
        response = view_func(request, *args, **kwargs)
        response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
        response['Pragma'] = 'no-cache'
        response['Expires'] = '0'
        return response
    return _wrapped_view_func
@no_cache
# Create your views here.
def ajout_liver(request):
    if 'admin' in request.session:
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
    else:
         return HttpResponseRedirect('/login')
@no_cache
def update_liver(request,id):
    if 'admin' in request.session:
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
    else:
        return HttpResponseRedirect('/login')
@no_cache
def update_client(request,id):
    if 'admin' in request.session:
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
    else:
        return HttpResponseRedirect('/login')
@no_cache
def affiche_livre(request):
    if 'admin' in request.session:
        email_admin=request.session['admin']
        livres=Livre.objects.all()
        paginator = Paginator(livres, 4)
        
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request,'admin/affiche_livre.html',{'livres':page_obj,'admin_conect':email_admin})
    else:
         return HttpResponseRedirect('/login')
     
@no_cache
def affiche_cliens(request):
    if 'admin' in request.session:
        email_admin=request.session['admin']
        clients=Clients.objects.all()
        return render(request,'admin/affiche_cliens.html',{'clients':clients,'admin_conect':email_admin})
    else:
        return HttpResponseRedirect('/login')
@no_cache
def delete(request,id):
    if 'admin' in request.session:
        liver=Livre.objects.filter(id=id).first()
        liver.delete()
        return HttpResponseRedirect(reverse('affiche_livre'))
    else:
        return HttpResponseRedirect('/login')
@no_cache
def test(request):
    return render(request,'admin/test.html')
@no_cache
def ajoute_clients(request):
    if 'admin' in request.session:
        
        nom=request.POST['nom']
        prenom=request.POST['prenom']
        email=request.POST['email']
        tel=request.POST['tel']
        age=request.POST['age']
        password=make_password(request.POST['password'])
        user=Clients(nom=nom,prenom=prenom,email=email,password=password,tel=tel,age=age)
        user.save()
        return HttpResponseRedirect(reverse('affiche_cliens'))
    else:
        return HttpResponseRedirect('/login')
@no_cache
def delete_clients(request,id):
    if 'admin' in request.session:
        
        client=Clients.objects.filter(id=id).first()
        client.delete()
        return HttpResponseRedirect(reverse('affiche_cliens'))
    else:
        return HttpResponseRedirect('/login')
@no_cache
def login(request):
    return HttpResponseRedirect('/login')
@no_cache
def deconection(request):
    request.session.flush()
    return HttpResponseRedirect('/login')
@no_cache
def affiche_liver_emprente(request):
    if 'admin' in request.session:
        email_admin=request.session['admin']
        list_empret=Emprunt.objects.filter(status='indisponible').all()
        paginator = Paginator(list_empret, 4)   
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request,'admin/affiche_le_liver_emprente.html',{'list_liver':page_obj,'admin_conect':email_admin})
    else:
        return HttpResponseRedirect('/login')
@no_cache
def changeetat(request,id):
    if 'admin' in request.session:
        liver_emp=Emprunt.objects.filter(id=id).first()
        liver_emp.status='disponible'
        id_liver=liver_emp.id_livre.id
        liver=Livre.objects.filter(id=id_liver).first()
        id_liver.status='disponible'
        liver.count+=1
        liver.save()
        liver_emp.save()
        return HttpResponseRedirect(reverse('affiche_liver_emprente'))
    else:
        return HttpResponseRedirect('/login')
@no_cache
def hh(request):
    return HttpResponseRedirect('/admin_system/purchases/')