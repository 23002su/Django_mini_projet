from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gestionDeBibiliotheque.urls')),
    path('admin_system/', include('admin_system.urls')),
   
]
