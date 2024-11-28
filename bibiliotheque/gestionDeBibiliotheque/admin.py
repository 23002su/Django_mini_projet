from django.contrib import admin
from .models import Livre,Clients,Emprunt

# Register your models here.

admin.site.register(Livre)
admin.site.register(Clients)
admin.site.register(Emprunt)