from django.urls import path,include
from . import views

urlpatterns=[
    path('ajout_liver',views.ajout_liver,name='ajout_liver'),
]