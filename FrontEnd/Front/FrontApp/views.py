from django.shortcuts import render, HttpResponse

def home(request):
    return render(request, "FrontApp/home.html")

def loadfile(request):
    return render(request, "FrontApp/loadfile.html")

def peticiones(request):
    return render(request, "FrontApp/peticiones.html")

def ayuda(request):
    return render(request, "FrontApp/ayuda.html")

