from django.shortcuts import render
from .models import Livre

# Create your views here.

def createlivre(request):
    livres = Livre.objects.all()
    return render(request, 'inde.html',{'livres':livres})