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
    elif "admin" in request.session:
        admin_conect=request.session['admin']
        return render(request, 'index.html', {'livres': livres, 'admin_conect':admin_conect })
    else:
        return render(request, 'index.html', {'livres': livres})

def CoinsPromodisplay(request):
    coins_promos = CoinsPromo.objects.filter(is_active=True)
    if "user" in request.session:
        user_conect=request.session['user']
        return render(request, 'coinsPromo.html', {'coins_promos': coins_promos, 'user_conect':user_conect })
    elif "admin" in request.session:
        admin_conect=request.session['admin']
        return render(request, 'coinsPromo.html', {'coins_promos': coins_promos, 'admin_conect':admin_conect })
    else:
        return render(request, 'coinsPromo.html', {'coins_promos': coins_promos})

def myBooks(request):
    if "user" in request.session:
        user_conect=request.session["user"]
        client=Clients.objects.filter(email=user_conect).first()
        # Get all borrowed books (Emprunt) by the client
        emprunts = Emprunt.objects.filter(id_client=client)
        
        # Extract book IDs from the emprunts queryset
        book_ids = emprunts.values_list('id_livre', flat=True)
        
        # Retrieve books using the extracted IDs
        books = Livre.objects.filter(id__in=book_ids)
        
        return render(request, 'myBooks.html', {'mybooks': books, 'user_conect': user_conect})
    else:
        return HttpResponseRedirect(reverse('displayBooks'))

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
            return redirect('CoinsPromodisplay')
        client.nbr_point=client.nbr_point-50
        date_emprunt=datetime.today().date()
        date_retour_prevue =datetime.today().date()+timedelta(days=4)
        livre =Livre.objects.filter(id=int(id)).first()
        
        emprenteur=Emprunt(id_client=client,id_livre=livre,date_emprunt=date_emprunt,date_retour_prevue=date_retour_prevue)
        emprenteur.save()

        client.save()
        return redirect("displayBooks")
    else:
        return HttpResponseRedirect(reverse("login"))
def emprent_avec_livreson(request,id):
    if "user" in request.session:
        email=request.session['user']
        client=Clients.objects.filter(email=email).first()
        if client.nbr_point==0:
            return redirect('CoinsPromodisplay')
        client.nbr_point=client.nbr_point-75
        date_emprunt=datetime.today().date()
        date_retour_prevue =datetime.today().date()+timedelta(days=4)
        livre =Livre.objects.filter(id=int(id)).first()
        
        emprenteur=Emprunt(id_client=client,id_livre=livre,date_emprunt=date_emprunt,date_retour_prevue=date_retour_prevue)
        emprenteur.save()

        client.save()
        return redirect('displayBooks')
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
                    return redirect('displayBooks')
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






















# CoinsPromo.objects.create(
#     name="Welcome Bundle",
#     description="Get started with our exclusive welcome offer and receive bonus coins to explore!",
#     coins=500,
#     bonus_coins=50,
#     price=4.99 * 37,  # Converted to MRU
#     is_active=True
#     )

#     CoinsPromo.objects.create(
#         name="Weekend Booster Pack",
#         description="Limited-time offer! Get extra coins and bonus rewards this weekend only.",
#         coins=1000,
#         bonus_coins=200,
#         price=9.99 * 37,  # Converted to MRU
#         is_active=True
#     )

#     CoinsPromo.objects.create(
#         name="Monthly Mega Bundle",
#         description="Save big with our best-value monthly promotion. Perfect for frequent users!",
#         coins=5000,
#         bonus_coins=1000,
#         price=39.99 * 37,  # Converted to MRU
#         is_active=True
#     )

#     CoinsPromo.objects.create(
#         name="Flash Sale 2X Bonus",
#         description="Double your rewards during this limited-time flash sale!",
#         coins=1000,
#         bonus_coins=1000,
#         price=14.99 * 37,  # Converted to MRU
#         is_active=True
#     )

#     CoinsPromo.objects.create(
#         name="Holiday Cheer Pack",
#         description="Celebrate the season with a festive coin bundle and huge bonuses!",
#         coins=3000,
#         bonus_coins=750,
#         price=24.99 * 37,  # Converted to MRU
#         is_active=True
#     )

#     CoinsPromo.objects.create(
#         name="Starter Pack",
#         description="A small, affordable pack for first-time buyers.",
#         coins=300,
#         bonus_coins=30,
#         price=2.99 * 37,  # Converted to MRU
#         is_active=True
#     )

#     CoinsPromo.objects.create(
#         name="Loyalty Rewards Pack",
#         description="As a token of appreciation, we’re offering bonus coins exclusively for our loyal users!",
#         coins=2000,
#         bonus_coins=400,
#         price=19.99 * 37,  # Converted to MRU
#         is_active=True
#     )

#     CoinsPromo.objects.create(
#         name="Ultimate Collector's Bundle",
#         description="For the ultimate player! Unlock massive rewards with this premium bundle.",
#         coins=10000,
#         bonus_coins=2500,
#         price=79.99 * 37,  # Converted to MRU
#         is_active=True
#     )

#     CoinsPromo.objects.create(
#         name="Mid-Week Coins Boost",
#         description="Beat the mid-week slump with this surprise bonus offer.",
#         coins=800,
#         bonus_coins=160,
#         price=6.99 * 37,  # Converted to MRU
#         is_active=True
#     )

#     CoinsPromo.objects.create(
#         name="Anniversary Special",
#         description="Celebrate with us! Enjoy an exclusive promotion to mark our anniversary.",
#         coins=4000,
#         bonus_coins=800,
#         price=29.99 * 37,  # Converted to MRU
#         is_active=True
#     )