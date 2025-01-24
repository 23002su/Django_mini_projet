from django.urls import path
from . import views

urlpatterns = [
    path("",views.displayBooks,name="displayBooks"),
    path("borrowed_books",views.myBooks,name="myBooks"),
    path("coins/purchase",views.CoinsPromodisplay,name="CoinsPromodisplay"),
    path("book/<int:id>",views.ClickedBook,name="ClickedBook"),
    path("emprent_liver/<int:id>",views.emprent_liver,name="emprent_liver"),
    path("emprent_avec_livreson/<int:id>",views.emprent_avec_livreson,name="emprent_avec_livreson"),
    path("cancel",views.cancel,name="cancel"),
    path("regester",views.regester,name="regester"),
    path("login",views.login,name="login"),
    path("deconenction", views.logout, name="logout"),
]