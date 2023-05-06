from django.shortcuts import render
import requests

# Create your views here.
def entradaPefiles(request):
    return render(request, "perfiles.html")

def entradaPrincipal(request):
    return render(request, "principal.html")

def entradaMensajes(request):
    return render(request, "mensajes.html")

