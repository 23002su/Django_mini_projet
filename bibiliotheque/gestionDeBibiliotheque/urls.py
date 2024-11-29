from django.urls import path
from . import views

urlpatterns = [
    path("",views.createlivre,name="createlivre"),
    path("regester",views.regester,name="regester"),
    path("login",views.login,name="login"),
]