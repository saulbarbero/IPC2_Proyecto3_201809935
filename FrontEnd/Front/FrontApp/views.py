import json
from django.shortcuts import render, HttpResponse
from .models import Prueba, SentimientosEmpresa
import requests
import pdfkit



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
        SentimientosEmpresa.objects.create(nombre=prueba['nombre'], totalMensajes=prueba['totalMensajes'],positivos=prueba['positivos'], negativos=prueba['negativos'], neutrales=prueba['neutrales'] )

    return render(request,"FrontApp/peticiones.html",{'SentimientosEmpresa': SentimientosEmpresa.objects.all()})    #Tambien se puede mandar solo la lista

def getPruebas():
    return json.loads(requests.get('http://127.0.0.1:5000/prueba').text)


def eliminar(request):
    ob = Prueba.objects.all()
    ob.delete()
    return render(request,"FrontApp/peticiones.html",{'Ob':ob}) 
def pdf(request):
    pdfkit.from_url('http://127.0.0.1:8000/peticiones','./out.pdf')

    return render(request,"FrontApp/peticiones.html") 


def palabras(request):
    
    result=""
    if requests.method == "POST":
        text = requests.POST.get("textarea1")
        sendInfo(text)
        result=text
        print(result)
    context={"result":result}
    return render(request,"FrontApp/home.html",context) 

def sendInfo(texto):
    data = {"texto":texto}
    response = requests.post('http://127.0.0.1:5000/palabra',json=data)
    print(response.text)