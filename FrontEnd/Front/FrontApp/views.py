import json
from django.shortcuts import render, HttpResponse
from .models import Prueba
import requests



def home(request):
    return render(request, "FrontApp/home.html")

def loadfile(request):
    return render(request, "FrontApp/loadfile.html")

def peticiones(request):
   
    return render(request, "FrontApp/peticiones.html") #Tambien se puede mandar solo la lista

def ayuda(request):
    return render(request, "FrontApp/ayuda.html")

def getPruebaFromServer(request):
    list = getPruebas()

    for prueba in list:
        print(prueba)
        Prueba.objects.create(nombre=prueba['nombre'], positivos=prueba['positivos'], negativos=prueba['negativos'] )

    return render(request,"FrontApp/peticiones.html",{'ObjetoPruebas': Prueba.objects.all()})    #Tambien se puede mandar solo la lista

def getPruebas():
    return json.loads(requests.get('http://127.0.0.1:5000/prueba').text)


def pruebasDelete(request):
    Prueba.objects.delete()

    return HttpResponse("Delete")