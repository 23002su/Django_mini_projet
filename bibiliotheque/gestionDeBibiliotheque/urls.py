from django.urls import path
from . import views

urlpatterns = [
    path("books",views.displayBooks,name="displayBooks"),
    path("coins/purchase",views.CoinsPromodisplay,name="CoinsPromodisplay"),
    path("regester",views.regester,name="regester"),
    path("login",views.login,name="login"),
    path("deconenction", views.logout, name="logout"),
]