from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gestionDeBibiliotheque.urls')),
    path('admin_system/', include('admin_system.urls')),
   
]


if settings.DEBUG:  # Only serve media in development, not in production!
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
