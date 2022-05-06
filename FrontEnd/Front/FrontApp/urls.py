from django.urls import path

from  FrontApp import views

urlpatterns = [
    
    path('', views.home, name="Home"),
    path('loadfile', views.loadfile, name="Load File"),
    path('peticiones', views.getPruebaFromServer, name="Request"),
    path('ayuda', views.ayuda, name="Help"),
    path('delete', views.eliminar, name="Eliminar_Prueba"),
    path('pdf', views.pdf, name="pdf_prueba"),
    
    
]