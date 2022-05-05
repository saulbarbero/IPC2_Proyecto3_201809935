from django.urls import path

from  FrontApp import views

urlpatterns = [
    
    path('', views.home, name="Home"),
    path('loadfile', views.loadfile, name="Load File"),
    path('peticiones', views.getPruebaFromServer, name="Request"),
    path('ayuda', views.ayuda, name="Help"),
    path('delete', views.pruebasDelete, name="delete"),
    
]