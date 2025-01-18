from django.urls import path
from . import views

urlpatterns = [
    path("",views.displayBooks,name="displayBooks"),
    path("book/<id>",views.ClickedBook,name="ClickedBook"),
    path("emprent_liver/<id>",views.emprent_liver,name="emprent_liver"),
    path("emprent_avec_livreson/<id>",views.emprent_avec_livreson,name="emprent_avec_livreson"),
    path("cancel",views.cancel,name="cancel"),
    path("regester",views.regester,name="regester"),
    path("login",views.login,name="login"),
    path("deconenction", views.logout, name="logout"),
]