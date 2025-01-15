from django.urls import path
from . import views

urlpatterns = [
    path("",views.displayBooks,name="displayBooks"),
    path("book/<int:id>",views.ClickedBook,name="ClickedBook"),
    path("book/cancel",views.cancelClickedBook,name="cancelClickedBook"),
    path("regester",views.regester,name="regester"),
    path("login",views.login,name="login"),
]