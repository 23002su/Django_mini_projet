from django.urls import path,include
from . import views

urlpatterns=[
    path('',views.affiche_livre,name='affiche_livre'),
    path('login',views.login,name='login'),
    path('deconection',views.deconection,name='deconection'),
    path('cliens',views.affiche_cliens,name='affiche_cliens'),
    path('update_client/<id>',views.update_client,name='update_client'),
    path('ajout_liver',views.ajout_liver,name='ajout_liver'),
    path('update_liver/<id>',views.update_liver,name='update_liver'),
    path('delete/<id>',views.delete,name='delete'),
    path('test',views.test,name='test'),
    path('ajoute_clients',views.ajoute_clients,name='ajoute_clients'),
    path('delete_clients/<id>',views.delete_clients,name='delete_clients'),
]