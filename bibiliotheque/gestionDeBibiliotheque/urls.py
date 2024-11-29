from django.urls import path
from . import views

urlpatterns = [
    path("",views.createlivre,name="createlivre"),
]